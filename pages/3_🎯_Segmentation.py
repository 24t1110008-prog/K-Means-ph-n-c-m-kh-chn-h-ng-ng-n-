import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA

from utils.data_loader import load_data
from utils.preprocess import preprocess
from utils.model import train_model


# =====================
# PAGE CONFIG
# =====================

st.set_page_config(

    page_title="Segmentation",

    page_icon="🎯",

    layout="wide"

)


# =====================
# LOAD CSS
# =====================

with open("assets/style.css") as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True

    )


# =====================
# LOAD DATA
# =====================

with st.spinner("Đang phân cụm khách hàng..."):

    df = load_data()

    customer = preprocess(df)

    customer, model, scaler = train_model(

        customer,

        k=4

    )


# =====================
# HEADER
# =====================

st.title("🎯 Customer Segmentation")

st.write(

    "Phân cụm khách hàng bằng thuật toán MiniBatchKMeans"

)

st.markdown("---")


# =====================
# CHỌN K
# =====================

k = st.slider(

    "Số cụm K",

    min_value=2,

    max_value=8,

    value=4

)


customer, model, scaler = train_model(

    customer,

    k=k

)


# =====================
# PCA
# =====================

X = customer[

    [

        'Age',

        'AvgBalance',

        'TotalTransaction',

        'AvgTransaction',

        'TransactionCount'

    ]

]


X_scaled = scaler.transform(X)


pca = PCA(

    n_components=2

)


X_pca = pca.fit_transform(

    X_scaled

)


customer['PCA1'] = X_pca[:,0]

customer['PCA2'] = X_pca[:,1]


# =====================
# PCA PLOT
# =====================

st.subheader(

    "🎯 PCA Scatter Plot"

)


fig = px.scatter(

    customer.sample(

        min(

            15000,

            len(customer)

        ),

        random_state=42

    ),

    x='PCA1',

    y='PCA2',

    color='Cluster',

    opacity=0.6,

    title='Customer Segmentation'

)


st.plotly_chart(

    fig,

    use_container_width=True

)


# =====================
# CLUSTER SIZE
# =====================

st.subheader(

    "📊 Cluster Distribution"

)


cluster_count=(

    customer['Cluster']

    .value_counts()

    .sort_index()

    .reset_index()

)


cluster_count.columns=[

    'Cluster',

    'Customers'

]
fig = px.bar(

    cluster_count,

    x='Cluster',

    y='Customers',

    text_auto=True

)


st.plotly_chart(

    fig,

    use_container_width=True

)


# =====================
# CLUSTER SUMMARY
# =====================

st.markdown("---")

st.subheader(

    "📄 Cluster Summary"

)


summary=(

    customer

    .groupby(

        'Cluster'

    )

    .agg(

        Customers=(

            'CustomerID',

            'count'

        ),

        AvgAge=(

            'Age',

            'mean'

        ),

        AvgBalance=(

            'AvgBalance',

            'mean'

        ),

        AvgTransaction=(

            'AvgTransaction',

            'mean'

        ),

        TransactionCount=(

            'TransactionCount',

            'mean'

        )

    )

    .round(2)

)


st.dataframe(

    summary,

    use_container_width=True

)


# =====================
# MARKETING STRATEGY
# =====================

st.markdown("---")

st.subheader(

    "📢 Marketing Recommendation"

)


for cluster in sorted(

    customer['Cluster'].unique()

):


    st.markdown(

        f"## Cluster {cluster}"

    )


    avg_balance=(

        customer

        [

            customer['Cluster']==cluster

        ]

        ['AvgBalance']

        .mean()

    )


    avg_trans=(

        customer

        [

            customer['Cluster']==cluster

        ]

        ['AvgTransaction']

        .mean()

    )


    if avg_balance > 200000:


        st.success(

            """

            👑 Khách hàng VIP

            • Priority Banking

            • Platinum Credit Card

            • Wealth Management

            • Personal Advisor

            """

        )


    elif avg_trans > 5000:


        st.info(

            """

            💼 Khách hàng giao dịch thường xuyên

            • Cashback

            • Mobile Banking Premium

            • Cross-selling

            • Loyalty Program

            """

        )


    else:


        st.warning(

            """

            🎓 Khách hàng phổ thông

            • SMS Marketing

            • Tiết kiệm Online

            • Mobile Banking

            • Ưu đãi chuyển tiền

            """

        )


# =====================
# CUSTOMER DATA
# =====================

st.markdown("---")

st.subheader(

    "📄 Customer Data"

)


st.dataframe(

    customer.head(30),

    use_container_width=True

)