from pyspark.sql import Window, DataFrame, Column
from pyspark.sql.functions import mean

from pyspark.sql.functions import when, col

def replace_null(orig: Column, average: Column):
    """replace_null

    Args:
        orig (Column): The original column
        average (double): the mean for that column

    Returns:
        Column: The original column with null values replaced by the average
    """
    return when(orig.isNull(), average).otherwise(orig)

def replace_null_prices_with_floating_averages(df: DataFrame) -> DataFrame:
    """replace_null_prices_with_floating_averages

    Args:
        df (DataFrame): A pyspark dataframe containing information about diamond prices. Expected format:
        
        +-----+---------+-----+-------+-----+-----+-----+----+----+----+
        |carat|      cut|color|clarity|depth|table|price|   x|   y|   z|
        +-----+---------+-----+-------+-----+-----+-----+----+----+----+
        | 0.23|    Ideal|    E|    SI2| 61.5| 55.0|  326|3.95|3.98|2.43|
        | 0.21|  Premium|    E|    SI1| 59.8| 61.0|  326|3.89|3.84|2.31|
        | 0.23|     Good|    E|    VS1| 56.9| 65.0| null|4.05|4.07|2.31|
        | 0.29|  Premium|    I|    VS2| 62.4| 58.0|  334| 4.2|4.23|2.63|
        | 0.31|     Good|    J|    SI2| 63.3| 58.0|  335|4.34|4.35|2.75|

    Returns:
        DataFrame: A dataframe where any null values in price have been replaced with 
        the average price for that day of all diamonds with the same cut, color, and clarity.
    """

    window = Window.partitionBy('cut', 'clarity').orderBy('price').rowsBetween(-3, 3)
    moving_avg = mean(df['price']).over(window)
    df = df.withColumn('moving_avg', moving_avg)

    df_new = df.withColumn('imputed', replace_null(col('price'), col('moving_avg')))

    return df_new
