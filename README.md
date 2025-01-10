# OpenAI Audio Processing App

This Streamlit app allows users to record audio from their microphone, send it to the OpenAI API for processing, and receive both text and audio responses. It leverages OpenAI's `gpt-4o-audio-preview` model to transcribe and respond to audio input.

## Features

- **Audio Input**: Record audio directly from your microphone.
- **OpenAI API Integration**: Send audio to OpenAI for transcription and response generation.
- **Text and Audio Output**: Receive a text transcription of your audio and an optional audio response.
- **User-Friendly Interface**: Simple and intuitive interface powered by Streamlit.

## Prerequisites

Before running the app, ensure you have the following:

1. **Python 3.9 or higher**: The app is built using Python.
2. **OpenAI API Key**: You need an API key from OpenAI to use their services. Sign up at [OpenAI](https://platform.openai.com/signup) if you don't have an account.
3. **Streamlit**: The app is built using the Streamlit framework.

## Installation

1. **Clone the repository** (if applicable):

   bash

   Copy

   ```
   git clone https://github.com/skitsanos/streamlit-audiogpt.git
   cd streamlit-audiogpt
   ```

2. **Install dependencies**:

   bash

   Copy

   ```
   pip install streamlit openai
   ```

3. **Set up your OpenAI API key**:

   - Create a `.env` file in the root directory of the project.

   - Add your OpenAI API key to the `.env` file:

     Copy

     ```
     OPENAI_API_KEY=your-api-key-here
     ```

   - Alternatively, you can set the API key directly in the app code (not recommended for production).

## Running the App

1. **Navigate to the project directory**:

   bash

   Copy

   ```
   cd your-repo-name
   ```

2. **Run the Streamlit app**:

   bash

   Copy

   ```
   streamlit run app.py
   ```

3. **Open the app in your browser**:

   - Streamlit will provide a local URL (e.g., `http://localhost:8501`).
   - Open the URL in your browser to use the app.

## How to Use

1. **Record Audio**:
   - Click the "Speak into your microphone" button to start recording.
   - Stop recording when you're done.
2. **Process Audio**:
   - The app will send your audio to the OpenAI API for processing.
   - A spinner will indicate that the app is working on your request.
3. **View Results**:
   - The app will display:
     - A text transcription of your audio.
     - A text response from the OpenAI model (if applicable).
     - An audio response (if available).
4. **Repeat**:
   - Record new audio and repeat the process as needed.

## Customization

- **Model**: You can change the OpenAI model in the `app.py` file by modifying the `model` parameter in the `client.chat.completions.create` call.
- **Voice**: The app uses the `alloy` voice for audio responses. You can change this by modifying the `audio` parameter in the API call.
- **Styling**: You can customize the app's appearance by modifying the CSS in the `st.markdown` section.

## Troubleshooting

- **API Key Issues**: Ensure your OpenAI API key is correctly set in the `.env` file or app code.
- **Audio Recording Problems**: Make sure your microphone is working and that the app has permission to access it.
- **Network Errors**: Check your internet connection if the app fails to communicate with the OpenAI API.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request. Contributions are welcome!

------

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/).
- Powered by [OpenAI](https://openai.com/).