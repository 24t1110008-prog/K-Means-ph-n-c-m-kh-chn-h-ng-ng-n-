import streamlit as st
import plotly.express as px
from sklearn.decomposition import PCA
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from utils.data_loader import load_data
from utils.preprocess import preprocess
from utils.model import train_model

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

css_path = os.path.join(parent_dir, "assets", "style.css")
if os.path.exists(css_path):
    with open(css_path, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

with st.spinner("Đang đọc dữ liệu..."):
    df = load_data()
    customer = preprocess(df)
    customer, model, scaler = train_model(customer, k=4)

st.markdown(
"""
<div class='header'>
<h1 style='font-size:50px;'>
📊 Dashboard
</h1>
<h3>
Tổng quan hệ thống phân khúc khách hàng ngân hàng
</h3>
<p>
Phân tích dữ liệu giao dịch và phân cụm khách hàng bằng MiniBatchKMeans
</p>
</div>
""",
unsafe_allow_html=True
)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
    f"""
    <div class='card'>
    <div style='font-size:50px'>
    👥
    </div>
    <div class='big-number'>
    {len(customer):,}
    </div>
    <div class='small-text'>
    Customers
    </div>
    </div>
    """,
    unsafe_allow_html=True
    )

with col2:
    st.markdown(
    f"""
    <div class='card'>
    <div style='font-size:50px'>
    🎯
    </div>
    <div class='big-number'>
    {customer['Cluster'].nunique()}
    </div>
    <div class='small-text'>
    Clusters
    </div>
    </div>
    """,
    unsafe_allow_html=True
    )

with col3:
    st.markdown(
    f"""
    <div class='card'>
    <div style='font-size:50px'>
    💰
    </div>
    <div class='big-number'>
    {customer['AvgTransaction'].mean():,.0f}
    </div>
    <div class='small-text'>
    Avg Transaction
    </div>
    </div>
    """,
    unsafe_allow_html=True
    )

st.write("")
st.write("")

X = customer[['Age', 'AvgBalance', 'TotalTransaction', 'AvgTransaction', 'TransactionCount']]
X_scaled = scaler.transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

customer['PCA1'] = X_pca[:, 0]
customer['PCA2'] = X_pca[:, 1]

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    st.subheader("🎯 PCA Scatter Plot")

    fig_pca = px.scatter(
        customer.sample(10000, random_state=42) if len(customer) > 10000 else customer,
        x='PCA1',
        y='PCA2',
        color='Cluster',
        opacity=0.6,
        template='plotly_dark',
        title='Customer Segmentation',
        height=500
    )

    fig_pca.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(
        fig_pca,
        use_container_width=True,
        key="pca_chart",
        config={'displayModeBar': False}
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    st.subheader("🥧 Cluster Distribution")

    cluster_count = customer['Cluster'].value_counts().reset_index()
    cluster_count.columns = ['Cluster', 'Count']

    fig_pie = px.pie(
        cluster_count,
        names='Cluster',
        values='Count',
        hole=0.45,
        template='plotly_dark',
        height=500
    )

    fig_pie.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True,
        key="pie_chart",
        config={'displayModeBar': False}
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.subheader("💰 Average Balance by Cluster")

avg_balance = customer.groupby('Cluster')['AvgBalance'].mean().reset_index()

fig_bar = px.bar(
    avg_balance,
    x='Cluster',
    y='AvgBalance',
    text_auto=True,
    template='plotly_dark',
    height=500
)

fig_bar.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_title='Cluster',
    yaxis_title='Average Balance'
)

st.plotly_chart(
    fig_bar,
    use_container_width=True,
    key="bar_chart",
    config={'displayModeBar': False}
)

st.markdown("---")
st.subheader("📄 Customer Data")

st.dataframe(
    customer.head(20),
    use_container_width=True
)
