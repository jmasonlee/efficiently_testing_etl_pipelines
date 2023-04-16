from src.project import replace_null_prices_with_floating_averages
from approvaltests import verify
from pyspark.sql import DataFrame, Row, SparkSession


def test_will_replace_null_prices_with_floating_averages(spark: SparkSession) -> None:
    output_df_as_str = impute_null_values_for_diamond(spark, price=327, cut = "good", clarity = "SI2", color = "A")

    verify(output_df_as_str)

def get_string_representation_of_dataframe(df: DataFrame) -> str:
    return df.toPandas().to_string(header=True, index=False)

def impute_null_values_for_diamond(spark: SparkSession, price:float, cut: str, clarity: str, color: str) -> str:
    input_df = spark.createDataFrame([
        Row(price=price,cut=cut,clarity=clarity,color=color)
    ])
    output_df = replace_null_prices_with_floating_averages(input_df)
    
    return get_string_representation_of_dataframe(output_df)
    