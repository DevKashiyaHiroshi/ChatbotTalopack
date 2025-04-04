import google.generativeai as genai
import streamlit as st
import pandas as pd

# Cấu hình API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Khởi tạo model Gemini Pro
model = genai.GenerativeModel("gemini-pro")

# Giao diện người dùng
st.title("📄 Chatbot ISO – TALOPACK (Gemini)")
query = st.text_input("Hỏi tôi về tài liệu ISO bạn cần:")

# Đọc dữ liệu tài liệu
try:
    df = pd.read_csv("iso_data.csv")
except:
    st.error("Không tìm thấy iso_data.csv")
    st.stop()

# Xử lý khi người dùng nhập câu hỏi
if query:
    context = "\n".join([f"{row['Tên']} ({row['Loại']}): {row['Tóm tắt']}" for _, row in df.iterrows()])
    prompt = f"""
Bạn là trợ lý ISO của công ty. Dưới đây là danh sách tài liệu:

{context}

Người dùng hỏi: "{query}". 
Hãy gợi ý tài liệu liên quan (tên, loại, mô tả) nếu có, và gợi ý link nếu tìm thấy.
"""

    try:
        response = model.generate_content(prompt)
        st.markdown("### 📘 Trả lời:")
        st.write(response.text)

    except Exception as e:
        st.error(f"Lỗi gọi Gemini API: {e}")
