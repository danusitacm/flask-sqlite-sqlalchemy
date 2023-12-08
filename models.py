from extensions import db

class BaseModel(db.Model):
    __abstract__ = True
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Usuario(BaseModel):
    __tablename__='usuario'
    usuario_pk = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    email = db.Column(db.String(255))
    telefono = db.Column(db.String(255))
    genero = db.Column(db.String(255))
    
    # # Relaciones
    alumno = db.relationship('Alumno', back_populates='usuario', uselist=False)
    tutores = db.relationship('Tutor', back_populates='usuario',uselist=False)

    def __init__(self,nombre,email,telefono,genero) -> None:
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.genero = genero

    def __repr__(self):
        return f"User('{self.username}')"
    
class Alumno(BaseModel):
    __tablename__='alumno'
    alumno_pk=db.Column(db.Integer(), primary_key=True)
    puntaje_alumno=db.Column(db.Float())
    usuario_pk=db.Column(db.Integer, db.ForeignKey('usuario.usuario_pk'),nullable=False)
    
    # # Relaciones 
    usuario = db.relationship('Usuario', back_populates='alumno', uselist=False)
    solicitud = db.relationship('Solicitud', back_populates='alumno')
    tutoria = db.relationship('Tutoria', back_populates='alumno')
    review_tutor = db.relationship('ReviewTutor', back_populates='alumno')
    review_alumno = db.relationship('ReviewAlumno', back_populates='alumno')

    def __init__(self,puntaje_alumno,usuario_pk) -> None:
        self.puntaje_alumno = puntaje_alumno
        self.usuario_pk =usuario_pk

    
    def __repr__(self):
        return '<alumno_pk {}>'.format(self.alumno_pk)

# Tabla de unión para la relación muchos a muchos
tutor_materia = db.Table('tutor_materia',
                        db.Column('materia_pk', db.Integer, db.ForeignKey('materia.materia_pk'), primary_key=True),
                        db.Column('tutor_pk', db.Integer, db.ForeignKey('tutor.tutor_pk'), primary_key=True))

class Tutor(BaseModel):
    __tablename__='tutor'
    tutor_pk=db.Column(db.Integer(), primary_key=True)
    puntaje_tutor=db.Column(db.Float())
    usuario_pk=db.Column(db.Integer, db.ForeignKey('usuario.usuario_pk'),nullable=False)
    
    # Relaciones 
    usuario = db.relationship('Usuario', back_populates='tutores', uselist=False)
    materia = db.relationship('Materia',secondary=tutor_materia, back_populates='tutor')
    tutoria = db.relationship('Tutoria', back_populates='tutor')
    review_tutor = db.relationship('ReviewTutor', back_populates='tutor')
    review_alumno = db.relationship('ReviewAlumno', back_populates='tutor')

    
    def __init__(self,puntaje_tutor,usuario_pk) -> None:
        self.puntaje_tutor = puntaje_tutor
        self.usuario_pk =usuario_pk

    
    def __repr__(self):
        return '<Tutor_pk {}>'.format(self.tutor_pk)
    
class Materia(BaseModel):
    __tablename__='materia'
    materia_pk=db.Column(db.Integer(), primary_key=True)
    nombre=db.Column(db.String(255))
    codigo=db.Column(db.String(255))
    
    #Relaciones
    solicitud = db.relationship('Solicitud', back_populates='materia')
    tutor= db.relationship('Tutor',secondary=tutor_materia, back_populates='materia')
    tutoria= db.relationship('Tutoria',back_populates='materia')
    
    def __init__(self,nombre,codigo) -> None:
        self.nombre = nombre
        self.codigo =codigo

    
    def __repr__(self):
        return '<Materia_pk {}>'.format(self.materia_pk)
    
class Solicitud(BaseModel):
    __tablename__='solicitud'
    solicitud_pk = db.Column(db.Integer, primary_key=True)
    fecha_solicitud = db.Column(db.Date)
    estado_solicitud = db.Column(db.String(255))
    materia_pk = db.Column(db.Integer,db.ForeignKey('materia.materia_pk'),nullable=False)
    alumno_pk = db.Column(db.Integer,db.ForeignKey('alumno.alumno_pk'),nullable=False)
    
    # Relaciones
    alumno = db.relationship('Alumno', back_populates='solicitud')
    materia = db.relationship('Materia', back_populates='solicitud')

    def __init__(self,fecha_solicitud,estado_solicitud,materia_pk,alumno_pk) -> None:
        self.fecha_solicitud = fecha_solicitud
        self.estado_solicitud = estado_solicitud
        self.materia_pk = materia_pk
        self.alumno_pk = alumno_pk
        

    def __repr__(self):
        return '<solicitud_pk {}>'.format(self.solicitud_pk)
    
class Tutoria(BaseModel):
    __tablename__='tutoria'
    tutoria_pk = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    materia_pk = db.Column(db.Integer,db.ForeignKey('materia.materia_pk'),nullable=False)
    alumno_pk = db.Column(db.Integer,db.ForeignKey('alumno.alumno_pk'),nullable=False)
    tutor_pk = db.Column(db.Integer,db.ForeignKey('tutor.tutor_pk'),nullable=False)
    
    # Relaciones
    alumno = db.relationship('Alumno', back_populates='tutoria')
    materia = db.relationship('Materia', back_populates='tutoria')
    tutor= db.relationship('Tutor', back_populates='tutoria')
    
    def __init__(self,fecha_inicio,fecha_fin,materia_pk,alumno_pk,tutor_pk) -> None:
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.materia_pk = materia_pk
        self.alumno_pk = alumno_pk
        self.tutor_pk = tutor_pk
        

    def __repr__(self):
        return '<tutoria_pk {}>'.format(self.tutoria_pk)
    
class ReviewTutor(BaseModel):
    __tablename__='review_tutor'
    review_tutor_pk = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))
    calificacion_tutor = db.Column(db.Float())
    tutor_pk = db.Column(db.Integer,db.ForeignKey('tutor.tutor_pk'),nullable=False)
    alumno_pk = db.Column(db.Integer,db.ForeignKey('alumno.alumno_pk'),nullable=False)
    
    # Relaciones
    alumno = db.relationship('Alumno', back_populates='review_tutor')
    tutor = db.relationship('Tutor', back_populates='review_tutor')

    def __init__(self,descripcion ,calificacion_tutor,alumno_pk,tutor_pk) -> None:
        self.descripcion = descripcion
        self.calificacion_tutor = calificacion_tutor
        self.alumno_pk = alumno_pk
        self.tutor_pk = tutor_pk
        
        

    def __repr__(self):
        return '<review_tutor_pk {}>'.format(self.review_tutor_pk)
    
class ReviewAlumno(BaseModel):
    __tablename__='review_alumno'
    review_alumno_pk = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))
    calificacion_alumno= db.Column(db.Float())
    tutor_pk = db.Column(db.Integer,db.ForeignKey('tutor.tutor_pk'),nullable=False)
    alumno_pk = db.Column(db.Integer,db.ForeignKey('alumno.alumno_pk'),nullable=False)
    
    # Relaciones
    alumno = db.relationship('Alumno', back_populates='review_alumno')
    tutor = db.relationship('Tutor', back_populates='review_alumno')

    def __init__(self,descripcion ,calificacion_alumno,alumno_pk,tutor_pk) -> None:
        self.descripcion = descripcion
        self.calificacion_alumno = calificacion_alumno
        self.alumno_pk = alumno_pk
        self.tutor_pk = tutor_pk
        
        

    def __repr__(self):
        return '<review_alumno_pk {}>'.format(self.review_alumno_pk)