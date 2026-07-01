import pandas as pd

def test_no_missing_values():
    df = pd.read_csv("bank.csv")
    assert df.isnull().sum().sum() == 0, "Dataset contains missing values"

def test_no_duplicate_rows():
    df = pd.read_csv("bank.csv")
    assert df.duplicated().sum() == 0, "Dataset contains duplicate rows"

def test_required_columns_exist():
    df = pd.read_csv("bank.csv")
    required_columns = [
        "age", "job", "marital", "education", "default", "balance",
        "housing", "loan", "contact", "day", "month", "duration",
        "campaign", "pdays", "previous", "poutcome", "deposit"
    ]

    for col in required_columns:
        assert col in df.columns, f"Missing required column: {col}"
