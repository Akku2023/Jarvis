# Jarvis – AI Voice Assistant 🎙️🤖

Jarvis is a Python-based voice assistant that listens for the wake word **"Jarvis"**, recognizes voice commands, performs basic tasks, and responds using speech. It integrates speech recognition, text-to-speech conversion, web browsing, music playback, and a locally running LLM through Ollama.

## ✨ Features

- **Wake Word Detection:** Activates when you say "Jarvis".
- **Speech Recognition:** Captures voice commands through your microphone using Google Speech Recognition.
- **Text-to-Speech:** Converts text responses into speech using Google Text-to-Speech (gTTS) and Pygame.
- **Website Navigation:** Opens popular websites using voice commands.
- **Music Playback:** Plays songs by opening their associated links from a custom music library.
- **AI-Powered Responses:** Uses the Llama 3.2 model through Ollama to process general queries.
- **Command Processing:** Routes recognized commands to predefined actions or the AI model.

## 🛠️ Technologies Used

- **Python** – Main programming language.
- **SpeechRecognition** – Captures and recognizes spoken commands.
- **PyAudio** – Provides microphone audio input for SpeechRecognition.
- **gTTS** – Converts text into spoken audio.
- **Pygame** – Plays generated audio files.
- **Ollama** – Runs the Llama 3.2 language model locally.
- **Webbrowser** – Opens websites in the default browser.
- **Pyttsx3** – Provides an alternative offline text-to-speech implementation.
- **Music Library** – A custom Python module containing song names and their links.

## 📁 Project Structure

```text
Jarvis/
│
├── main.py              # Main voice assistant application
├── client.py            # Client application
├── client1.py           # Additional client application
├── musicLibrary.py      # Dictionary of songs and their URLs
└── README.md            # Project documentation
```

*Note: `main.py` is an example filename. Replace it with the actual filename of your Python script if different.*

## ⚙️ Prerequisites

Before running Jarvis, make sure you have:

- Python 3.9 or later.
- A working microphone.
- Speakers or headphones.
- An active internet connection for Google Speech Recognition, gTTS, and website access.
- Ollama installed on your system.
- The Llama 3.2 model downloaded through Ollama.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Jarvis
```

Alternatively, download the project and open its directory in your terminal.

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install SpeechRecognition pyttsx3 gTTS pygame ollama PyAudio
```

If PyAudio fails to install, install the appropriate system audio dependencies or use a compatible prebuilt package for your operating system.

### 4. Install and Configure Ollama

Download and install Ollama from:

https://ollama.com/

Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Start Ollama if it is not already running:

```bash
ollama serve
```

If Ollama is already running as a background service, you do not need to start it again.

### 5. Configure the Music Library

Create a `musicLibrary.py` file containing a dictionary that maps song names to their URLs.

Example:

```python
music = {
    "song1": "https://www.youtube.com/",
    "song2": "https://open.spotify.com/"
}
```

Replace the example entries with your preferred song links. The dictionary keys should be single words because the current command handler uses the second word of a recognized command as the song key.

For example, saying **"Play song1"** opens the corresponding URL in your browser.

## ▶️ How to Run

Run the Python script:

```bash
python main.py
```

Jarvis will announce that it is initializing and begin listening for the wake word.

### Example Voice Commands

| Voice command | Action |
|---|---|
| "Jarvis" | Activates the assistant |
| "Open Google" | Opens Google |
| "Open YouTube" | Opens YouTube |
| "Open Facebook" | Opens Facebook |
| "Open Instagram" | Opens Instagram |
| "Open LinkedIn" | Opens LinkedIn |
| "Play song1" | Opens the configured song URL |
| "What is artificial intelligence?" | Sends the question to the Llama 3.2 model |

For general questions, Jarvis prints the AI response and attempts to speak it aloud.

## 🧠 How It Works

1. **Initialization:** The assistant initializes its speech and audio components.
2. **Wake Word Listening:** The microphone captures short audio clips, which Google Speech Recognition converts to text.
3. **Wake Word Matching:** When the recognized text matches "Jarvis", the assistant responds with an acknowledgment.
4. **Command Listening:** The microphone captures the next spoken command.
5. **Command Processing:** The `processCommand()` function checks whether the command matches a predefined website or music action.
6. **AI Processing:** If no predefined command matches, the command is sent to the Llama 3.2 model through Ollama.
7. **Voice Response:** The `speak()` function converts text to audio, plays the generated MP3 file, and removes the temporary file.

## 📌 Main Functions

| Function | Purpose |
|---|---|
| `speak_old(text)` | Uses pyttsx3 for speech synthesis. |
| `speak(text)` | Converts text to speech using gTTS and plays it with Pygame. |
| `aiProcess(command)` | Sends a command to the Llama 3.2 model and prints its response. |
| `processCommand(c)` | Executes predefined commands or forwards general queries to the AI model. |

## ⚠️ Important Notes and Limitations

- **Internet connection:** Google Speech Recognition and gTTS require internet access. Website access also requires connectivity.
- **Local AI model:** Ollama runs the Llama 3.2 model locally, but the model must be installed and the Ollama service must be accessible.
- **Microphone permissions:** Make sure your operating system allows Python to access the microphone.
- **Wake word accuracy:** The current implementation uses speech recognition to detect "Jarvis"; it is not a dedicated always-on wake-word detection engine.
- **Command handling:** Website commands are predefined, and music commands must match keys in `musicLibrary.py`.
- **AI speech response:** Currently, `aiProcess()` prints the model's response but does not return it. As a result, the AI response is not passed correctly to `speak()` in `processCommand()`. To enable spoken AI responses, add the following line at the end of `aiProcess()`:

```python
return response["message"]["content"]
```

- **Audio playback:** Pygame must be able to initialize its audio mixer and play MP3 files on your system.
- **Error handling:** The main loop catches exceptions, but more specific error handling can make troubleshooting easier.

## 🔮 Future Improvements

- Implement dedicated wake-word detection.
- Add weather updates and news headlines.
- Support more websites and multiword song names.
- Add reminders, timers, and calendar integration.
- Improve error handling and microphone calibration.
- Add conversation history for more contextual AI responses.
- Support offline speech recognition and offline text-to-speech.
- Introduce a configuration file for customizable commands and settings.

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Open a pull request describing your improvements.

## 📄 License

This project is available for personal learning and experimentation. Add a license file, such as an MIT License, if you want to explicitly define how others may use, modify, and distribute the project.

---

**Built with Python, speech recognition, and Ollama.**

*Meet Jarvis — your personal voice-controlled AI assistant!* 🚀
