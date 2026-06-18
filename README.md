# 🏦 Dự án Phân cụm Khách hàng Ngân hàng (K-Means Clustering)

Dự án này sử dụng thuật toán học máy không giám sát **K-Means** để phân nhóm khách hàng dựa trên hành vi giao dịch công việc, từ đó hỗ trợ phòng Marketing đưa ra các chiến lược tiếp thị phù hợp cho từng phân khúc.

## 📁 Cấu trúc thư mục
* `app.py`: File chạy chính của ứng dụng Streamlit.
* `assets/`: Chứa file `style.css` tùy chỉnh giao diện ứng dụng.
* `pages/`: Các trang chức năng (Dashboard, EDA, Segmentation, Marketing, Predict).
* `utils/`: Các hàm xử lý dữ liệu, tiền xử lý và huấn luyện mô hình K-Means.
* `bank_transactions.csv`: Tập dữ liệu giao dịch của khách hàng.
* `requirements.txt`: Danh sách các thư viện cần cài đặt để chạy dự án.

## 🛠 Hướng dẫn cài đặt và chạy ứng dụng

1. **Cloning dự án hoặc tải về máy máy tính.**
2. **Cài đặt các thư viện cần thiết:**
   ```bash
   pip install -r requirements.txt
