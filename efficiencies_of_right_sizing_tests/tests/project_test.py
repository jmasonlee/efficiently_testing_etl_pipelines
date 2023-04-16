from src.project import replace_null_prices_with_floating_averages
from approvaltests import verify
from pyspark.sql import DataFrame, Row

def test_will_replace_null_prices_with_floating_averages(spark) -> None:
    price=327
    cut = "good"
    clarity = "SI2"
    
    input_df = spark.createDataFrame([Row(price=price,cut=cut,clarity=clarity)])
    output_df = replace_null_prices_with_floating_averages(input_df)
    
    output_df_as_str = get_string_representation_of_dataframe(output_df)
    verify(output_df_as_str)

def get_string_representation_of_dataframe(df: DataFrame) -> str:
    return df.toPandas().to_string(header=True, index=False)
    