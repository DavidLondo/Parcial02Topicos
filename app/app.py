from flask import Flask, render_template

app = Flask(__name__)

# Función que calcula el factorial de un número dado
def factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos."
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# No se define ninguna ruta, se deja que el programa esté en la pagina de inicio
@app.route("/<int:numero>")
def inicio(numero):
    resultado = factorial(numero)
    return render_template("index.html", numero=numero, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)