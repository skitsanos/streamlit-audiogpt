import streamlit as st
import base64
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Streamlit app title
st.title("OpenAI Audio Processing App")

# Record audio from the user's microphone
audio_value = st.audio_input("Speak into your microphone")

if audio_value:
    # Display the recorded audio
    #st.audio(audio_value, format="audio/wav")

    # Get the audio data as bytes using getvalue()
    audio_bytes = audio_value.getvalue()

    # Encode the audio data to base64
    encoded_string = base64.b64encode(audio_bytes).decode('utf-8')

    # Show a spinner while processing the API request
    with st.spinner("Processing your audio..."):
        # Send the audio to OpenAI API for processing
        completion = client.chat.completions.create(
            model="gpt-4o-audio-preview",
            modalities=["text", "audio"],
            audio={"voice": "alloy", "format": "wav"},
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_audio",
                            "input_audio": {
                                "data": encoded_string,
                                "format": "wav"
                            }
                        }
                    ]
                },
            ]
        )

    # Display the text response from the API
    st.write("Response:")
    st.write(completion.choices[0].message.audio.transcript)

    if completion.choices[0].message.content:
        st.write(completion.choices[0].message.content)

    # Decode the audio response from the API
    if hasattr(completion.choices[0].message, 'audio') and completion.choices[0].message.audio:
        wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)

        # Save the audio response to a file (optional)
        with open("response.wav", "wb") as f:
            f.write(wav_bytes)

        # Play the audio response in the app
        st.audio("response.wav", format='audio/wav')
    else:
        st.write("No audio response received.")