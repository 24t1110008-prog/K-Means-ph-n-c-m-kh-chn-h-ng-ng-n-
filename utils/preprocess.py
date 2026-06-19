import pandas as pd
import streamlit as st

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

    # Tự động đoán định dạng ngày tháng thay vì ép buộc %d/%m/%Y
    df['CustomerDOB'] = pd.to_datetime(df['CustomerDOB'], errors='coerce')
    df = df.dropna(subset=['CustomerDOB'])

    # Kiểm tra xem sau khi lọc dữ liệu có bị trống không
    if df.empty:
        st.error("Lỗi: Dữ liệu bị trống sau khi xử lý định dạng ngày tháng (CustomerDOB). Hãy kiểm tra lại file dữ liệu gốc!")
        st.stop()

    df['Age'] = 2026 - df['CustomerDOB'].dt.year

    df = df[(df['Age'] >= 18) & (df['Age'] <= 100)]
    
    if df.empty:
        st.error("Lỗi: Không có khách hàng nào nằm trong độ tuổi từ 18 đến 100!")
        st.stop()

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
