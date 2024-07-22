from app import db

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)    
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    costo = db.Column(db.Integer, nullable=False)

    modelo = db.relationship('Modelo', backref=db.backref('equipos', lazy=True))
    marca = db.relationship('Marca', backref=db.backref('equipos', lazy=True))       

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    
    fabricante = db.relationship('Fabricante', backref=db.backref('modelos', lazy=True))

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)

    tipo = db.relationship('Tipo', backref=db.backref('marcas', lazy=True))
class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    pais_origen = db.Column(db.String(30), nullable=False)

class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    descripcion = db.Column(db.String(250), nullable=True)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad_disponible = db.Column(db.Integer, nullable=False)
    ubicacionAlmacen_id = db.Column(db.Integer, db.ForeignKey('ubicacion_almacen.id'), nullable=False)

    ubicacion = db.relationship('UbicacionAlmacen', backref=db.backref('stocks', lazy=True))

class UbicacionAlmacen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    apellido = db.Column(db.String(30), nullable=False)
    mail = db.Column(db.String(50), nullable=False)

class Tipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)
    cantidad_disponible = db.Column(db.String(30), nullable=False)
    ubicacion_almacen = db.Column(db.String(30), nullable=False)    

class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    compatibilidad = db.Column(db.String(30), nullable=False)
