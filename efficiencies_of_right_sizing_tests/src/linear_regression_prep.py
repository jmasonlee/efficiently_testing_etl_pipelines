from pyspark.sql import DataFrame
from pyspark.sql.functions import log

def prep_for_linear_regression(df: DataFrame):
    df = df[['carat', 'clarity', 'price']]

    df = df.withColumn('lprice', log('price'))