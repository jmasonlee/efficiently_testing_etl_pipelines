from src.project import replace_null_prices_with_floating_averages
def test_I_can_run_tests(spark) -> None:
    df = spark.createDataFrame([{"price": 327, "cut": "good", "clarity": "SI2"}])
    replace_null_prices_with_floating_averages(df)
    assert True