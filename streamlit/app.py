import streamlit as st

# importing packages
from pytube import YouTube
import whisper
import subprocess


@st.cache(show_spinner=False)
def load_model():
    return whisper.load_model("base", download_root="./", in_memory=False)


st.set_page_config(layout="wide", page_title="Extract Sentiment")
st.title("Extract Sentiment")
url = st.text_input(
    "Youtube or Webpage URL",
    "",
    placeholder="https://www.youtube.com/watch?v=gIr9TQnV25A",
)
if st.button("Process"):
    # url input from user
    yt = YouTube(str(url))
    st.markdown(f"<h2> Video Title : {yt.title}</h2> ", unsafe_allow_html=True)
    placeholder = st.empty()

    with st.spinner(text="Extracting audio from the video"):
        # extract only audio"
        video = yt.streams.filter(only_audio=True).first()

        # download the file
        out_file = video.download(output_path="./data/video/")
        title = yt.title.replace("?", "")

        command = f'''ffmpeg -i "data/video/{title}.mp4" -ab 160k -ac 2 -ar 44100 -vn -y "data/audio/{title}.wav"'''

        subprocess.call(command, shell=True)
        model = load_model()

        result = model.transcribe(f"data/audio/{title}.wav")
        placeholder.text_area("transcription", result["text"])
