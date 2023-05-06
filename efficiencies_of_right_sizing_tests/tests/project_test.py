from src.project import replace_null_prices_with_floating_averages
from approvaltests import verify_all_combinations, Options
from approvaltests.scrubbers.scrubbers import create_regex_scrubber
from pyspark.sql import DataFrame, Row, SparkSession


def test_will_replace_null_prices_with_floating_averages(spark: SparkSession) -> None:
    price = [327]

    verify_all_combinations(impute_null_values_for_diamond, [[spark], price], options=Options().with_scrubber(
            create_regex_scrubber("<pyspark.sql.session.SparkSession object at (.*?)>", "[SparkSession]")
        ))
   

def impute_null_values_for_diamond(spark: SparkSession, price:float, cut: str = "good", clarity: str = "SI2", color: str = "A") -> str:
    input_df = spark.createDataFrame([
        Row(id=1, price=price,cut=cut,clarity=clarity,color=color)
    ])
    output_df = replace_null_prices_with_floating_averages(input_df)
    
    return output_df.where(output_df.id==1).first()['price']
    