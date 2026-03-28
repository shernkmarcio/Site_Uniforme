# 🧥 UniformPro — Site de Uniformes com Chat de Voz

## Estrutura do Projeto
```
uniformes_app/
├── app.py              # Servidor Flask + integração Claude API
├── requirements.txt    # Dependências Python
└── templates/
    └── index.html      # Frontend completo com chat de voz
```

## ▶️ Como Rodar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar a API Key
Abra o `app.py` e substitua `SUA_CHAVE_API_AQUI` pela sua chave da Anthropic:
```python
client = anthropic.Anthropic(api_key="sk-ant-...")
```
Ou use variável de ambiente (recomendado):
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

### 3. Rodar o servidor
```bash
python app.py
```
Acesse: http://localhost:5000

## 🎙️ Funcionalidades de Voz
- **Microfone (STT):** Clique no ícone 🎙️ → fale → a mensagem é transcrita automaticamente
- **Resposta em voz (TTS):** O assistente Carlos responde em voz sintetizada em PT-BR
- Visualizador de ondas animado durante gravação/fala

## 💬 Chat de IA
- Assistente "Carlos" com personalidade de consultor
- Conhece todo o catálogo e preços
- Dá desconto para pedidos em lote automaticamente
- Histórico de conversa mantido durante a sessão

> ⚠️ O reconhecimento de voz funciona melhor no Google Chrome
