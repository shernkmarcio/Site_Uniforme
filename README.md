# 👔 UNIFORSHERNK — Loja de Uniformes Profissionais

> *"Para de enrolar mano, aproveita essa oferta"* — Carlão, consultor da UNIFORSHERNK

Salve! Esse projeto é um site de vendas de uniformes profissionais com um assistente virtual chamado **Carlão** — um consultor da quebrada, corinthiano, sarrista, que atende via chat com texto e voz. É nois véi!

---

## 🚀 Funcionalidades

- 🛍️ **Catálogo completo** com modal filtrável por categoria (Saúde, Corporativo, Escolar, Industrial)
- 🤖 **Chat com IA** — o Carlão responde dúvidas sobre produtos, tamanhos e preços
- 🎙️ **Voz bidirecional** — reconhecimento de fala (STT) e síntese de voz (TTS) em pt-BR
- 📦 **Descontos por volume** — 15% acima de 10 peças, 25% acima de 50
- 🪡 **Personalização** — bordado com logo/nome disponível
- 📱 **Responsivo** — funciona em desktop e mobile

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|--------|-----------|
| Backend | Python + Flask |
| IA | Google Gemini 2.5 Flash |
| Frontend | HTML + CSS + JS puro |
| Voz | Web Speech API (nativa do browser) |
| Config | python-dotenv |

---

## ⚙️ Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/shernkmarcio/Site_Uniforme.git
cd Site_Uniforme
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install flask python-dotenv google-genai
```

**4. Configure o `.env`**
```bash
# Crie um arquivo .env na raiz do projeto
GEMINI_API_KEY=sua_chave_aqui
FLASK_PORT=5000
FLASK_DEBUG=True
```

**5. Rode o servidor**
```bash
python app.py
```

Acesse: [http://localhost:5000](http://localhost:5000)

---

## 📁 Estrutura do projeto

```
projeto5/
├── app.py                  # Servidor Flask + integração Gemini
├── templates/
│   └── index.html          # Frontend completo
├── .env                    # Variáveis de ambiente (não commitado)
├── .gitignore
└── README.md
```

---

## 💬 Sobre o Carlão

O Carlão é o assistente virtual da UNIFORSHERNK. Ele fala gíria paulistana, torce pro Timão e não deixa cliente sair sem fechar negócio. Configurado via `SYSTEM_PROMPT` no `app.py` — dá pra customizar a personalidade lá.

---

## ⚠️ Avisos

- O reconhecimento de voz funciona melhor no **Google Chrome**
- Nunca suba o `.env` pro GitHub — a chave de API fica exposta
- O servidor Flask em modo `debug=True` é só pra desenvolvimento

---

## 📄 Licença

MIT — usa à vontade, só não esquece de dar os créditos. É nois! 🤙