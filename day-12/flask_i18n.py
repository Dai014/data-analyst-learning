from flask import Flask, request, jsonify
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'es'])

@app.route('/')
def index():
    return _('Hello, World!')

if __name__ == '__main__':
    app.run(debug=True)