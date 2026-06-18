import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.preprocess import preprocess
from utils.model import train_model


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(

    page_title="Marketing",

    page_icon="📢",

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
# LOAD DATA
# ==========================

with st.spinner("Đang phân tích dữ liệu..."):

    df = load_data()

    customer = preprocess(df)

    customer, model, scaler = train_model(

        customer,

        k=4

    )


# ==========================
# HEADER
# ==========================

st.title("📢 Marketing Recommendation")

st.write(

    "Đề xuất chiến lược Marketing dựa trên kết quả phân cụm khách hàng"

)

st.markdown("---")


# ==========================
# CLUSTER DISTRIBUTION
# ==========================

cluster_count=(

    customer["Cluster"]

    .value_counts()

    .sort_index()

    .reset_index()

)


cluster_count.columns=[

    "Cluster",

    "Customers"

]


fig=px.pie(

    cluster_count,

    names="Cluster",

    values="Customers",

    hole=0.4,

    title="Cluster Distribution"

)


st.plotly_chart(

    fig,

    use_container_width=True

)


st.markdown("---")


# ==========================
# MARKETING STRATEGY
# ==========================

for cluster in sorted(

    customer["Cluster"].unique()

):


    temp=customer[

        customer["Cluster"]==cluster

    ]


    avg_balance=temp[

        "AvgBalance"

    ].mean()


    avg_transaction=temp[

        "AvgTransaction"

    ].mean()


    st.markdown(

        f"# 🎯 Cluster {cluster}"

    )


    col1,col2=st.columns([1,2])


    with col1:


        st.metric(

            "Customers",

            len(temp)

        )


        st.metric(

            "Avg Balance",

            f"{avg_balance:,.0f}"

        )


        st.metric(

            "Avg Transaction",

            f"{avg_transaction:,.0f}"

        )



    with col2:


        if avg_balance > 200000:


            st.success(

            """

            👑 KHÁCH HÀNG VIP

            ### Đặc điểm

            - Số dư tài khoản lớn

            - Giá trị giao dịch cao

            - Tiềm năng sinh lời lớn


            ### Marketing

            ✅ Priority Banking

            ✅ Platinum Credit Card

            ✅ Wealth Management

            ✅ Personal Advisor


            ### Kênh tiếp cận

            - Email cá nhân hóa

            - Chuyên viên tư vấn

            - Sự kiện VIP

            """

            )



        elif avg_transaction > 5000:


            st.info(

            """

            💼 KHÁCH HÀNG GIAO DỊCH THƯỜNG XUYÊN


            ### Đặc điểm

            - Giao dịch nhiều

            - Sử dụng Mobile Banking

            - Tần suất sử dụng cao


            ### Marketing

            ✅ Cashback

            ✅ Loyalty Program

            ✅ Mobile Banking Premium

            ✅ Cross-selling


            ### Kênh tiếp cận

            - Push Notification

            - SMS

            - Mobile App

            """

            )



        else:


            st.warning(

            """

            🎓 KHÁCH HÀNG PHỔ THÔNG


            ### Đặc điểm

            - Số dư thấp

            - Giá trị giao dịch nhỏ

            - Tiềm năng phát triển


            ### Marketing

            ✅ Online Saving

            ✅ SMS Marketing

            ✅ Mobile Banking

            ✅ Transfer Promotion


            ### Kênh tiếp cận

            - SMS

            - Facebook

            - Zalo OA

            """

            )


    st.markdown("---")


# ==========================
# CUSTOMER DATA
# ==========================

st.subheader(

    "📄 Customer Data"

)


st.dataframe(

    customer.head(30),

    use_container_width=True

)