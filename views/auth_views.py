from datetime import timedelta
from flask import request, jsonify, Blueprint

from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
)
from werkzeug.security import (
    generate_password_hash, 
    check_password_hash,
)
from app import db
from celulares import User
from schemas import UserSchema, MinimalUserSchema

auth_bp = Blueprint('auth', __name__)


@auth_bp .route("/users", methods=['POST', 'GET'])
@jwt_required()
def user():

    additional_data = get_jwt()
    administrador = additional_data.get('administrador')
    if request.method == 'POST':  
        if administrador:
            data=request.get_json()
            username=data.get('username')
            password=data.get('password')
            
            password_hashed = generate_password_hash(
                password=password,
                method='pbkdf2',
                salt_length=8,
            )
            try:
                new_user = User(
                    username=username, 
                    password_hash=password_hashed,
                    )
                db.session.add(new_user)
                db.session.commit()

                return jsonify({"Usuario creado": username}), 201
            except:
                return jsonify({"Error" : "Algo salió mal"})
        return jsonify(Mensaje="Ud no esta habilitado para crear un usuario")
    
    if administrador:
        usuarios = User.query.all()
        return UserSchema().dump(usuarios, many=True)
    else:
        usuarios = User.query.all()
        return MinimalUserSchema().dump(usuarios, many=True)

@auth_bp .route("/login", methods=['POST'])
def login():
    data = request.authorization
    username = data.username
    password = data.password

    usuario = User.query.filter_by(username=username).first()

    if usuario and check_password_hash(
        pwhash=usuario.password_hash, 
        password=password,
    ):
        acces_token = create_access_token(
            identity=username,
            expires_delta=timedelta(minutes=30),
            additional_claims=dict(
                administrador=usuario.is_admin,
                )
        )
        return jsonify({"Mensaje":f"Token {acces_token}"})
    return jsonify({"Mensaje":"NO MATCH"})