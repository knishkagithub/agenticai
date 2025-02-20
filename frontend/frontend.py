# import streamlit as st
# import requests

# # Flask API URL
# FLASK_API_URL = "http://localhost:5000/ask"

# # Streamlit UI
# st.title("💰 AI-Powered Microfinance Chatbot")

# st.sidebar.header("Select AI Task")
# option = st.sidebar.selectbox(
#     "Choose an AI Agent:",
#     ["Creditworthiness Assessment", "KYC Verification", "Social Media Analysis", "ESG Evaluation"]
# )

# st.sidebar.header("Input Data")
# user_input = st.sidebar.text_area("Enter your query or upload a document:")

# if st.sidebar.button("Submit"):
#     if not user_input:
#         st.warning("Please enter a query!")
#     else:
#         # Prepare request payload
#         payload = {"query": f"{option}: {user_input}"}

#         # Call Flask API
#         response = requests.post(FLASK_API_URL, json=payload)

#         if response.status_code == 200:
#             st.success("✅ AI Agent Response:")
#             st.write(response.json()["response"])
#         else:
#             st.error("❌ Error communicating with AI bot. Please try again.")

# # Display response
# st.sidebar.markdown("---")
# st.sidebar.info("This AI-powered chatbot analyzes microfinance risks, automates compliance, and evaluates ESG factors.")
# import streamlit as st

# st.title("💰 AI-Powered Microfinance Chatbot")

# st.sidebar.header("Select AI Task")
# option = st.sidebar.selectbox(
#     "Choose an AI Agent:",
#     ["Creditworthiness Assessment", "KYC Verification", "Social Media Analysis", "ESG Evaluation"]
# )

# st.sidebar.header("Input Data")
# user_input = st.sidebar.text_area("Enter your query:")

# if st.sidebar.button("Submit"):
#     st.success("Processing your request...")
#     st.write(f"Selected Task: {option}")
#     st.write(f"User Input: {user_input}")
import streamlit as st
import requests

# Flask API URL
FLASK_API_URL = "http://localhost:5000/ask"

# Streamlit UI
st.set_page_config(page_title="Microfinance Chatbot", page_icon="💰")

st.title("💰 AI-Powered Microfinance Chatbot")

# Sidebar for AI Task Selection
st.sidebar.header("Select AI Task")
option = st.sidebar.selectbox(
    "Choose an AI Agent:",
    ["Creditworthiness Assessment", "KYC Verification", "Social Media Analysis", "ESG Evaluation"]
)

st.sidebar.header("Input Data")
user_input = st.text_area("Enter your query or upload a document:")

if st.button("Submit"):
    if not user_input:
        st.warning("⚠️ Please enter a query!")
    else:
        with st.spinner("Processing... ⏳"):
            # Prepare request payload
            payload = {"query": f"{option}: {user_input}"}

            try:
                # Call Flask API
                response = requests.post(FLASK_API_URL, json=payload)

                if response.status_code == 200:
                    st.success("✅ AI Agent Response:")
                    st.write(response.json()["response"])
                else:
                    st.error(f"❌ Error: {response.status_code} - Unable to communicate with AI bot.")

            except requests.exceptions.ConnectionError:
                st.error("❌ Unable to connect to Flask API. Make sure it's running.")

# Display response
st.sidebar.markdown("---")
st.sidebar.info("🔍 This AI-powered chatbot analyzes microfinance risks, automates compliance, and evaluates ESG factors.")
