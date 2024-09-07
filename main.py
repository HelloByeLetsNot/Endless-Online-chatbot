import pytesseract
from PIL import ImageGrab
import pyautogui
import time
import random
import json

def load_responses(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def capture_window_coordinates():
    print("Move your mouse to the top-left corner of the chat area and press ENTER.")
    input("Press Enter to capture the top-left corner...")
    top_left = pyautogui.position()
    print(f"Top-left corner captured at: {top_left}")

    print("Move your mouse to the bottom-right corner of the chat area and press ENTER.")
    input("Press Enter to capture the bottom-right corner...")
    bottom_right = pyautogui.position()
    print(f"Bottom-right corner captured at: {bottom_right}")

    return (top_left.x, top_left.y, bottom_right.x, bottom_right.y)

def save_window_coordinates(coords, filename="window_coords.json"):
    with open(filename, 'w') as f:
        json.dump({"bbox": coords}, f)
    print(f"Coordinates saved to {filename}")

def load_window_coordinates(filename="window_coords.json"):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return tuple(data['bbox'])
    except FileNotFoundError:
        print("No saved coordinates found. Please capture window coordinates first.")
        return None

def extract_chat_text(bbox):
    img = ImageGrab.grab(bbox=bbox)
    chat_text = pytesseract.image_to_string(img)
    return chat_text.lower()

def reply_to_chat(chat_text, responses):
    for keyword, reply_list in responses.items():
        if keyword in chat_text:
            reply = random.choice(reply_list)
            print(f"Responding with: {reply}")
            pyautogui.write(reply)
            pyautogui.press('enter')
            return True
    return False

def bot_loop(json_file, bbox):
    responses = load_responses(json_file)
    last_response_time = time.time()

    while True:
        chat_text = extract_chat_text(bbox)
        print(f"Detected chat: {chat_text}")

        if time.time() - last_response_time > 5:
            if reply_to_chat(chat_text, responses):
                last_response_time = time.time()

        time.sleep(1)

def main():
    print("Do you want to capture the chat window coordinates? (y/n)")
    choice = input().lower()

    if choice == 'y':
        bbox = capture_window_coordinates()
        save_window_coordinates(bbox)
    else:
        bbox = load_window_coordinates()
        if bbox is None:
            print("No coordinates available. Exiting.")
            return

    bot_loop('responses.json', bbox)

if __name__ == "__main__":
    main()