from pyspark.sql import DataFrame
from pyspark.sql.functions import log

from efficiencies_of_right_sizing_tests.src.build_indep_vars import build_indep_vars


def transform(df: DataFrame) -> DataFrame:
    df = df[['carat', 'clarity', 'color', 'price']]

    df = df.withColumn('lprice', log('price'))
    df = replace_null_prices_with_floating_averages(df)
    df = build_indep_vars(df, ['carat', 'clarity', 'color'],
                                      categorical_vars=['clarity', 'color'],
                                      keep_intermediate=False,
                                      summarizer=True)
    return df
