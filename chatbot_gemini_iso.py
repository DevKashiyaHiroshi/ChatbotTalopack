import streamlit as st
import google.generativeai as genai
from docx import Document

# Cấu hình API
genai.configure(api_key="YOUR_API_KEY_HERE")  # Thay YOUR_API_KEY_HERE bằng API key thật

model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="📑 ISO ChatBot với Gemini", layout="wide")
st.title("📑 Trợ lý truy vấn tài liệu ISO với Gemini")

# Tải file ISO
uploaded_file = st.file_uploader("📤 Tải tài liệu ISO (.docx)", type=["docx"])

if uploaded_file:
    # Đọc nội dung file Word
    doc = Document(uploaded_file)
    full_text = "\n".join([para.text for para in doc.paragraphs])

    # Hiển thị tùy chọn
    st.subheader("💬 Nhập câu hỏi về tài liệu:")
    user_input = st.text_area("Câu hỏi", placeholder="Ví dụ: Mẫu phiếu kiểm tra chất lượng ở đâu?")

    if st.button("Gửi câu hỏi"):
        with st.spinner("Đang xử lý..."):
            prompt = f"""
Tài liệu ISO sau:\n\n{full_text[:15000]}\n\n
Người dùng hỏi:\n\"{user_input}\"\n\n
Hãy trả lời ngắn gọn, rõ ràng, trích đúng nội dung từ tài liệu nếu có.
"""
            response = model.generate_content(prompt)
            st.markdown("### 🧠 Trợ lý trả lời:")
            st.write(response.text)
