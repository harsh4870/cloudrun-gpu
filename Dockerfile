FROM ollama/ollama

RUN bash -c "ollama serve &" && sleep 4 && ollama pull gemma2:2b

RUN apt-get update && apt-get install -y python3 pip

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# ENV PORT 8080

ENTRYPOINT bash -c "ollama serve &" && sleep 4 && python3 main.py