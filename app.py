from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'chave-secreta-bvapp-gestao-pessoas'
    
    from unidades_consumidoras.routes import uc_bp
    from operadoras_energia.routes import operadora_bp
    from prestadores_servicos.routes import prestador_bp

    app.register_blueprint(uc_bp, url_prefix='/unidades-consumidoras')
    app.register_blueprint(operadora_bp, url_prefix='/operadoras-energia')
    app.register_blueprint(prestador_bp, url_prefix='/prestadores-servicos')

    @app.route('/')
    def index():
        return "BVapp - Módulo de Gestão de Pessoas"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)