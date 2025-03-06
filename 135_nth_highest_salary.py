# Get rid of duplicates, return an empty df if Nth highest salary does not exist, else sort the df using
# salary, get first N elements in descending order and give out the last element in that list.

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if N > len(df) or N <= 0:
        return pd.DataFrame([None], columns=[f'getNthHighestSalary({N})'])
    return (df.sort_values(by=['salary'], ascending=False).head(N).tail(1)
                        .rename(columns={'salary' : f'getNthHighestSalary({N})'}))