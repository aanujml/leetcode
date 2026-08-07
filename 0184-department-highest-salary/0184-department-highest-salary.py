import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    if employee.empty or department.empty:
        return pd.DataFrame(columns=['Department', 'Employee', 'Salary'])
    
    # Calculate max salary for each department
    employee['max_salary'] = employee.groupby('departmentId')['salary'].transform('max')
    
    # Filter employees having highest salary in their department
    highest = employee[employee['salary'] == employee['max_salary']]
    
    # Merge with Department table to get department name
    result = highest.merge(department, left_on='departmentId', right_on='id')
    
    # Rename and select output columns
    result = result.rename(columns={
        'name_y': 'Department',
        'name_x': 'Employee',
        'salary': 'Salary'
    })
    
    return result[['Department', 'Employee', 'Salary']]