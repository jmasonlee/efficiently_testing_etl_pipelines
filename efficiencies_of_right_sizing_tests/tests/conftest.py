import pytest
from _pytest.fixtures import FixtureRequest
from pyspark import SparkConf
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark(request: FixtureRequest):
    conf = (SparkConf()
        .setMaster("local")
        .setAppName("sample_pyspark_testing_starter"))

    spark = SparkSession \
        .builder \
        .config(conf=conf) \
        .getOrCreate()

    request.addfinalizer(lambda: spark.stop())
    return spark