from core.llm import get_llm_response
from features.date_time import get_date, get_time
from features.weather import get_weather
from core.voice import speak

EXIT_COMMANDS = ["exit", "quit", "shutdown", "close program", "stop assistant", "stop"]

def handle_command(text: str) -> str:
    text = text.lower()

    if any(cmd in text for cmd in EXIT_COMMANDS):
        speak("Assistant shutting down")
        print("Assistant shutting down!!")
        exit()

    elif "weather" in text:
        return get_weather("Pune")

    elif "time" in text and "date" in text:
        return f"{get_date()} {get_time()}"

    elif "time" in text:
        return get_time()

    elif "date" in text:
        return get_date()

    else:
        response = get_llm_response(text)
        print("LLM:", response)
        return response
