from pyspark.sql import DataFrame
from pyspark.sql.functions import log

from src.build_indep_vars import build_indep_vars
from src.diamond_pricing import replace_null_prices_with_floating_averages


def transform(df: DataFrame) -> DataFrame:

    df = df.withColumn('lprice', log('price'))
    df = replace_null_prices_with_floating_averages(df)
    df = df[['id', 'carat', 'clarity', 'color', 'price']]
    df = build_indep_vars(df, ['carat', 'clarity', 'color'],
                                      categorical_vars=['clarity', 'color'],
                                      keep_intermediate=False,
                                      summarizer=True)
    return df
