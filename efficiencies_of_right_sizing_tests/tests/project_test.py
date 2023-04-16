from src.project import replace_null_prices_with_floating_averages
from approvaltests import verify
from pyspark.sql import DataFrame

def test_will_replace_null_prices_with_floating_averages(spark) -> None:
    input_df = spark.createDataFrame([{"price": 327, "cut": "good", "clarity": "SI2"}])
    output_df = replace_null_prices_with_floating_averages(input_df)
    
    test_case = f"{get_string_representation_of_dataframe(input_df)}\n------- WITH NULL PRICES REPLACED -------\n{get_string_representation_of_dataframe(output_df)}"
    verify(test_case)

def get_string_representation_of_dataframe(df: DataFrame) -> str:
    return df.toPandas().to_string(header=True, index=False)
    