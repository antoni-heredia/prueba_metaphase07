from flask import Flask,request, render_template
from flask_restplus import Api,Resource
from utils import sumaDatos
app = Flask(__name__)


'''
 Rutas servidor web
'''
@app.route('/')
def index():
    """Pagina principal."""
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    """Formulario para añadir datos."""
    return render_template('formulario.html')

'''
 API REST
'''
api = Api(
    app,
    doc='/doc/',
    version="0.1",
    title="Prueba Programación",
    description="Microservicio para la gestión de suma de argumentos"
)

suma = api.namespace("Suma", path="/v1")

number = api.parser()
number.add_argument('datos', action='append')

#Declaro variables para el poder guardar un historico de llamadas al endpoint
#Comenzamos a contar desde 0 ;)
numero_llamada = 0
#Creo una lista de todas las llamadas recibidas para poder llevar un registro
lista_llamadas = []

@suma.route('/suma')
@api.doc(parser=number)
class RealizarSuma(Resource):
    @api.response(200, 'Success')
    def get(self):
        '''
            Devuelve la suma de los argumentos de entrada 
        '''
        #Estas variables son exteriores a la función
        global numero_llamada
        global lista_llamadas
        #recogemos los datos
        datos = request.args.getlist("datos")

        #Obtenemos la suma de los datos
        suma = sumaDatos(datos)

        #Formateamos la llamada para poder guardarla y la guardamos
        llamada =  {"numero_llamada": numero_llamada,
                     "datos_recibidos" : datos,
                     "suma" : suma
                    }
        #Aumentamos en uno la cantidad de llamdas
        numero_llamada += 1
        #Guardamos la llamada actual
        lista_llamadas.append(llamada)
        #Devolvemos la suma
        return { "resultado": suma}

@suma.route('/historial')
class ObtenerHistorial(Resource):
    @api.response(200, 'Success')
    def get(self):
        '''
            Devuelve el historial de todas las llamadas al endpoint /suma
        '''
        #Estas variables son exteriores a la función
        global lista_llamadas
        
        return lista_llamadas

if __name__ == "__main__":
    app.run(debug=True, port=8080)