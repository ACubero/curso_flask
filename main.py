from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Inicio"

@app.route("/hello")
def hello():
    return "Hello World!"

#Para ejecutar la aplicación app.run
# host='0.0.0.0' para que corra en cualquier IP
# puerto = 3000
# debug = True, para desarrollo, pero luego quitarlo en producción para que no salgan los errores
app.run(host='0.0.0.0',port=3000,debug=True) 
