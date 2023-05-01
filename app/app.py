from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

os.environ["OPENAI_API_KEY"] = "WRITE_YOUR_API_OPENAI_KEY_HERE" #WRITE_YOUR_API_OPENAI_KEY_HERE
# Configuración de OpenAI
openai.api_key = os.environ["OPENAI_API_KEY"]
model_engine = "text-davinci-002"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtener el texto del usuario de los cuadros de texto
        source_lang = request.form["source_lang"]
        target_lang = request.form["target_lang"]
        code = request.form["code"]

        # Traducir el código utilizando la API de OpenAI
        response = openai.Completion.create(
            engine=model_engine,
            prompt=f"Traducir el siguiente código de {source_lang} a {target_lang}: {code}",
            temperature=0.5,
            max_tokens=2048,
            n=1,
            stop=None,
            timeout=10.0,
        )

        # Obtener la respuesta de la API y mostrarla al usuario
        translated_code = response.choices[0].text
        return render_template("index.html", translated_code=translated_code)

    # Si es una solicitud GET, mostrar la página principal
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

