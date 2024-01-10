print('speech_recognition project using google library')

import speech_recognition as sr

def speech_to_text():
    # Create a speech recognition object
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        # Adjust for ambient noise before listening
        recognizer.adjust_for_ambient_noise(source)
        # Listen to the speech
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Transcribing...")
        # Use the Google Web Speech API to convert speech to text
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    speech_to_text()


print('Finalise the project')