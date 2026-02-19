FROM python:3.10-slim-bullseye

ENV TZ=Asia/Yangon
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y ffmpeg git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV PORT=8080
EXPOSE 8080

# server.py error ကိုရှောင်ဖို့
CMD ["sh", "-c", "python main.py 2>&1"]
