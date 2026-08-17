import pandas as pd
import numpy as np

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts["category"] = np.select(
        [
            accounts["income"] < 20000,
            accounts["income"] <= 50000
        ],
        [
            "Low Salary",
            "Average Salary"
        ],
        default="High Salary"
    )

    categories = ["Low Salary", "Average Salary", "High Salary"]

    return (
        accounts["category"]
        .value_counts()
        .reindex(categories, fill_value=0)
        .rename_axis("category")
        .reset_index(name="accounts_count")
    )