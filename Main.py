import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Step 1: Configure Gemini API
def configure_gemini(api_key):
    genai.configure(api_key=api_key)

# Step 2: Initialize Text-to-Speech Engine
def initialize_tts():
    engine = pyttsx3.init()
    return engine

# Step 3: Capture Voice Input
def capture_voice_input(wake_word="jarvis"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio).lower()  # Convert to lowercase
        print(f"You said: {text}")
        if wake_word and text.startswith(wake_word):
            return text.replace(wake_word, "").strip()  # Remove the wake word
        else:
            return text  # Return the full input if no wake word is required
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return None

# Step 4: Get Response from Gemini
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")
    # Add context to the prompt
    full_prompt = f"You are Jarvis, a friendly and helpful AI assistant. Respond to the following in a conversational tone: {prompt}"
    response = model.generate_content(full_prompt)
    print("Full Response Object:", response)  # Debugging: Print the full response
    if response.text:
        return response.text
    else:
        return "Sorry, I couldn't generate a response. Please try again."

# Step 5: Speak the Response
def speak_text(engine, text):
    engine.say(text)
    engine.runAndWait()

# Main Function
def main():
    # Replace with your Gemini API key
    GENAI_API_KEY = "AIzaSyCPDFqKQha-uYDyQUT_fmvkrzDjHEvZhoE"

    # Configure Gemini
    configure_gemini(GENAI_API_KEY)

    # Initialize TTS Engine
    engine = initialize_tts()

    # Greet the user
    greeting = "Hello, I am Jarvis. How can I assist you today?"
    print(greeting)
    speak_text(engine, greeting)

    while True:
        # Capture voice input
        print("Say something...")
        user_input = capture_voice_input(wake_word="jarvis")  # Set wake word to "jarvis"

        if user_input:
            if user_input.lower() in ["exit", "quit", "stop"]:
                print("Exiting...")
                break

            # Get response from Gemini
            response = get_gemini_response(user_input)
            print(f"Jarvis says: {response}")

            # Speak the response
            speak_text(engine, response)

if __name__ == "__main__":
    main()