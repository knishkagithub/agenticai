
# # import os
# # import google.generativeai as genai
# # from langchain.document_loaders import PyPDFLoader
# # from dotenv import load_dotenv

# # # Load API key
# # load_dotenv()
# # GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# # genai.configure(api_key=GOOGLE_API_KEY)
# # llm = genai.GenerativeModel("gemini-1.5-flash")
# # # ✅ Define function for KYC Verification
# # def verify_kyc(document_path: str):
# #     """Verifies KYC document authenticity and detects AML risks using Gemini 1.5 Flash."""

# #     # Load KYC document
# #     loader = PyPDFLoader(document_path)
# #     docs = loader.load()

# #     # ✅ Construct AI prompt
# #     prompt = f"""
# #     You are an AI compliance officer. Analyze the following KYC document and check for:
# #     - Authenticity
# #     - Anti-Money Laundering (AML) risks
# #     - Possible fraud indicators

# #     Document content:
# #     {docs[0].page_content}

# #     Provide a decision on whether this document should be approved, flagged, or rejected.
# #     """

# #     # ✅ Generate AI response using Gemini 1.5 Flash
# #     llm = genai.GenerativeModel("gemini-1.5-flash")
# #     response = llm.generate_content(prompt)

# #     return response.text  # Returns AI-generated KYC decision
# import os
# import google.generativeai as genai
# from langchain_community.document_loaders import PyPDFLoader  # Fixed Import
# from dotenv import load_dotenv

# # Load API Key
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# if not GOOGLE_API_KEY:
#     raise ValueError("❌ GOOGLE_API_KEY is missing. Please set it in .env")

# genai.configure(api_key=GOOGLE_API_KEY)

# def verify_kyc(document_path: str):
#     """Verifies KYC document authenticity using Gemini 1.5 Flash."""

#     try:
#         # Check if document exists
#         if not os.path.exists(document_path):
#             return "❌ Error: KYC document not found."

#         # Load KYC document
#         loader = PyPDFLoader(document_path)
#         docs = loader.load()

#         if not docs:
#             return "❌ Error: KYC document is empty."

#         # Construct AI prompt
#         prompt = f"""
#         You are an AI compliance officer. Analyze the following KYC document and check for:
#         - Authenticity
#         - Anti-Money Laundering (AML) risks
#         - Possible fraud indicators

#         Document content:
#         {docs[0].page_content}

#         Provide a decision on whether this document should be approved, flagged, or rejected.
#         """

#         # Generate AI response using Gemini 1.5 Flash
#         llm = genai.GenerativeModel("gemini-1.5-flash")
#         response = llm.generate_content(prompt)

#         return response.text if response else "❌ Error: No response from Gemini AI."

#     except Exception as e:
#         print(f"❌ ERROR in verify_kyc: {str(e)}")  # Logs error in terminal
#         return f"❌ Internal Error: {str(e)}"
import os
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from dotenv import load_dotenv

# ✅ Load API Key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY is missing. Please set it in .env")

genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Initialize FAISS Vector Store (Replaces manual document loading)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# ✅ Updated KYC Data in John & Jane Format
kyc_data = [
    "John Doe: Verified identity, Passport ID: X1234567, No history of fraud, AML risk: Low",
    "Jane Smith: Verified identity, Driver’s License: S9876543, Minor discrepancies in address, AML risk: Medium",
    "Michael Brown: Passport ID: M5678901, Inconsistencies in financial records, AML risk: High",
    "Emily Davis: Verified KYC, National ID: E6543219, No red flags, AML risk: Low",
    "David Wilson: Unverified identity, Expired documents, Incomplete financial disclosures, AML risk: High"
]

# ✅ Store KYC data in FAISS for retrieval
vector_db = FAISS.from_texts(kyc_data, embeddings)

# ✅ Function to Verify KYC using FAISS + Gemini AI
def verify_kyc(query):
    """Verifies KYC details by retrieving stored identity records and analyzing fraud risks."""

    # ✅ Retrieve the most relevant KYC data from FAISS
    similar_kyc_records = vector_db.similarity_search(query, k=3)

    prompt = f"""
    You are an AI compliance officer analyzing KYC (Know Your Customer) verification details.
    
    Query: {query}

    🔍 **Retrieved KYC Data from Vector Database:**
    {similar_kyc_records}

    Analyze the following:
    - **Identity Verification** (Valid, Discrepancies, or Unverified)
    - **Fraud Indicators** (Red flags, fake documents, inconsistencies)
    - **AML Risk Level** (High, Medium, or Low)
    - **Final Decision** (Approve, Flag, or Reject)

    Provide a clear summary with a final decision.
    """

    try:
        # ✅ Ensure AI Model is initialized
        llm = genai.GenerativeModel("gemini-1.5-flash")
        response = llm.generate_content(prompt)

        # ✅ Fix: Ensure response is valid
        if response and hasattr(response, 'text'):
            return response.text
        else:
            return "❌ Error: No valid response from Gemini AI."

    except Exception as e:
        print(f"❌ ERROR in verify_kyc: {str(e)}")  # Logs error in terminal
        return f"❌ Internal Error: {str(e)}"
