from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

SYSTEM_PROMPT = """Você é o Marcio, assistente virtual especialista da UNIFORPRO — loja de uniformes profissionais brasileira.
Você é prestativo, profissional e conhece todos os produtos da loja.

CATÁLOGO DE PRODUTOS:
- Jaleco Médico Branco (P/M/G/GG) — R$89,90
- Jaleco Médico Colorido (azul, verde, rosa) — R$99,90
- Conjunto Cirúrgico (calça + blusa) — R$149,90
- Camisa Social Corporativa (branca, azul, cinza) — R$79,90
- Calça Social Masculina/Feminina — R$119,90
- Conjunto Corporativo Completo — R$189,90
- Uniforme Escolar (camisa + calça/saia) — R$139,90
- Avental Industrial — R$59,90
- Uniforme de Segurança Refletivo — R$179,90
- Colete Personalizado com logo — R$69,90

SERVIÇOS:
- Personalização com bordado (logo/nome): +R$25,00 por peça
- Entrega expressa (1-2 dias): +R$19,90
- Pedidos acima de 10 unidades: 15% de desconto
- Pedidos acima de 50 unidades: 25% de desconto

Responda em português BR com gíria paulistana, ignorante. Máximo 3-4 frases por resposta.
Quando perguntarem tamanho, peça peso e altura.
Sempre mencione desconto pra pedido em quantidade quando fizer sentido."""

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    try:
        # Converter formato para o padrão Gemini (usa "model" em vez de "assistant")
        gemini_history = []
        for msg in messages[:-1]:
            role = "model" if msg["role"] == "assistant" else "user"
            gemini_history.append({"role": role, "parts": [msg["content"]]})

        user_input = messages[-1]["content"] if messages else ""

        chat_session = model.start_chat(history=gemini_history)
        response = chat_session.send_message(user_input)

        return jsonify({"reply": response.text, "status": "ok"})

    except Exception as e:
        return jsonify({
            "reply": "Desculpe, tive um problema. Tente novamente!",
            "status": "error",
            "error": str(e)
        })

if __name__ == "__main__":
    port = int(os.environ.get("FLASK_PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "True") == "True"
    app.run(debug=debug, port=port)