import streamlit as st


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(

    page_title="AI Customer Segmentation",

    page_icon="🏦",

    layout="wide",

    initial_sidebar_state="expanded"

)


# ==========================
# LOAD CSS
# ==========================
import os

# Thêm đoạn này vào trước hoặc ngay tại dòng 25
current_dir = os.path.dirname(os.path.abspath(__file__))
css_path = os.path.join(current_dir, "assets", "style.css")

# Sửa lại dòng open file thành css_path
with open(css_path, encoding="utf-8") as f:
with open("assets/style.css", encoding="utf-8") as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True

    )


# ==========================
# SIDEBAR
# ==========================

st.sidebar.image(

    "https://img.icons8.com/fluency/240/bank-building.png",

    width=100

)

st.sidebar.markdown(

"""

# 🏦 AI Banking

### Customer Segmentation

MiniBatchKMeans

---

📊 Dashboard

📈 EDA Analysis

🎯 Customer Segmentation

📢 Marketing Strategy

🤖 Predict Cluster

---

Ứng dụng AI hỗ trợ:

✔ Phân tích dữ liệu

✔ Phân cụm khách hàng

✔ Hỗ trợ Marketing

✔ Dự đoán khách hàng mới

"""

)


# ==========================
# HERO HEADER
# ==========================

st.markdown(

"""

<div class='header'>

<h1 style='font-size:60px;'>

🏦 AI Customer Segmentation System

</h1>

<h3>

Phân khúc khách hàng ngân hàng bằng MiniBatchKMeans

</h3>

<p style='font-size:20px;'>

Ứng dụng AI hỗ trợ phân tích hành vi khách hàng,

tối ưu chiến lược Marketing và nâng cao trải nghiệm ngân hàng.

</p>

</div>

""",

unsafe_allow_html=True

)


st.write("")


# ==========================
# FEATURE CARDS
# ==========================

col1,col2,col3=st.columns(3)


with col1:

    st.markdown(

    """

    <div class='card'>

    <div style='font-size:70px;'>

    📊

    </div>

    <h2>

    Dashboard

    </h2>

    <p>

    Tổng quan dữ liệu khách hàng

    </p>

    </div>

    """,

    unsafe_allow_html=True

    )



with col2:

    st.markdown(

    """

    <div class='card'>

    <div style='font-size:70px;'>

    🎯

    </div>

    <h2>

    Segmentation

    </h2>

    <p>

    Phân cụm khách hàng bằng AI

    </p>

    </div>

    """,

    unsafe_allow_html=True

    )



with col3:

    st.markdown(

    """

    <div class='card'>

    <div style='font-size:70px;'>

    📢

    </div>

    <h2>

    Marketing

    </h2>

    <p>

    Đề xuất chiến lược kinh doanh

    </p>

    </div>

    """,

    unsafe_allow_html=True

    )


st.write("")

st.write("")


# ==========================
# INTRODUCTION
# ==========================

st.markdown(

"""

## 🚀 Chức năng của hệ thống

- 📊 Phân tích dữ liệu giao dịch ngân hàng

- 🎯 Phân cụm khách hàng bằng MiniBatchKMeans

- 📈 Trực quan hóa dữ liệu với PCA

- 📢 Đề xuất chiến lược Marketing theo từng nhóm

- 🤖 Dự đoán khách hàng mới thuộc Cluster nào


---

### 🔥 Công nghệ sử dụng

- Python

- Streamlit

- Pandas

- Plotly

- Scikit-Learn

- MiniBatchKMeans

"""

)


# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.markdown(

"""

<center>

<p style='color:#cbd5e1;'>

© 2026 AI Customer Segmentation System

<br>

MiniBatchKMeans | Streamlit | Plotly

</p>

</center>

""",

unsafe_allow_html=True

)
