import requests
import uuid
import streamlit as st

st.set_page_config(page_title="📄 Chatbot", layout="centered")
st.title("Resume Chatbot")
st.markdown("Have a conversation with my AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
#
# user = st.chat_input("Ask me anything")
# if user:
#     st.session_state.messages.append({
#         "role": "user",
#         "content": user
#     })
#     with st.chat_message("user"):
#         st.write(user)
#     with st.spinner("Thinking..."):
#         response = requests.post(
#             url="http://127.0.0.1:8000/chat",
#             json={
#                 "session_id": st.session_state.session_id,
#                 "question": user
#             }
#         )
#
#         st.session_state.messages.append({
#             "role": "assistant",
#             "content": response.json().get("answer")
#         })
#         with st.chat_message("assistant"):
#             st.write(response.json().get("answer"))
#     # st.rerun()


def stream_answer(question):
    with requests.post(
        url="http://127.0.0.1:8000/chat/stream",
        json={
            "session_id": str(uuid.uuid4()),
            "question": question
        },
        stream=True,
        timeout=60
    ) as response:
        response.raise_for_status()
        response.encoding = "utf-8"
        for piece in response.iter_content(chunk_size=None, decode_unicode=True):
            if piece:
                yield piece

user = st.chat_input("Ask me anything")
if user:
    st.session_state.messages.append({
        "role": "user",
        'content': user
    })
    with st.chat_message("user"):
        st.write(user)

    with st.chat_message("assistant"):
        answer = st.write_stream(stream_answer(user))
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
