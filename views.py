from models import Usuario,Alumno,Tutor,Solicitud,Tutoria,ReviewAlumno,ReviewTutor
from schemas import usuarios_schema
from flask import Blueprint,request, jsonify
from extensions import db

usuarios_bp = Blueprint('usuarios_bp', __name__)
@usuarios_bp.route('/')  # Ruta para la página de inicio
def index():
    return 'hola mundo'


@usuarios_bp.route('/usuario')  
def obtener_usuarios():
    if request.method == 'GET':
        usuario = Usuario.query.all()
        return usuarios_schema.dump(usuario)

