FROM ubuntu:22.04


WORKDIR /app



RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN apt-get install -y libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
RUN apt-get install -y ffmpeg 

EXPOSE 8501

COPY . .


# install python dependencies

RUN pip3 install --upgrade pip
RUN --mount=type=cache,target=/root/.cache \
    pip3 install -r requirements.txt

# gunicorn

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]