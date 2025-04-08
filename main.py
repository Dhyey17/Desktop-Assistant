from utils import *

if __name__ == "__main__":
    print("Assistant starting......")
    speak("Assistant started!")
    EXIT_COMMANDS = ["exit", "quit", "shutdown", "close program", "stop assistant"]

    while True:
        print("Listening for commands...")  # Visual cue
        text = get_prompt()

        if not text or text.strip() == "":
            speak("Got no inputs. Please try again.")
            continue  # Avoid exiting unexpectedly

        if any(command in text.lower() for command in EXIT_COMMANDS):
            speak("Assistant shutting down")
            exit()
        speak(text)