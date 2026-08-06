import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    col_name = f'getNthHighestSalary({N})'
   
    if N <= 0 or len(unique_salaries) < N:
        return pd.DataFrame({col_name: [None]})
    
    
    nth_salary = unique_salaries.iloc[N - 1]
    
    return pd.DataFrame({col_name: [nth_salary]})