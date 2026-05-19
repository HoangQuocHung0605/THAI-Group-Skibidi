import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# URL dùng v1 (Stable) - Endpoint chuẩn nhất 2026
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"

payload = {"contents": [{"parts": [{"text": "Hello, respond with 'OK' if you see this."}]}]}

try:
    print(f"[*] Đang test Key mới: {api_key[:10]}...")
    res = requests.post(url, json=payload)
    if res.status_code == 200:
        print("✅ CHÚC MỪNG! Key mới hoạt động hoàn hảo.")
        print("AI trả lời:", res.json()['candidates'][0]['content']['parts'][0]['text'])
    else:
        print(f"❌ Vẫn lỗi {res.status_code}: {res.json()}")
except Exception as e:
    print(f"❌ Lỗi kết nối: {e}")