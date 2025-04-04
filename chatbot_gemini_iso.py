import streamlit as st
import google.generativeai as genai
from docx import Document

# 🔐 Cấu hình Gemini API từ secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

# 🚀 Cài đặt giao diện
st.set_page_config(page_title="📑 ISO ChatBot với Gemini", layout="wide")
st.title("📑 Trợ lý truy vấn tài liệu ISO với Gemini")

# 📂 Upload file .docx
uploaded_file = st.file_uploader("📤 Tải tài liệu ISO (.docx)", type=["docx"])

if not uploaded_file:
    st.warning("📂 Vui lòng tải lên tài liệu ISO để bắt đầu.")
else:
    try:
        # 🧾 Đọc file .docx
        doc = Document(uploaded_file)
        full_text = "\n".join([para.text for para in doc.paragraphs if para.text.strip() != ""])

        # 📝 Nhập câu hỏi
        st.subheader("💬 Nhập câu hỏi về tài liệu:")
        user_input = st.text_area("Câu hỏi", placeholder="Ví dụ: Trách nhiệm kiểm tra chất lượng thuộc về ai?", height=100)

        # 🔍 Gửi truy vấn
        if st.button("Gửi câu hỏi") and user_input.strip():
            with st.spinner("🔎 Đang truy vấn Gemini..."):
                prompt = f"""
Bạn là trợ lý ISO. Hãy dựa vào tài liệu dưới đây để trả lời câu hỏi.

==== TÀI LIỆU ====
{full_text[:15000]}

==== CÂU HỎI ====
{user_input}

Trả lời ngắn gọn, dễ hiểu, và chính xác.
"""
                response = model.generate_content(prompt)
                st.markdown("### 🧠 Trợ lý trả lời:")
                st.write(response.text)
        elif st.button("Gửi câu hỏi") and not user_input.strip():
            st.warning("❗ Vui lòng nhập câu hỏi trước khi gửi.")
    except Exception as e:
        st.error(f"⚠️ Lỗi khi đọc tài liệu: {e}")
