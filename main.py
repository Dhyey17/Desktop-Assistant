from model import get_llm_response
from utils import *

if __name__ == "__main__":
    print("Assistant starting......")
    speak("Assistant started!")
    EXIT_COMMANDS = ["exit", "quit", "shutdown", "close program", "stop assistant", "stop"]

    while True:
        print("Listening for commands...")
        text = get_prompt()

        if any(command in text.lower() for command in EXIT_COMMANDS):
            speak("Assistant shutting down")
            exit()
        else:
            response = get_llm_response(text)
            print("LLM:", response)
            speak(response)
