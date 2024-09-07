# Automated Chat Bot

This Python script implements an automated chat bot that responds to messages in a chat window based on predefined keywords and responses.

## Features

- Captures chat window coordinates for consistent operation
- Extracts text from the chat area using OCR (Optical Character Recognition)
- Responds to detected keywords with predefined responses
- Avoids spamming by implementing a cooldown between responses

## Requirements

- Python 3.6+
- pytesseract
- Pillow (PIL)
- pyautogui

## Installation

1. Clone this repository or download the script.
2. Install the required packages:
   ```
   pip install pytesseract Pillow pyautogui
   ```
3. Ensure you have Tesseract OCR installed on your system and accessible in your PATH.

## Usage

1. Prepare a `responses.json` file with your keyword-response pairs. For example:
   ```json
   {
     "hello": ["Hi there!", "Hello!", "Greetings!"],
     "how are you": ["I'm good, thanks!", "Doing well, how about you?"]
   }
   ```

2. Run the script:
   ```
   python chat_bot.py
   ```

3. Follow the prompts to either capture new chat window coordinates or use previously saved ones.

4. The bot will start monitoring the chat area and respond to messages containing the specified keywords.

## Customization

- Modify the `responses.json` file to change the bot's responses.
- Adjust the cooldown period in the `bot_loop` function if needed.

## Note

This script uses screen capture and text input simulation. Make sure to use it responsibly and in compliance with the terms of service of the chat platform you're using.

## Troubleshooting

If the OCR is not working correctly, you may need to adjust the Tesseract path in the script or ensure it's correctly installed on your system.

## License

This project is open source and available under the [MIT License](LICENSE).