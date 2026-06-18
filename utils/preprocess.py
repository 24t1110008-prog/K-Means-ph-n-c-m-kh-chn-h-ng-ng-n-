import pandas as pd


def preprocess(df):

    # Chỉ giữ các cột cần thiết

    cols = [

        'CustomerID',

        'CustomerDOB',

        'CustAccountBalance',

        'TransactionAmount (INR)'

    ]

    df = df[cols].copy()


    # Xóa dòng thiếu ở các cột quan trọng

    df = df.dropna(

        subset=[

            'CustomerID',

            'CustomerDOB',

            'CustAccountBalance',

            'TransactionAmount (INR)'

        ]

    )


    # DOB -> datetime

    df['CustomerDOB'] = pd.to_datetime(

        df['CustomerDOB'],

        errors='coerce',

        dayfirst=True

    )


    # Xóa DOB lỗi

    df = df.dropna(

        subset=['CustomerDOB']

    )


    # Tính tuổi

    df['Age'] = (

        2026

        -

        df['CustomerDOB'].dt.year

    )


    # Lọc tuổi hợp lý

    df = df[

        (df['Age'] >= 18)

        &

        (df['Age'] <= 100)

    ]


    # Gom nhóm khách hàng

    customer = (

        df.groupby(

            'CustomerID'

        )

        .agg(

            Age=('Age','first'),

            AvgBalance=(

                'CustAccountBalance',

                'mean'

            ),

            TotalTransaction=(

                'TransactionAmount (INR)',

                'sum'

            ),

            AvgTransaction=(

                'TransactionAmount (INR)',

                'mean'

            ),

            TransactionCount=(

                'TransactionAmount (INR)',

                'count'

            )

        )

        .reset_index()

    )


    return customer