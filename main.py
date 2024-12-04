import os
from flask import Flask, request
from llama_index.llms.ollama import Ollama
llm = Ollama(model="gemma2:2b")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def call_function():
    body = request.get_json(force=True)
    prompt = body['prompt']
    response = llm.complete(prompt)
    return f"{response}"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT',8080)))