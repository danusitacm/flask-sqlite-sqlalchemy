from models import Usuario,Alumno,Tutor,Solicitud,Tutoria,ReviewAlumno,ReviewTutor
from marshmallow import fields,validate
from app import ma

class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Usuario
        load_instance = True
        fields = ("usuario_pk", "nombre", "email", "telefono", "genero")
        ordered=True
        
    usuario_pk = fields.Integer()
    #para validar tengo que haces esto
    # nombre = fields.String(required=True, validate=validate.Length(min=1, max=255),error=" el error")
    
    nombre = fields.String(required=True)
    email = fields.String(required=True)
    telefono = fields.String(required=True)
    genero = fields.String(required=True)

class AlumnoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Alumno
        load_instance = True
        fields = ("alumno_pk", "puntaje_alumno", "usuario_pk")
        ordered=True
        
    alumno_pk = fields.Integer()
    #para validar tengo que haces esto
    # nombre = fields.String(required=True, validate=validate.Length(min=1, max=255),error=" el error")
    puntaje_alumno =fields.Float(required=True)
    usuario_pk = fields.Integer(required=True)

class TutorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tutor
        load_instance = True
        fields = ("tutor_pk", "puntaje_tutor", "usuario_pk")
        ordered=True
        
    tutor_pk = fields.Integer()
    #para validar tengo que haces esto
    # nombre = fields.String(required=True, validate=validate.Length(min=1, max=255),error=" el error")
    puntaje_tutor =fields.Float(required=True)
    usuario_pk = fields.Integer(required=True)

class SolicitudSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Solicitud
        load_instance = True
        fields = ("solicitud_pk", 
                  "fecha_solicitud",
                  "estado_solicitud", 
                  "materia_pk",
                  "alumno_pk")
        ordered=True
        
    solicitud_pk = fields.Integer()
    #para validar tengo que haces esto
    # nombre = fields.String(required=True, validate=validate.Length(min=1, max=255),error=" el error")
    fecha_solicitud =fields.Date(required=True)
    estado_solicitud = fields.String(required=True)
    materia_pk = fields.Integer(required=True)
    alumno_pk = fields.Integer(required=True)

class TutoriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tutoria
        load_instance = True
        fields = ("tutoria_pk", 
                  "fecha_inicio",
                  "fecha_fin", 
                  "materia_pk",
                  "alumno_pk",
                  "tutor_pk")
        ordered=True
    
    tutoria_pk=fields.Integer()
    fecha_inicio=fields.Date(required=True)
    fecha_fin=fields.Date(required=True)
    materia_pk=fields.Integer(required=True)
    alumno_pk=fields.Integer(required=True)
    tutor_pk=fields.Integer(required=True)
    
class ReviewAlumnoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ReviewAlumno
        load_instance = True  
        fields = (
            'review_alumno_pk',
            'descripcion',
            'calificacion_alumno',
            'tutor_pk',
            'alumno_pk',
        )
    review_alumno_pk=fields.Integer()
    descripcion =fields.String(required=True)
    calificacion_alumno =fields.Float(required=True)
    tutor_pk=fields.Integer()
    alumno_pk=fields.Integer()
    
class ReviewTutorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ReviewTutor
        load_instance = True  
        fields = (
            'review_tutor_pk',
            'descripcion',
            'calificacion_tutor',
            'tutor_pk',
            'alumno_pk',
        )
    review_tutor_pk=fields.Integer()
    descripcion =fields.String(required=True)
    calificacion_tutor =fields.Float(required=True)
    tutor_pk=fields.Integer()
    alumno_pk=fields.Integer()
    

#Declaracion de schemas
usuario_schema = UsuarioSchema ()
usuarios_schema  = UsuarioSchema(many=True)

tutor_schema = TutorSchema ()
tutors_schema  = TutorSchema(many=True)

alumno_schema = AlumnoSchema ()
alumnos_schema  = AlumnoSchema(many=True)

solicitud_schema = SolicitudSchema ()
solicitudes_schema  = SolicitudSchema(many=True)

tutoria_schema = TutoriaSchema ()
tutorias_schema  = TutoriaSchema(many=True)

reviewalumnoschema =ReviewAlumnoSchema()
reviewalumnosschema =ReviewAlumnoSchema(many=True)
    
reviewtutorschema =ReviewTutorSchema()
reviewtutoresschema =ReviewTutorSchema(many=True)