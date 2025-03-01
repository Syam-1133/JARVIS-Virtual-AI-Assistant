
# 🎙️ Jarvis Voice Assistant 🤖

## 📝 Description
Jarvis Voice Assistant is a Python-based virtual assistant that uses Google's Gemini API for natural language processing. It can understand voice commands, perform tasks, and respond in a conversational manner. This project is inspired by the idea of creating a personal assistant like Jarvis from Iron Man. 🚀

**Key Features**:
- 🎤 Voice input and output.
- 🤖 Integration with Google's Gemini API for AI-powered responses.
- 🔔 Customizable wake word (e.g., "Jarvis").

## ✨ Features
- **🎤 Voice Recognition**: Uses `speech_recognition` to capture voice input.
- **🗣️ Text-to-Speech**: Uses `pyttsx3` to convert text responses into speech.
- **🧠 AI-Powered Responses**: Leverages Google's Gemini API for intelligent and conversational responses.
- **🔔 Wake Word Support**: Responds only when the wake word "Jarvis" is detected.
- **🛠️ Customizable**: Easy to modify and extend with new features.

## 🛠️ Technologies Used
- **🐍 Python**: The programming language used for the project.
- **🤖 Google Gemini API**: For natural language processing and generating responses.
- **🎤 SpeechRecognition**: For capturing and processing voice input.
- **🗣️ pyttsx3**: For text-to-speech conversion.
- **🎙️ PyAudio**: For handling microphone input.

## 🚀 Installation
Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Syam-1133/-JARVIS---A-Virtual-Assistant
## Run the project  
```bash
pip install -r requirements.txt
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
python main.py