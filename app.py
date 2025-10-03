import streamlit as st
import os
from QABot import OpenRouterQABot

# --- Streamlit App ---
st.set_page_config(page_title="Voucher & Orders QA Bot", page_icon="💬", layout="wide")

# --- Get API key from Streamlit secrets or environment variable ---
api_key = st.secrets.get("OPENROUTER_KEY") or os.environ.get("OPENROUTER_KEY")
if not api_key:
    st.error("API key not found! Please add OPENROUTER_KEY to secrets.toml or environment variable.")
    st.stop()

# Initialize bot
bot = OpenRouterQABot(
    faq_source="./faq/offerz_context.txt",
    api_key=api_key,
    site_url="https://example.com",
    site_name="MySite"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Layout with two columns ---
left_col, right_col = st.columns([1, 2])  # left narrow, right wider for chat

# Left column: Ticket Form
with left_col:
    st.subheader("Submit a Ticket")
    st.text_input("Order ID*", value="", key="order_id")
    ticket_type = st.selectbox("Ticket type*", ["Voucher does not work", "Order not received", "Other"])
    problem_desc = st.text_area("Describe the problem*", placeholder="Please describe the problem and be detailed.", key="problem")
    st.file_uploader("Add attachment", type=["png", "jpg", "pdf"])

    if st.button("SUBMIT TICKET"):
        if problem_desc.strip():
            user_question = f"Ticket type: {ticket_type}\nProblem: {problem_desc}"
            st.session_state.messages.append({"role": "user", "content": user_question})

            with st.spinner("Bot is thinking..."):
                answer = bot.answer_question(st.session_state.messages)

            st.session_state.messages.append({"role": "bot", "content": answer})
        else:
            st.warning("Please describe the problem before submitting.")

# Right column: Chat interface
with right_col:
    st.subheader("Chat with Voucher & Orders QA Bot")

    if not st.session_state.messages:
        st.info("No messages yet. Submit a ticket to start the conversation.")

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**🧑 You:** {msg['content']}")
        else:
            st.markdown(f"**🤖 Bot:** {msg['content']}")