from src.project import replace_null_prices_with_floating_averages
from approvaltests import verify

def test_will_replace_null_prices_with_floating_averages(spark) -> None:
    df = spark.createDataFrame([{"price": 327, "cut": "good", "clarity": "SI2"}])
    df = replace_null_prices_with_floating_averages(df)
    df_columns = df.dtypes
    df_columns = [f"{column[0]}::{column[1]}" for column in df_columns]
    verify(df_columns)