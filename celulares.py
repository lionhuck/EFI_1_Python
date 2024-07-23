from app import db

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)    
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    costo = db.Column(db.Integer, nullable=False)

    modelo = db.relationship('Modelo', backref=db.backref('equipos', lazy=True))
    categoria = db.relationship('Categoria', backref=db.backref('equipos', lazy=True))       

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    caracteristica_id = db.Column(db.Integer, db.ForeignKey('caracteristica.id'), nullable=False)
    
    fabricante = db.relationship('Fabricante', backref=db.backref('modelos', lazy=True))
    caracteristica = db.relationship('Caracteristica', backref=db.backref('modelos', lazy=True))

class Categoria(db.Model):   #Es donde en el texto dice Marca(me parecio mas pertinente ponerle categoria y no marca)
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)

    pais = db.relationship('Pais', backref=db.backref('fabricantes',lazy=True))
class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    descripcion = db.Column(db.String(250), nullable=True)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad_disponible = db.Column(db.Integer, nullable=False)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    almacen_id = db.Column(db.Integer, db.ForeignKey('almacen.id'), nullable=False)

    almacen = db.relationship('Almacen', backref=db.backref('stocks', lazy=True))
    equipo = db.relationship('Equipo', backref=db.backref('stocks', lazy=True))
class Almacen(db.Model):
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


class AccesorioModelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accesorio_id = db.Column(db.Integer, db.ForeignKey('accesorio.id'), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)

    accesorio = db.relationship('Accesorio', backref=db.backref('accesorio_modelos', lazy=True))
    modelo = db.relationship('Modelo', backref=db.backref('accesorio_modelos', lazy=True))


class Pais(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)