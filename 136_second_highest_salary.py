# Get rid of duplicates, return an empty df if 2nd highest salary does not exist, else sort the df using
# salary, get first 2 elements in descending order and give out the last element in that list.

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if len(df) < 2:
        return pd.DataFrame([None], columns=['SecondHighestSalary'])
    return (df.sort_values(by=['salary'], ascending=False).head(2).tail(1)
            .rename(columns={'salary':'SecondHighestSalary'}))