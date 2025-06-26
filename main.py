from core.voice import get_prompt, speak
from utils.command_handler import handle_command

if __name__ == "__main__":
    print("Assistant starting......")
    speak("Assistant started!")

    while True:
        try:
            print("Listening for commands...")
            text = get_prompt()
            response = handle_command(text)
            speak(response)

        except Exception as e:
            print("Error occurred:", e)
            speak("Sorry, something went wrong.")

# todo: active memory
# todo: passive memory

