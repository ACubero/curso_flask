#make_response sirve para responder rutas pasando parámetros
from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    #creamos una nueva URL: nos entra por /index y nosotros lo reenviamos a /show_information_address
    response = make_response( redirect("/show_information_address") )
    
    #creamos una cookie
    response.set_cookie("user_ip_information",user_ip_information)
    
    #devolvermos la respuesta
    return response

@app.route("/show_information_address")
def show_information_address():
    user_ip = request.cookies.get("user_ip_information")
    return f"Hola que tal? Tu dirección IP es: {user_ip}"

#Para ejecutar la aplicación app.run
# host='0.0.0.0' para que corra en cualquier IP
# puerto = 3000
# debug = True, para desarrollo, pero luego quitarlo en producción para que no salgan los errores
app.run(host='0.0.0.0',port=3000,debug=True) 
