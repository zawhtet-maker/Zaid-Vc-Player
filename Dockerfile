FROM python:3.10-slim-bullseye

# NTP နဲ့ date sync လုပ်ဖို့ထည့်ပါ
RUN apt-get update && apt-get install -y ffmpeg git ntpdate && \
    ntpdate -u pool.ntp.org && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD python3 main.py
