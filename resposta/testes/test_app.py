from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from scripts.app import app, resposta_chat

client = TestClient(app)

@pytest.fixture
def mock_response():
    return {
        "choices": [{"text": "\nResposta simulada do ChatGPT\n"}]
    }

def test_resposta_chat(mock_response):
    """Teste unitário para a função resposta_chat
    """
    with patch('scripts.app.requests.post') as mock_post:
        mock_post.return_value.json.return_value = mock_response

        response = resposta_chat("Olá")

        # A resposta esperada deve ser apenas o texto da mensagem, sem o '\n'
        assert response == "\nResposta simulada do ChatGPT\n"

def test_rota(mock_response):
    """Teste de integração para a rota /chat"""
    with patch('scripts.app.requests.post') as mock_post:
        mock_post.return_value.json.return_value = mock_response

        response = client.get("/chat", params={"message": "Olá"})

        assert response.status_code == 200
        assert response.json() == "\nResposta simulada do ChatGPT\n"
