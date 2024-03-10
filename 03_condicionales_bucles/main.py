#make_response sirve para responder rutas pasando parámetros
from flask import Flask, request, make_response, redirect,render_template

app = Flask(__name__)

items = ["Item1","Item2","Item3","Item4"]
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
    # creamos una variable context para crear un diccionario y pasarle todas las variables en una
    # sino en el render_template tendríamos que pasar cada una de las variables independientemente
    context = {
        "user_ip":user_ip,
        "items":items
    }
    # Si pusieramos el parámetro context=context, en el html/jinja, tendriamos que ir poniendo context. delante de cada variable
    # pero al ponerle el ** desconstruimos el contenido y podemos acceder directamente desde el html/jinja a cada uno de los elementos
    # del diccionario
    return render_template("ip_information.html",**context)

#Para ejecutar la aplicación app.run
# host='0.0.0.0' para que corra en cualquier IP
# puerto = 3000
# debug = True, para desarrollo, pero luego quitarlo en producción para que no salgan los errores
app.run(host='0.0.0.0',port=3000,debug=True) 
