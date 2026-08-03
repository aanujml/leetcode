import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    
    
    valid_df = users[users['mail'].str.match(pattern, na=False)]
    
    return valid_df