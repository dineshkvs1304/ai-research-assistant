import streamlit as st
import requests
import time

API_URL = "http://127.0.0.1:8000"

st.title("AI Research Assistant")

# =========================
# Upload Section
# =========================

st.subheader("Upload Research Paper")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:

    files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}

    with st.spinner("Uploading and indexing document..."):

        response = requests.post(
            f"{API_URL}/upload",
            files=files
        )

    if response.status_code == 200:
        st.success("Document uploaded successfully!")

# =========================
# Chat Section
# =========================

st.subheader("Ask Questions")

if "chat" not in st.session_state:
    st.session_state.chat = []

question = st.text_input("Ask a question about the research papers")

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        with st.spinner("Thinking..."):

            response = requests.post(
                f"{API_URL}/ask",
                json={"question": question}
            )

        data = response.json()

        answer = data.get("answer", "No answer returned.")
        sources = data.get("sources", [])

        st.session_state.chat.append(("user", question))

        st.session_state.chat.append((
            "ai",
            {
                "answer": answer,
                "sources": sources
            }
        ))

# =========================
# Chat Display
# =========================

for role, message in st.session_state.chat:

    if role == "user":

        st.write(f"**You:** {message}")

    else:

        st.write("**AI:**")

        placeholder = st.empty()

        typed = ""

        # Streaming typing effect
        for word in message["answer"].split():
            typed += word + " "
            placeholder.write(typed)
            time.sleep(0.05)

        # Show sources
        if message.get("sources"):

            st.write("Sources:")

            for s in message["sources"]:
                st.write("-", s)

# =========================
# Clear Chat
# =========================

if st.button("Clear Chat"):
    st.session_state.chat = []