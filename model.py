import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def get_llm_response(prompt):
    system_prompt = (
        "You are a helpful virtual assistant. Answer the user's question clearly and concisely.\n"
        f"User: {prompt}\n"
        "Assistant:"
    )
    payload = {"inputs": system_prompt}
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        generated_text = data[0]["generated_text"]

        assistant_response = generated_text.split("Assistant:")[-1].strip()
        return assistant_response
    except Exception as e:
        print("LLM API Error:", e)
        print("Response:", response.text if 'response' in locals() else 'No response')
        return "Some error occurred, please try again!"
