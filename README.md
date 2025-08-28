# Celeste AI

Celeste AI is a multifunctional, voice-activated desktop assistant and automation toolkit. It combines natural language processing, browser automation, music playback, brute-force demonstration tools, and a wake word detection system. Celeste is designed for productivity, research, and educational purposes, integrating AI and automation in a single Python project.

---

## Features

- **Voice Assistant**: Responds to natural language commands for web search, Wikipedia, YouTube, StackOverflow, time, music, and more.
- **Browser Automation**: Automates Google, YouTube, and image searches using Selenium.
- **Music Player**: Plays and lists songs from your local music library.
- **Brute Force Demonstration**: Educational tool to demonstrate password brute-forcing on login forms (for ethical and educational use only).
- **AI Integration**: Uses OpenAI GPT (text-davinci-003) to answer arbitrary questions.
- **Wake Word Detection**: Record, preprocess, and train a neural network to detect custom wake words using audio data.
- **Email Sending**: Send emails via voice command (requires configuration).

---

## Project Structure

```
Celeste/
├── main.py                  # Main entry point, voice assistant logic
├── requirements.txt         # Python dependencies
├── functions/
│   ├── ai_res/gpt.py        # OpenAI GPT integration
│   ├── browser/             # Browser automation modules
│   ├── exploits/            # Brute force and password tools
│   └── system/musicPlayer.py# Music player logic
├── hotword/                 # Wake word detection and audio scripts
│   ├── plot_cm.py
│   ├── PreparingData.py
│   ├── PreprocessingData.py
│   ├── RunParallely.py
│   └── training.py
└── ...
```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Celeste.git
   cd Celeste
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   # For hotword detection, you may also need:
   pip install librosa keras sounddevice matplotlib numpy pandas
   ```

3. **Install ChromeDriver:**
   - Download the version matching your Chrome browser from [here](https://chromedriver.chromium.org/downloads).
   - Add it to your system PATH.

4. **Set up OpenAI API Key:**
   - Create a `.env` file in `functions/ai_res/`:
     ```env
     API=your_openai_api_key_here
     ```

5. **Configure Music Directory:**
   - Edit `functions/system/musicPlayer.py` and set your music directory path in the `directory` variable.

6. **(Optional) Prepare Audio Data for Wake Word Detection:**
   - Use scripts in `hotword/` to record and preprocess audio data, then train the model.

---

## Usage

Run the main assistant:
```bash
python main.py
```

**Sample Voice Commands:**
- "Search Wikipedia for Alan Turing"
- "Open Stack"
- "Play the song Imagine"
- "Songs in my playlist"
- "The time"
- "Open code"
- "Search images for cats"
- "Search Google for Python decorators"
- "Search YouTube for lo-fi music"
- "Run brute force on Instagram"
- "Email to someone"

> **Note:** For brute force and email features, additional configuration is required. Use these features responsibly and ethically.

---

## Educational Brute Force Tool
- The brute force module is for educational and ethical testing only.
- Requires a password list (see `functions/exploits/example_passlist.txt`).
- Never use on accounts or systems you do not own or have explicit permission to test.

---

## Wake Word Detection
- Scripts in `hotword/` allow you to record audio, preprocess data, train, and test a wake word detection model.
- Requires additional dependencies (see above).

---

## Contributing

Contributions are welcome! Please:
- Open issues for bugs or feature requests.
- Fork the repo and submit pull requests.
- Follow best practices for Python code and documentation.

---

## License

This project is for educational and personal use. For any other use, please check the repository license or contact the author.

---

## Disclaimer

Celeste AI includes tools for browser automation and brute force demonstration. Use these features responsibly and only on systems you own or have permission to test. The authors are not responsible for misuse.
