# # from langchain.chains import RetrievalQA

# # # ESG Data
# # esg_data = [
# #     "Company X: Carbon reduction 30%, Employee satisfaction high, Governance strong",
# #     "Company Y: Carbon reduction 10%, Employee satisfaction low, Governance weak"
# # ]

# # # Vector DB for ESG
# # vector_db = FAISS.from_texts(esg_data, embeddings)

# # # ESG AI Agent
# # esg_qa = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=vector_db.as_retriever())

# # # Query ESG performance
# # query = "Evaluate the ESG compliance of Company X"
# # response = esg_qa.run(query)
# # print(response)
# import os
# import google.generativeai as genai
# from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import OpenAIEmbeddings  # Replace with Gemini embeddings if needed
# from langchain.chains import RetrievalQA
# from langchain.docstore.document import Document
# from dotenv import load_dotenv

# # ✅ Load API Key
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# if not GOOGLE_API_KEY:
#     raise ValueError("❌ GOOGLE_API_KEY is missing. Please set it in .env")

# genai.configure(api_key=GOOGLE_API_KEY)

# # ✅ Initialize FAISS Vector Store (to store ESG data)
# embeddings = OpenAIEmbeddings()
# esg_data = [
#     "Company X: Carbon reduction 30%, Employee satisfaction high, Governance strong",
#     "Company Y: Carbon reduction 10%, Employee satisfaction low, Governance weak",
#     "Company Z: Renewable energy usage 50%, Employee benefits provided, Ethical leadership"
# ]

# vector_db = FAISS.from_texts(esg_data, embeddings)

# # ✅ Function to evaluate ESG factors
# def evaluate_esg(query):
#     """Analyzes a company's ESG compliance and sustainability risks using a vector database + Gemini 1.5 Flash."""

#     # Retrieve relevant ESG data
#     similar_esg_data = vector_db.similarity_search(query, k=3)

#     prompt = f"""
#     You are an ESG compliance expert. Evaluate the company's sustainability and governance performance.
    
#     Query: {query}
    
#     Relevant ESG Data:
#     {similar_esg_data}

#     Provide a summary including:
#     - Environmental performance (carbon emissions, energy use, sustainability)
#     - Social impact (workplace conditions, employee satisfaction, community engagement)
#     - Governance (transparency, ethical leadership, regulatory compliance)

#     Final ESG compliance rating (High, Medium, or Low).
#     """

#     try:
#         # ✅ Ensure AI Model is initialized
#         llm = genai.GenerativeModel("gemini-1.5-flash")
#         response = llm.generate_content(prompt)

#         # ✅ Fix: Ensure response is valid
#         if response and hasattr(response, 'text'):
#             return response.text
#         else:
#             return "❌ Error: No valid response from Gemini AI."

#     except Exception as e:
#         print(f"❌ ERROR in evaluate_esg: {str(e)}")
#         return f"❌ Internal Error: {str(e)}"
import os
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # ✅ Gemini Embeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
from dotenv import load_dotenv

# ✅ Load API Key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY is missing. Please set it in .env")

genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Initialize FAISS Vector Store with Gemini Embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  # ✅ Replaced OpenAI with Gemini
# esg_data = [
#     "Company X: Carbon reduction 30%, Employee satisfaction high, Governance strong",
#     "Company Y: Carbon reduction 10%, Employee satisfaction low, Governance weak",
#     "Company Z: Renewable energy usage 50%, Employee benefits provided, Ethical leadership"
# ]
esg_data = [
    "John Doe: Carbon footprint reduction 25%, Community service involvement high, Ethical investment portfolio strong",
    "Jane Smith: Carbon footprint reduction 15%, No community service involvement, Ethical investment portfolio weak",
    "Michael Brown: Uses 80% renewable energy, Active in environmental NGOs, Corporate governance advisor",
    "Emily Davis: Carbon footprint reduction 40%, Works for an ESG-certified company, No investment in fossil fuels",
    "David Wilson: No renewable energy usage, No sustainability initiatives, Limited ESG awareness"
]


vector_db = FAISS.from_texts(esg_data, embeddings)  # ✅ Store ESG data in FAISS

# ✅ Function to evaluate ESG factors
def evaluate_esg(query):
    """Analyzes a company's ESG compliance and sustainability risks using FAISS + Gemini 1.5 Flash."""

    # Retrieve relevant ESG data
    similar_esg_data = vector_db.similarity_search(query, k=3)

    prompt = f"""
    You are an ESG compliance expert. Evaluate the company's sustainability and governance performance.
    
    Query: {query}
    
    Relevant ESG Data:
    {similar_esg_data}

    Provide a summary including:
    - Environmental performance (carbon emissions, energy use, sustainability)
    - Social impact (workplace conditions, employee satisfaction, community engagement)
    - Governance (transparency, ethical leadership, regulatory compliance)

    Final ESG compliance rating (High, Medium, or Low).
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
        print(f"❌ ERROR in evaluate_esg: {str(e)}")
        return f"❌ Internal Error: {str(e)}"
