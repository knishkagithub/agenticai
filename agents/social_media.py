
# # # # import os
# # # # import requests
# # # # from bs4 import BeautifulSoup
# # # # import google.generativeai as genai
# # # # from dotenv import load_dotenv

# # # # # Load API Key
# # # # load_dotenv()
# # # # GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # # # if not GOOGLE_API_KEY:
# # # #     raise ValueError("❌ GOOGLE_API_KEY is missing. Please set it in .env")

# # # # genai.configure(api_key=GOOGLE_API_KEY)

# # # # # ✅ Function to scrape news or social media data
# # # # def scrape_news(url):
# # # #     """Scrapes text content from a given news or social media URL."""
# # # #     try:
# # # #         response = requests.get(url, timeout=10)
# # # #         if response.status_code != 200:
# # # #             return f"❌ Error: Unable to fetch data from {url}. Status code: {response.status_code}"
        
# # # #         soup = BeautifulSoup(response.text, 'html.parser')
# # # #         return soup.get_text()

# # # #     except Exception as e:
# # # #         print(f"❌ ERROR in scrape_news: {str(e)}")
# # # #         return f"❌ Internal Error: {str(e)}"

# # # # # ✅ Function to analyze sentiment & borrower behavior
# # # # def analyze_social_media(url):
# # # #     """Analyzes sentiment & predicts borrower behavior based on news/social media mentions."""
    
# # # #     # Scrape content from the given URL
# # # #     news_text = scrape_news(url)

# # # #     if "❌" in news_text:
# # # #         return news_text  # Return error if scraping failed

# # # #     # Construct AI prompt
# # # #     prompt = f"""
# # # #     You are an AI financial analyst. Analyze the following news article/social media content and predict:
# # # #     - Sentiment (Positive, Neutral, Negative)
# # # #     - Borrower financial stability and behavior
# # # #     - Any red flags related to fraud or risky transactions

# # # #     News Content:
# # # #     {news_text}

# # # #     Provide a summary of your findings.
# # # #     """

# # # #     try:
# # # #         # Generate AI response using Gemini 1.5 Flash
# # # #         llm = genai.GenerativeModel("gemini-1.5-flash")
# # # #         response = llm.generate_content(prompt)

# # # #         return response.text if response else "❌ Error: No response from Gemini AI."

# # # #     except Exception as e:
# # # #         print(f"❌ ERROR in analyze_social_media: {str(e)}")
# # # #         return f"❌ Internal Error: {str(e)}"
# # # import os
# # # import requests
# # # from bs4 import BeautifulSoup
# # # import google.generativeai as genai
# # # from dotenv import load_dotenv

# # # # ✅ Load API Key
# # # load_dotenv()
# # # GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # # if not GOOGLE_API_KEY:
# # #     raise ValueError("❌ GOOGLE_API_KEY is missing. Please set it in .env")

# # # genai.configure(api_key=GOOGLE_API_KEY)

# # # # ✅ Function to scrape news or social media data
# # # def scrape_news(url):
# # #     """Scrapes text content from a given news or social media URL."""
# # #     try:
# # #         response = requests.get(url, timeout=10)

# # #         # ✅ Check if response is successful
# # #         if response.status_code != 200:
# # #             return f"❌ Error: Unable to fetch data from {url}. Status code: {response.status_code}"
        
# # #         soup = BeautifulSoup(response.text, 'html.parser')
# # #         return soup.get_text()

# # #     except requests.exceptions.RequestException as e:
# # #         print(f"❌ ERROR in scrape_news: {str(e)}")
# # #         return f"❌ Internal Error: Unable to scrape data. {str(e)}"

# # # # ✅ Function to analyze sentiment & borrower behavior
# # # def analyze_social_media(url):
# # #     """Analyzes sentiment & predicts borrower behavior based on news/social media mentions."""
    
# # #     news_text = scrape_news(url)

# # #     if "❌" in news_text:
# # #         return news_text  # Return error if scraping failed

# # #     prompt = f"""
# # #     You are an AI financial analyst. Analyze the following news article/social media content and predict:
# # #     - Sentiment (Positive, Neutral, Negative)
# # #     - Borrower financial stability and behavior
# # #     - Any red flags related to fraud or risky transactions

# # #     News Content:
# # #     {news_text}

# # #     Provide a summary of your findings.
# # #     """

# # #     try:
# # #         # ✅ Ensure AI Model is initialized
# # #         llm = genai.GenerativeModel("gemini-1.5-flash")
# # #         response = llm.generate_content(prompt)

# # #         # ✅ Fix: Ensure response is valid
# # #         if response and hasattr(response, 'text'):
# # #             return response.text
# # #         else:
# # #             return "❌ Error: No valid response from Gemini AI."

# # #     except Exception as e:
# # #         print(f"❌ ERROR in analyze_social_media: {str(e)}")
# # #         return f"❌ Internal Error: {str(e)}"
# # import googleapiclient.discovery
# # import google.generativeai as genai
# # from dotenv import load_dotenv
# # import os

# # # ✅ Load API Key
# # load_dotenv()
# # GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# # GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")  # ✅ Add Google Search API Key
# # SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")  # ✅ Add Custom Search Engine ID

