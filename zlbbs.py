from flask import Flask
import config
from apps.cms import bp as cms_bp
from apps.common import bp as com_bp
from apps.front import bp as front_bp
from exts import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(cms_bp)
    app.register_blueprint(com_bp)
    app.register_blueprint(front_bp)

    db.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
