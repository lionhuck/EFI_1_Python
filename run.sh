sleep 5

pip install -r requirements.txt
flask db init
flask db migrate -m "initial migration"
flask db upgrade

# Configurar Flask en modo desarrollo
export FLASK_ENV=development
export FLASK_DEBUG=1

# Correr Gunicorn en modo de desarrollo (1 worker, reload activado)
gunicorn app:app --bind 0.0.0.0:5005 --reload --workers=1 --log-level=debug