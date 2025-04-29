from flask import Flask, Blueprint, render_template

# Create a Flask application
app = Flask(__name__)

# Create a blueprint
example_blueprint = Blueprint('example', __name__)

@example_blueprint.route('/')
def home():
    return render_template('home.html')

# Register the blueprint with the application
app.register_blueprint(example_blueprint, url_prefix='/example')

if __name__ == '__main__':
    app.run(debug=True)