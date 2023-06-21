from pyspark.sql import SparkSession
from tests.test_helpers.verification_helpers import verify_will_replace_null_values_with_floating_averages


def test_will_replace_null_prices_with_floating_averages(spark: SparkSession) -> None:
    price = [327, None]

    verify_will_replace_null_values_with_floating_averages(spark, price)
   
    