# # if not GOOGLE_API_KEY:
# #     raise ValueError("❌ GOOGLE_API_KEY is missing. Please set it in .env")
# # if not GOOGLE_SEARCH_API_KEY or not SEARCH_ENGINE_ID:
# #     raise ValueError("❌ Google Search API Key or Search Engine ID is missing. Please set them in .env")

# # genai.configure(api_key=GOOGLE_API_KEY)

# # # ✅ Function to Fetch Financial News Links Using Google Search API
# # def search_google_news(query):
# #     """Fetches top financial news articles for a given query using Google Search API."""

# #     try:
# #         service = googleapiclient.discovery.build("customsearch", "v1", developerKey=GOOGLE_SEARCH_API_KEY)
# #         res = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=5).execute()

# #         # ✅ Extract news links
# #         news_links = [item["link"] for item in res.get("items", [])]
# #         return news_links if news_links else ["❌ No news articles found. Try refining your search query."]
    
# #     except Exception as e:
# #         return [f"❌ Error fetching news: {str(e)}"]

# # # ✅ Function to Analyze Social Media & News Sentiment Using Gemini AI
# # def analyze_social_media(query):
# #     """Uses Google Search API to fetch news articles & Gemini AI to analyze sentiment."""

# #     # ✅ Get top news articles
# #     news_links = search_google_news(query)
    
# #     # ✅ Construct AI prompt
# #     prompt = f"""
# #     You are an AI financial analyst. Analyze sentiment & predict financial stability based on recent news:

# #     🔍 **News Sources:**
# #     {news_links}

# #     Query: {query}

# #     Provide insights on:
# #     - **Overall Sentiment** (Positive, Neutral, or Negative)
# #     - **Financial Stability of the Individual/Business**
# #     - **Potential Fraud Risks or Red Flags**
# #     - **Predicted Impact on Creditworthiness**
# #     """

# #     try:
# #         llm = genai.GenerativeModel("gemini-1.5-flash")
# #         response = llm.generate_content(prompt)

# #         return response.text if response else "❌ Error: No valid response from Gemini AI."

# #     except Exception as e:
# #         return f"❌ Internal Error: {str(e)}"
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# # ✅ Load API Key
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# if not GOOGLE_API_KEY:
#     raise ValueError("❌ GOOGLE_API_KEY is missing. Please set it in .env")

# genai.configure(api_key=GOOGLE_API_KEY)

# # ✅ Function to Analyze Social Media & News Sentiment Using Gemini AI
# def analyze_social_media(query):
#     """Uses Gemini 1.5 Flash to analyze financial sentiment without external data scraping."""
    
#     # ✅ AI Prompt for Sentiment Analysis
#     prompt = f"""
#     You are an AI financial analyst with access to the latest economic trends and borrower behaviors.

#     Analyze the following query related to financial sentiment and borrower stability:

#     Query: {query}

#     Provide insights on:
#     - **Overall Sentiment** (Positive, Neutral, or Negative)
#     - **Financial Stability of the Individual/Business**
#     - **Potential Fraud Risks or Red Flags**
#     - **Predicted Impact on Creditworthiness**
#     - **Industry Trends or Past Events That Might Be Relevant**
#     """

#     try:
#         # ✅ Call Gemini AI for Analysis
#         llm = genai.GenerativeModel("gemini-1.5-flash")
#         response = llm.generate_content(prompt)

#         return response.text if response else "❌ Error: No valid response from Gemini AI."

#     except Exception as e:
#         return f"❌ Internal Error: {str(e)}"
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ✅ Load API Key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY is missing. Please set it in .env")

genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Function to Analyze Social Media & News Sentiment Using Gemini AI
def analyze_social_media(query):
    """Uses Gemini 1.5 Flash to analyze financial sentiment with a structured approach."""
    
    # ✅ AI Prompt for Detailed Sentiment Analysis
    prompt = f"""
    You are an AI financial analyst specializing in sentiment analysis and borrower risk assessment.

    Task:
    - Analyze the **public perception** of the given person or business in the finance industry.
    - Consider **historical market trends, investor opinions, and financial news**.
    - Predict potential risks based on **past similar financial cases**.

    Query: {query}

    🚀 **Your response should include:**
    1️⃣ **Overall Sentiment** (Positive, Neutral, or Negative)  
    2️⃣ **Financial Reputation Score** (1-10 scale, where 10 = highly reputable, 1 = high risk)  
    3️⃣ **Potential Red Flags** (List specific fraud, default, or investment risks)  
    4️⃣ **Likely Investor Confidence** (Is the person/business trustworthy for lending or investment?)  
    5️⃣ **Historical Comparisons** (If relevant, compare with past financial figures)  

    📌 **Example Response Format:**
    - **Sentiment:** Negative 🚨  
    - **Reputation Score:** 3/10 🔴  
    - **Potential Red Flags:** History of missed loan payments, SEC investigation in 2023.  
    - **Investor Confidence:** Low due to multiple bankruptcy filings.  
    - **Comparison:** Similar to the Enron collapse in early 2000s.  

    🔹 Ensure your response is direct, structured, and avoids generic disclaimers.  
    """

    try:
        # ✅ Call Gemini AI for Analysis
        llm = genai.GenerativeModel("gemini-1.5-flash")
        response = llm.generate_content(prompt)

        return response.text if response else "❌ Error: No valid response from Gemini AI."

    except Exception as e:
        return f"❌ Internal Error: {str(e)}"
