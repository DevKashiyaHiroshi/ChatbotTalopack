import streamlit as st
import pandas as pd
import openai

# Cấu hình
openai.api_key = st.secrets["Osk-proj-LQU3kq08ShszoTEPpuWhx6NhJqwrOhW9qBTzvuiUGOA_4O8msAAgUxiz9Ww6U3oG0wL6sflXgcT3BlbkFJg_4wYT_DHnCNr-Rl6BlbnDQtNUUSzkBhPqMoDMVWSF9hrqpDmBfj3VlFODcdCXOpgvZehj-eUA"]

st.title("📄 Chatbot Tài liệu ISO - TALOPACK")
query = st.text_input("Hỏi tôi về tài liệu ISO bạn cần:")

df = pd.read_csv("iso_data.csv")

if query:
    context = "\n".join([f"{row['Tên']}: {row['Tóm tắt']}" for _, row in df.iterrows()])
    prompt = f"""Tài liệu ISO hiện có:
    {context}

    Hãy trả lời câu hỏi: '{query}' bằng cách gợi ý tài liệu phù hợp và đường link nếu có."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    st.markdown("### ✅ Gợi ý:")
    st.write(response.choices[0].message.content)
