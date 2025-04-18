# Desktop Assistant

A simple voice assistant that listens to your commands using your mic as the input source and responds using text-to-speech. It can perform tasks like checking the weather, providing the current date and time, and answering queries using AI-powered responses.

## Features

- **Voice Command Recognition**: Listens for and processes spoken commands using your microphone.
- **Text-to-Speech**: Provides verbal responses to the user.
- **Weather Information**: Retrieve current weather information (customizable city).
- **Current Date and Time**: Returns the current date, time, or both.
- **AI-powered Responses**: Responds to user queries with AI-generated answers using Mistral AI.
- **Exit Commands**: Exits or stops the assistant when keywords like `exit`, `quit`, `stop`, etc., are spoken.


## Installation

### 1. Clone the repository

```
git clone https://github.com/Dhyey17/DesktopAssistant.git
```

### 2. Navigate to the project folder

```
cd DesktopAssistant
```

### 3. Install the dependencies

```
pip install -r requirements.txt
```

### 4. Setup Environment variables
You can obtain the necessary API keys from the following services:
- [Hugging Face API Token](https://huggingface.com/settings/tokens)
- [Weather API Key](https://www.weatherapi.com/my)

Create a `.env` file in the root of the project and add the following:
```
HF_TOKEN=your_huggingface_api_token
WEATHER_API_KEY=your_weather_api_key
```


### 5. Run the assistant
```
python main.py
```

