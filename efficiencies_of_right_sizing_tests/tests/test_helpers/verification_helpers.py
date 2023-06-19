from typing import List

from approvaltests import verify_all_combinations, Options
from approvaltests.scrubbers.scrubbers import create_regex_scrubber
from pyspark.sql import Row, SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

from efficiencies_of_right_sizing_tests.src.diamond_pricing import replace_null_prices_with_floating_averages


def verify_will_replace_null_values_with_floating_averages(
        spark, price: List[float], cut: List[str] = [], clarity: List[str] = [], color: List[str] = []
) -> None:
    arguments = [[spark], price]
    if cut:
        arguments.append(cut)
    if clarity:
        arguments.append(clarity)
    if color:
        arguments.append(color)

    return verify_all_combinations(impute_null_values_for_diamond, arguments, options=Options().with_scrubber(
        create_regex_scrubber("<pyspark.sql.session.SparkSession object at (.*?)>", "[SparkSession]")
    ))


def impute_null_values_for_diamond(spark: SparkSession, price: float, cut: str = "good", clarity: str = "SI2",
                                   color: str = "A") -> str:
    schema = StructType([
        StructField("id", IntegerType()),
        StructField("price", IntegerType()),
        StructField("cut", StringType()),
        StructField("clarity", StringType()),
        StructField("color", StringType()),
    ])

    input_df = spark.createDataFrame(
        schema=schema,
        data=[
            Row(id=1, price=price, cut=cut, clarity=clarity, color=color),
            Row(id=2, price=300, cut=cut, clarity=clarity, color=color),
        ]
    )

    output_df = replace_null_prices_with_floating_averages(input_df)

    return output_df.where(output_df.id == 1).first()['price']
