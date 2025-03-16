# Finny - Your Loan Knowledge Assistant 🤖

## Overview

Finny is a smart, AI-powered chatbot designed to provide instant loan-related assistance. It combines a **dynamic knowledge base** with **real-time AI-generated responses** to help users get accurate information about loans, credit scores, interest rates, and more.

---

## Features

### 1. **Dynamic Knowledge Base (FAISS-powered Retrieval System)**
- Finny stores a **knowledge base** of predefined loan-related information using the **FAISS (Facebook AI Similarity Search) vector store**.
- **How it works:**
  - When a user asks a question, the system searches the **most relevant** answer from the knowledge base.
  - If an answer is found, it is **displayed instantly**.
  - If no answer is found, Finny **intelligently learns** the new query over time and expands its knowledge base.

### 2. **AI-Powered Chatbot (Google Gemini AI Integration)**
- If a user asks a question **not covered** in the knowledge base, Finny will generate a response using **Google Gemini AI**.
- **How it works:**
  - The chatbot sends the question to **Google Gemini AI**.
  - The AI generates an **accurate, context-aware response**.
  - This ensures Finny is **always up-to-date** with the latest information.

### 3. **Speech-to-Text (STT) & Text-to-Speech (TTS) with Sarvam API**
- Finny integrates **Sarvam AI's advanced STT and TTS APIs** to provide speech-based interaction.
- **Sarvam AI is a leader in voice AI technology**, offering **highly accurate** speech recognition and natural-sounding text-to-speech conversion.
- **How it works:**
  - Users can upload voice recordings, which are transcribed into text using **Sarvam AI’s STT API**.
  - Finny processes the text, generates a response, and converts it back to speech using **Sarvam AI’s TTS API**.
  - This allows users to **communicate with Finny hands-free**.
- **Why Sarvam AI?**
  - Offers **multi-language support** for voice processing.
  - **High accuracy and speed** in transcription and synthesis.
  - Ensures a **seamless user experience** with natural-sounding AI-generated voice.

### 4. **Question Tracking & Automatic Learning**
- Finny keeps track of **frequently asked questions**.
- If a question is asked **5 or more times**, it is **automatically added** to the knowledge base.
- This helps Finny continuously **learn and improve** without manual updates.

### 5. **Real-time Chat UI with Streamlit**
- Finny provides a **smooth, interactive chat experience** using **Streamlit**.
- **How it works:**
  - The chatbot interface is built using **Streamlit chat components**.
  - Messages are displayed in **separate user and assistant chat bubbles**.
  - Users can type their questions and receive **instant responses**.

---

## Installation Guide

### **Prerequisites**
Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- Streamlit

### **Cloning the Repository**
Run the following commands to **clone** and **set up** the project:
```bash
git clone https://github.com/yourusername/finny-loan-assistant.git
