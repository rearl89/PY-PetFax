from flask import ( Flask, render_template )

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return render_template('home.html')
    
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)
    
    return app