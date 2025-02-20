# # from langchain.chains import RetrievalQA
# # from langchain.embeddings import OpenAIEmbeddings
# # from langchain.vectorstores import FAISS
# # from langchain.llms import OpenAI

# # # Sample Borrower Data
# # borrower_data = [
# #     "John Doe, Income: $50,000, Past Loans: 2, Defaults: 0, Business Revenue: $200,000",
# #     "Jane Smith, Income: $40,000, Past Loans: 3, Defaults: 1, Business Revenue: $100,000"
# # ]

# # # Create vector store
# # embeddings = OpenAIEmbeddings()
# # vector_db = FAISS.from_texts(borrower_data, embeddings)

# # # Define the agent
# # qa = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=vector_db.as_retriever())

# # # Query the agent
# # query = "What is the creditworthiness of John Doe?"
# # response = qa.run(query)
# # print(response)
# from langchain.chains import RetrievalQA
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.llms import OpenAI

# # Sample Borrower Data
# borrower_data = [
#     "John Doe, Income: $50,000, Past Loans: 2, Defaults: 0, Business Revenue: $200,000",
#     "Jane Smith, Income: $40,000, Past Loans: 3, Defaults: 1, Business Revenue: $100,000"
# ]

# # Create vector store
# embeddings = OpenAIEmbeddings()
# vector_db = FAISS.from_texts(borrower_data, embeddings)

# # Define the AI Agent
# qa = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=vector_db.as_retriever())

# # ✅ Define this function properly!
# def assess_creditworthiness(query: str):
#     """Assess the creditworthiness of a borrower based on data."""
#     return qa.run(query)
# import os
# from langchain_google_genai import GoogleGenerativeAI
# from langchain.vectorstores import FAISS
# from langchain.embeddings import OpenAIEmbeddings  # Optional, can replace with Gemini embeddings
# from langchain.chains import RetrievalQA
# from dotenv import load_dotenv

# # Load API key
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Initialize Gemini Model
# llm = GoogleGenerativeAI(model="gemini-pro", api_key=GOOGLE_API_KEY)

# # Sample Borrower Data
# borrower_data = [
#     "John Doe, Income: $50,000, Past Loans: 2, Defaults: 0, Business Revenue: $200,000",
#     "Jane Smith, Income: $40,000, Past Loans: 3, Defaults: 1, Business Revenue: $100,000"
# ]

# # Create FAISS vector store (Optional)
# embeddings = OpenAIEmbeddings()
# vector_db = FAISS.from_texts(borrower_data, embeddings)

# # Define AI Agent
# qa = RetrievalQA.from_chain_type(llm=llm, retriever=vector_db.as_retriever())

# # ✅ Define function
# def assess_creditworthiness(query: str):
#     """Assess the creditworthiness of a borrower using Gemini AI."""
#     return qa.run(query)
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini 1.5 Flash
genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Initialize Gemini 1.5 Flash Model
llm = genai.GenerativeModel("gemini-1.5-flash")

# Sample Borrower Data (You can extend this using a database)
borrower_data = {
    "John Doe": {"Income": "$50,000", "Past Loans": 2, "Defaults": 0, "Business Revenue": "$200,000"},
    "Jane Smith": {"Income": "$40,000", "Past Loans": 3, "Defaults": 1, "Business Revenue": "$100,000"}
}

# ✅ Define function for creditworthiness check
def assess_creditworthiness(query: str):
    """Assess the creditworthiness of a borrower using Gemini 1.5 Flash."""
    
    # Extract borrower name from query
    borrower_name = None
    for name in borrower_data.keys():
        if name.lower() in query.lower():
            borrower_name = name
            break

    if not borrower_name:
        return "Borrower not found in database."

    # Generate AI response
    borrower_info = borrower_data[borrower_name]
    prompt = f"""
    Evaluate the creditworthiness of {borrower_name}.
    - Income: {borrower_info['Income']}
    - Past Loans: {borrower_info['Past Loans']}
    - Defaults: {borrower_info['Defaults']}
    - Business Revenue: {borrower_info['Business Revenue']}
    
    Based on financial risk factors, is {borrower_name} eligible for a loan? Provide a recommendation.
    """

    response = llm.generate_content(prompt)
    
    return response.text
