import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders['customerId'])]
    
    # Required column select karke rename karo
    return df[['name']].rename(columns={'name': 'Customers'})