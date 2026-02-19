FROM python:3.10-slim-bullseye

# Timezone ထည့်ပါ (Asia/Yangon)
ENV TZ=Asia/Yangon
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# ffmpeg နဲ့ git ကိုထည့်ပါ
RUN apt-get update && apt-get install -y ffmpeg git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD python3 main.py
