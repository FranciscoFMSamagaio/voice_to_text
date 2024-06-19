# Voice Recorder and Translator

Voice Recorder and Translator is a Python application that records audio from the microphone, converts the recorded audio to text, and translates the text from English to French. The application uses the SpeechRecognition, SoundDevice, and Deep Translator libraries to achieve this functionality.

## Features

- Record audio from the microphone.
- Convert recorded audio to text using Google Speech Recognition.
- Translate the converted text from English to French using Google Translator.
- Save the converted text and translated text to files.

## Requirements

- Python 3.6 or higher
- SpeechRecognition library
- SoundDevice library
- NumPy library
- SciPy library
- Deep Translator library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/voice-recorder-translator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd voice-recorder-translator
    ```
3. Install the required libraries:
    ```bash
    pip install speechrecognition sounddevice numpy scipy deep-translator
    ```

## Usage

1. Run the application:
    ```bash
    python main.py
    ```
2. The application will record audio from your microphone for 5 seconds.
3. The recorded audio will be converted to text and saved in `voice_to_text_english.txt`.
4. The converted text will be translated to French and saved in `voice_to_text_translated.txt`.
