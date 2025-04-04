import streamlit as st
import pandas as pd
from openai import OpenAI

# Kết nối GPT từ secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Giao diện
st.title("📄 Chatbot ISO – TALOPACK")
query = st.text_input("Hỏi tôi về tài liệu ISO bạn cần:")

# Đọc file CSV đã chuẩn hóa
try:
    df = pd.read_csv("iso_data.csv")
except:
    st.error("Không tìm thấy file iso_data.csv. Vui lòng kiểm tra lại.")
    st.stop()

# Khi người dùng nhập câu hỏi
if query:
    # Chuẩn bị ngữ cảnh dữ liệu
    context = "\n".join([f"{row['Tên']} ({row['Loại']}): {row['Tóm tắt']}" for _, row in df.iterrows()])
    
    # Prompt cho GPT
    prompt = f"""
Bạn là trợ lý ISO trong công ty. Đây là danh sách tài liệu:

{context}

Người dùng hỏi: '{query}'. 
Hãy gợi ý tài liệu liên quan và nếu có thể, đưa tên tài liệu + loại + tóm tắt + đường dẫn truy cập.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Bạn là trợ lý ISO thông minh của công ty TALOPACK."},
                {"role": "user", "content": prompt}
            ]
        )

        st.markdown("### 🧾 Kết quả:")
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Lỗi gọi GPT API: {e}")
