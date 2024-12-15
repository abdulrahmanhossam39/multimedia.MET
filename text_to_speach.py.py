import tkinter as tk
from gtts import gTTS
import playsound
import os

# Function to convert text to speech
def text_to_speech():
    text = entry.get()
    if text.strip():  # Check if text is not empty
        tts = gTTS(text=text, lang='en')
        audio_file = "speech.mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)

# Function to clear the text in the entry field
def clear_text():
    entry.delete(0, tk.END)  # Clear all text in the entry field

# Function to exit the application
def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Text to Speech")
root.geometry("500x500")  # Set window size
root.configure(bg="#f0f0f0")  # Light background color

# Add a label
label = tk.Label(root, text="Enter Your Text Below", font=("Courier New", 20, "bold"), bg="#f0f0f0", fg="#333333")
label.pack(pady=30)

# Add a text entry field
entry = tk.Entry(root, width=30, font=("Courier New", 18))
entry.pack(pady=10)

# Add a frame for buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=40)

# Add buttons (vertically aligned)
play_button = tk.Button(button_frame, text="Play", command=text_to_speech,
                        bg="#4caf50", fg="white", font=("Courier New", 14, "bold"), width=15, height=2)
play_button.pack(pady=10)  # Space between buttons

set_button = tk.Button(button_frame, text="Clear", command=clear_text,
                       bg="#2196f3", fg="white", font=("Courier New", 14, "bold"), width=15, height=2)
set_button.pack(pady=10)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app,
                        bg="black", fg="white", font=("Courier New", 14, "bold"), width=15, height=2)
exit_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
