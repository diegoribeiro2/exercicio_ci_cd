import requests
import uvicorn
from fastapi import FastAPI

# Cria uma instância do FastAPI
app = FastAPI()

@app.get("/chat")
def resposta_chat(message: str):
    # Faz uma chamada para a API do ChatGPT
    response = requests.post("https://api.openai.com/v1/chat/completions", 
                             json={"messages": [{"role": "system", "content": "Você é um assistente."}, {"role": "user", "content": message}]}, 
                             headers={"Authorization": "Bearer API_KEY"})
    
    # Retorna a resposta do ChatGPT
    response = response.json()
    # Faz um tratamento com a resposta
    response = response["choices"][0]["text"]
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
