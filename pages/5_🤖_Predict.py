import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.preprocess import preprocess
from utils.model import train_model


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(

    page_title="Predict",

    page_icon="🤖",

    layout="wide"

)


# ==========================
# LOAD CSS
# ==========================

with open("assets/style.css") as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True

    )


# ==========================
# LOAD MODEL
# ==========================

with st.spinner("Đang tải mô hình..."):

    df = load_data()

    customer = preprocess(df)

    customer, model, scaler = train_model(

        customer,

        k=4

    )


# ==========================
# HEADER
# ==========================

st.title("🤖 Customer Cluster Prediction")

st.write(

    "Dự đoán nhóm khách hàng và đề xuất Marketing"

)

st.markdown("---")


# ==========================
# INPUT
# ==========================

col1,col2=st.columns(2)


with col1:

    age = st.number_input(

        "Age",

        18,

        100,

        30

    )


    balance = st.number_input(

        "Average Balance",

        0,

        1000000,

        50000

    )


    total_transaction = st.number_input(

        "Total Transaction",

        0,

        1000000,

        10000

    )



with col2:

    avg_transaction = st.number_input(

        "Average Transaction",

        0,

        100000,

        2000

    )


    transaction_count = st.number_input(

        "Transaction Count",

        1,

        1000,

        20

    )


st.write("")


# ==========================
# PREDICT
# ==========================

if st.button(

    "🔮 Predict Cluster",

    use_container_width=True

):


    data = pd.DataFrame(

        {

            'Age':[age],

            'AvgBalance':[balance],

            'TotalTransaction':[

                total_transaction

            ],

            'AvgTransaction':[

                avg_transaction

            ],

            'TransactionCount':[

                transaction_count

            ]

        }

    )


    X = scaler.transform(

        data

    )


    cluster = model.predict(

        X

    )[0]


    st.success(

        f"✅ Customer belongs to Cluster {cluster}"

    )


    st.markdown("---")


    if balance > 200000:


        st.markdown(

        """

        # 👑 VIP Customer


        ### Marketing Strategy

        ✅ Priority Banking

        ✅ Platinum Credit Card

        ✅ Wealth Management

        ✅ Personal Advisor


        ### Recommended Channel

        - Email Marketing

        - Personal Consultant

        - VIP Events

        """

        )


    elif avg_transaction > 5000:


        st.markdown(

        """

        # 💼 Frequent Transaction Customer


        ### Marketing Strategy

        ✅ Cashback

        ✅ Loyalty Program

        ✅ Mobile Banking Premium

        ✅ Cross-selling


        ### Recommended Channel

        - Push Notification

        - SMS

        - Mobile App

        """

        )


    else:


        st.markdown(

        """

        # 🎓 Regular Customer


        ### Marketing Strategy

        ✅ Online Saving

        ✅ SMS Marketing

        ✅ Mobile Banking

        ✅ Transfer Promotion


        ### Recommended Channel

        - SMS

        - Facebook

        - Zalo OA

        """

        )