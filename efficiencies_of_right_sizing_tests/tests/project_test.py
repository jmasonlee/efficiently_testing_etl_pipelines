from src.project import replace_null_prices_with_floating_averages
from approvaltests import verify
from pyspark.sql import DataFrame

def test_will_replace_null_prices_with_floating_averages(spark) -> None:
    df = spark.createDataFrame([{"price": 327, "cut": "good", "clarity": "SI2"}])
    df = replace_null_prices_with_floating_averages(df)
    
    verify(get_string_representation_of_dataframe(df))

def get_string_representation_of_dataframe(df: DataFrame) -> str:
    str_df = df.toPandas().to_string(header=True, index=False)
    for name, dtype in df.dtypes:
        str_df = str_df.replace(name, f"{name}::{dtype}")
    return str_df