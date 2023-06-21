"""
Program written by Jeff Levy (jlevy@urban.org) for the Urban Institute, last revised 8/24/2016.
Note that this is intended as a temporary work-around until pySpark improves its ML package.

Tested in pySpark 2.0.

"""
import pyspark


def build_indep_vars(df, independent_vars, categorical_vars=None, keep_intermediate=False, summarizer=True):
    check_input(categorical_vars, df, independent_vars)

    from pyspark.ml import Pipeline
    from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
    idx = 'index'
    vec = 'vector'
    if categorical_vars:
        string_indexer = [StringIndexer(inputCol=x,
                                        outputCol=f"{x}_{idx}")
                          for x in categorical_vars]

        encoder        = [OneHotEncoder(dropLast=True,
                                        inputCol =f'{x}_{idx}',
                                        outputCol=f'{x}_{vec}')
                          for x in categorical_vars]

        independent_vars = ['{}_vector'.format(x) if x in categorical_vars else x for x in independent_vars]
    else:
        string_indexer, encoder = [], []

    assembler = VectorAssembler(inputCols=independent_vars,
                                outputCol='indep_vars')
    pipeline  = Pipeline(stages=string_indexer+encoder+[assembler])
    model = pipeline.fit(df)
    df = model.transform(df)

    if not keep_intermediate:
        fcols = [c for c in df.columns if f'_{idx}' not in c[-3:] and f'_{vec}' not in c[-7:]]
        df = df[fcols]

    return df


def check_input(categorical_vars, df, independent_vars):
    assert (type(
        df) is pyspark.sql.dataframe.DataFrame), 'pypark_glm: A pySpark dataframe is required as the first argument.'
    assert (type(
        independent_vars) is list), 'pyspark_glm: List of independent variable column names must be the third argument.'
    for iv in independent_vars:
        assert (type(iv) is str), 'pyspark_glm: Independent variables must be column name strings.'
        assert (iv in df.columns), 'pyspark_glm: Independent variable name is not a dataframe column.'
    if categorical_vars:
        for cv in categorical_vars:
            assert (type(cv) is str), 'pyspark_glm: Categorical variables must be column name strings.'
            assert (cv in df.columns), 'pyspark_glm: Categorical variable name is not a dataframe column.'
            assert (cv in independent_vars), 'pyspark_glm: Categorical variables must be independent variables.'
