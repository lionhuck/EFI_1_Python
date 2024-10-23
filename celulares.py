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
    
    fabricante = db.relationship('Fabricante', backref=db.backref('modelos', lazy=True))

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


class CaracteristicaModelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caracteristica_id = db.Column(db.Integer, db.ForeignKey('caracteristica.id'), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)

    modelo = db.relationship('Modelo', backref=db.backref('CaracteristicasModelos', lazy=True))
    caracteristica = db.relationship('Caracteristica', backref=db.backref('CaracteristicasModelos', lazy=True))

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    cuit = db.Column(db.String(30), nullable=False)

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