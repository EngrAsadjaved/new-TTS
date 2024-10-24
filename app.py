# app.py
import streamlit as st
from TTS.api import TTS
import os

# Initialize the Tacotron2-DDC model
st.title("Text-to-Speech with Tacotron2-DDC")
st.write("Convert text to speech using the Tacotron2-DDC model.")

model_name = "tts_models/en/ljspeech/tacotron2-DDC"
tts = TTS(model_name)

# Input text from user
input_text = st.text_area("Enter the text you want to convert to speech:", "Hello, this is a test of the Tacotron2 DDC text-to-speech model.")

# Generate speech and save it to a file when the user clicks the button
if st.button("Generate Speech"):
    output_path = "output.wav"
    tts.tts_to_file(text=input_text, file_path=output_path)
    st.success("Speech generated successfully!")

    # Ensure the file exists and display the audio player for the user to listen to the generated audio
    if os.path.exists(output_path):
        audio_file = open(output_path, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/wav")

        # Clean up the audio file to save space after playing
        audio_file.close()
        os.remove(output_path)
