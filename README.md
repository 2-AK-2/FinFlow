# FinFlow

## Overview
This project is an AI-powered loan assistance system that provides eligibility checks, application guidance, and financial tips using NLP, intent recognition, and API integrations. It supports multilingual inputs, speech-to-text, and text-to-speech functionalities.

## Features
### Loan Eligibility & Guidance
- Determines eligibility and provides loan application insights.

### Multilingual NLP
- Processes inputs in multiple languages via mBERT and Google Translate API.

### Intent Recognition
- Classifies queries using BERT and Dialogflow CX.

### Named Entity Recognition (NER)
- Extracts key financial details like salary and credit score.

### Sentiment Analysis
- Understands user emotions using VADER and FinBERT.

### Dynamic API Routing
- Uses LangChain Agents to determine and call the correct APIs.

### Speech & Text Processing
- **Whisper (STT)** for speech-to-text conversion.
- **Google TTS / Amazon Polly** for text-to-speech.

## Tech Stack
### Backend
- **Node.js (Express.js) / Python (FastAPI):** Handles API requests and business logic.
- **PostgreSQL / Firebase Firestore:** Stores user interactions and loan details.

### NLP Models & AI Services
- **BERT / Dialogflow CX:** Intent classification and multilingual understanding.
- **spaCy / FinBERT:** Named entity recognition.
- **VADER / FinBERT:** Sentiment analysis.
- **LangChain Agents:** API routing and function calling.
- **LlamaIndex:** Fetches financial data from structured/unstructured sources.
- **OpenAI GPT-4:** Response generation and conversational AI.

### Frontend & Communication
- **Flutter:** For building the mobile/web application.
- **Google Cloud Translation API:** For multilingual support.
- **WhatsApp API:** Allows user interaction via chat.

## Workflow
1. **User Input:** Voice (**Whisper STT**) or text (**Flutter app, WhatsApp API**).
2. **Processing:**
   - If required, translates text via **Google Cloud Translate API**.
   - **BERT/Dialogflow CX** classifies intent.
   - **Named entity recognition** extracts key details.
3. **API Calls & Decision Making:**
   - **LangChain** determines the appropriate API.
   - Calls **Loan Eligibility API** if necessary.
4. **Response Generation:**
   - **GPT-4** formulates a response.
   - **Sentiment analysis (VADER/FinBERT)** refines the output.
   - **Google TTS / Amazon Polly** provides voice responses if needed.
5. **Delivery:** The response is sent back via text or speech.

## Why Choose This Solution?
- **AI-Driven & Scalable:** Uses cutting-edge NLP and ML models.
- **Multilingual Support:** Enables interaction in 50+ languages.
- **Seamless API Integration:** Efficient loan guidance and financial advice.
- **User-Friendly:** Supports text, voice, and multiple platforms.

## Future Enhancements
- **Integration with Banking APIs** for real-time loan offers.
- **Enhanced Personalization** using user history and preferences.
- **Blockchain-based Security** for financial data privacy.

## Team Name
**FinFlow**

##Team Members
**Akshaya Krishna**
**Khushi Mahesh**
**Kunjal Patwari**
**Samarth M**

