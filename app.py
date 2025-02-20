
# from flask import Flask, request, jsonify
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Import AI Agents
# from agents.creditworthiness import assess_creditworthiness
# from agents.kyc_verification import verify_kyc
# from agents.social_media import analyze_social_media
# from agents.esg_tracking import evaluate_esg

# app = Flask(__name__)

# # ✅ Load API Key
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# if not GOOGLE_API_KEY:
#     raise ValueError("❌ GOOGLE_API_KEY is missing. Please set it in .env")

# genai.configure(api_key=GOOGLE_API_KEY)

# # ✅ Flask API Endpoint
# @app.route('/ask', methods=['POST'])
# def ask_bot():
#     data = request.json
#     query = data.get("query", "")

#     if not query:
#         return jsonify({"error": "No query provided"}), 400

#     try:
#         # ✅ Route query to the right AI agent
#         if "creditworthiness" in query.lower():
#             response = assess_creditworthiness(query)
#         elif "kyc" in query.lower():
#             response = verify_kyc("kyc_document.pdf")  # Ensure the file exists
#         elif "social media" in query.lower() or "news" in query.lower():
#             response = analyze_social_media("https://www.financialexpress.com/")  # Replace with actual URL
#         elif "esg" in query.lower():
#             response = evaluate_esg(query)
#         else:
#             response = "Invalid query. Please specify a valid AI task."

#         return jsonify({"response": response})

#     except Exception as e:
#         print(f"❌ ERROR: {str(e)}")  # Logs error in terminal
#         return jsonify({"error": str(e)}), 500  # Returns actual error message

# # ✅ Run Flask Server
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
from flask import Flask, request, jsonify
import os
import re  # For better query matching
from dotenv import load_dotenv
import google.generativeai as genai

# Import AI Agents
from agents.creditworthiness import assess_creditworthiness
from agents.kyc_verification import verify_kyc
from agents.social_media import analyze_social_media
from agents.esg_tracking import evaluate_esg

app = Flask(__name__)

# ✅ Load API Key at startup
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY is missing. Please set it in .env")

genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Flask API Endpoint
@app.route('/ask', methods=['POST'])
def ask_bot():
    data = request.json
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        # ✅ Smart Query Routing (Improved)
        if re.search(r"\bcredit\b|\bloan\b|\brisk\b", query, re.IGNORECASE):
            response = assess_creditworthiness(query)
        elif re.search(r"\bkyc\b|\bverification\b|\bid\b", query, re.IGNORECASE):
            # Accepts a KYC file if provided
            kyc_file = data.get("file", "kyc_document.pdf")  # Defaults to 'kyc_document.pdf'
            response = verify_kyc(kyc_file)
        # elif re.search(r"\bsocial\b|\bnews\b|\bmedia\b|\bsentiment\b", query, re.IGNORECASE):
        #     # ✅ Use a real financial news site instead of a placeholder
        #     response = analyze_social_media("https://finance.yahoo.com/news")
        elif "social media" in query.lower() or "news" in query.lower():
            response = analyze_social_media(query)  # ✅ Now uses Gemini 1.5 Flash directly
        elif re.search(r"\besg\b|\bsustainability\b|\bgreen\b", query, re.IGNORECASE):
            response = evaluate_esg(query)
        else:
            response = "❌ Invalid query. Please specify a valid AI task."

        return jsonify({"response": response})

    except Exception as e:
        print(f"❌ ERROR: {str(e)}")  # Logs error in terminal
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500  # Returns actual error message

# ✅ Run Flask Server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
