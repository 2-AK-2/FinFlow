import requests

url = "http://127.0.0.1:8000/analyze-text/"
data = {"text": "I love learning about AI and machine learning!"}

response = requests.post(url, json=data)
print(response.json())  # Should return BERT sentiment analysis
