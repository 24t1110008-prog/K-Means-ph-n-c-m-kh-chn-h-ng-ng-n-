import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MiniBatchKMeans

from utils.data_loader import load_data
from utils.preprocess import preprocess


# =====================
# PAGE CONFIG
# =====================

st.set_page_config(

    page_title="EDA",

    page_icon="📈",

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

with st.spinner("Đang đọc dữ liệu..."):

    df = load_data()

    customer = preprocess(df)


# =====================
# HEADER
# =====================

st.title("📈 Exploratory Data Analysis")

st.write(

    "Khám phá và trực quan hóa dữ liệu khách hàng"

)

st.markdown("---")


# =====================
# DATA INFO
# =====================

col1,col2,col3=st.columns(3)


with col1:

    st.metric(

        "👥 Customers",

        f"{len(customer):,}"

    )


with col2:

    st.metric(

        "📊 Features",

        customer.shape[1]

    )


with col3:

    st.metric(

        "💰 Avg Balance",

        f"{customer['AvgBalance'].mean():,.0f}"

    )


st.write("")


# =====================
# HISTOGRAM
# =====================

col1,col2=st.columns(2)


with col1:

    st.subheader(

        "👥 Age Distribution"

    )


    fig=px.histogram(

        customer,

        x='Age',

        nbins=40,

        title='Age Histogram'

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



with col2:

    st.subheader(

        "💰 Balance Distribution"

    )


    fig=px.histogram(

        customer,

        x='AvgBalance',

        nbins=40,

        title='Balance Histogram'

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )


# =====================
# HEATMAP
# =====================

st.markdown("---")


st.subheader(

    "🔥 Correlation Heatmap"

)


corr=customer[

    [

        'Age',

        'AvgBalance',

        'TotalTransaction',

        'AvgTransaction',

        'TransactionCount'

    ]

].corr()


fig=ff.create_annotated_heatmap(

    z=corr.values,

    x=list(corr.columns),

    y=list(corr.index),

    annotation_text=round(

        corr,

        2

    ).values,

    showscale=True

)


st.plotly_chart(

    fig,

    use_container_width=True

)


# =====================
# ELBOW METHOD
# =====================

st.markdown("---")


st.subheader(

    "🎯 Elbow Method"

)


X=customer[

    [

        'Age',

        'AvgBalance',

        'TotalTransaction',

        'AvgTransaction',

        'TransactionCount'

    ]

]


scaler=StandardScaler()

X_scaled=scaler.fit_transform(X)


inertia=[]

K=range(2,9)


with st.spinner(

    "Đang tính Elbow Method..."

):

    for k in K:


        model=MiniBatchKMeans(

            n_clusters=k,

            batch_size=2048,

            random_state=42,

            n_init=3

        )


        model.fit(

            X_scaled

        )


        inertia.append(

            model.inertia_

        )


fig=go.Figure()


fig.add_trace(

    go.Scatter(

        x=list(K),

        y=inertia,

        mode='lines+markers'

    )

)


fig.update_layout(

    xaxis_title="K",

    yaxis_title="Inertia",

    title="Elbow Method"

)


st.plotly_chart(

    fig,

    use_container_width=True

)


# =====================
# DATA TABLE
# =====================

st.markdown("---")


st.subheader(

    "📄 Customer Data"

)


st.dataframe(

    customer.head(20),

    use_container_width=True

)