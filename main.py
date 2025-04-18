from core.llm import get_llm_response
from core.voice import *
from features.date_time import get_date, get_time
from features.weather import get_weather

if __name__ == "__main__":
    print("Assistant starting......")
    speak("Assistant started!")
    EXIT_COMMANDS = ["exit", "quit", "shutdown", "close program", "stop assistant", "stop"]

    while True:
        print("Listening for commands...")
        text = get_prompt()

        if any(command in text.lower() for command in EXIT_COMMANDS):
            print("Assistant shutting down!!")
            speak("Assistant shutting down")
            exit()

        elif "weather" in text:
            response = get_weather("Pune")

        elif "time" in text and "date" in text:
            response = get_date() + " " + get_time()

        elif "time" in text:
            response = get_time()

        elif "date" in text:
            response = get_date()
        else:
            response = get_llm_response(text)
            print("LLM:", response)
        speak(response)

# todo: implement memory
coffee=code=0


def deploy_successfully():
    pass


class ProductivityError:
    pass


if coffee and code:
    deploy_successfully()
else:
    raise ProductivityError

