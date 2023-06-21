import json

from pyspark.sql import SparkSession

from src.linear_regression_prep import transform
from tests.test_helpers.json_helpers import create_df_from_json, data_frame_to_json


def test_prep_for_linear_regression(spark: SparkSession):
    diamonds_df = create_df_from_json("tests/fixtures/diamonds.json", spark)

    actual_df = transform(diamonds_df)
    assert data_frame_to_json(actual_df) == expected_json()


def expected_json():
    with open("tests/fixtures/expected.json") as f:
        return json.loads(f.read())