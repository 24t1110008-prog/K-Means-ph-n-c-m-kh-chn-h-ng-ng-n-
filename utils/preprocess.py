import pandas as pd

def preprocess(df):
    cols = [
        'CustomerID',
        'CustomerDOB',
        'CustAccountBalance',
        'TransactionAmount (INR)'
    ]
    df = df[cols].copy()

    df = df.dropna(
        subset=[
            'CustomerID',
            'CustomerDOB',
            'CustAccountBalance',
            'TransactionAmount (INR)'
        ]
    )

    df['CustomerDOB'] = pd.to_datetime(df['CustomerDOB'], errors='coerce', format='%d/%m/%Y')
    df = df.dropna(subset=['CustomerDOB'])

    df['Age'] = 2026 - df['CustomerDOB'].dt.year

    df = df[(df['Age'] >= 18) & (df['Age'] <= 100)]

    customer = (
        df.groupby('CustomerID')
        .agg(
            Age=('Age', 'first'),
            AvgBalance=('CustAccountBalance', 'mean'),
            TotalTransaction=('TransactionAmount (INR)', 'sum'),
            AvgTransaction=('TransactionAmount (INR)', 'mean'),
            TransactionCount=('TransactionAmount (INR)', 'count')
        )
        .reset_index()
    )

    return customer
