from flask import Flask
from flask_cors import CORS
from database import db
from routes import products_routes

app = Flask(__name__)


# ===== KHUSUS POSTGRES
# load_dotenv()
# db_name = os.environ.get('DB_NAME')
# user = os.environ.get('DB_USER')
# host = os.environ.get('DB_HOST')
# password = os.environ.get('DB_USER_PASSWORD')
# port = os.environ.get('DB_DB_PORT')
# app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user}:{password}@{host}/{db_name}"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product_in_flask.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

CORS(app)

db.init_app(app)
app.app_context().push()


app.register_blueprint(products_routes, url_prefix='/api/products')


@app.route('/')
def index():
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')