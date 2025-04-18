from datetime import datetime

def get_time():
    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        part_of_day = "morning"
    elif 12 <= hour < 17:
        part_of_day = "afternoon"
    elif 17 <= hour < 21:
        part_of_day = "evening"
    else:
        part_of_day = "night"

    formatted_time = now.strftime("%I:%M %p")
    return f"The time is {formatted_time}."

def get_date():
    now = datetime.now()
    return f"Today is {now.strftime('%A, %B %d, %Y')}."
