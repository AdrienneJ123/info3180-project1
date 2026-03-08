import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file if it exists


class Config(object):
    """Base Config Object"""

    DEBUG = False

    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    default_db = "postgresql://postgres:Host123@localhost/propertiesdb"

    # Use DATABASE_URL if it exists, otherwise use default
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default_db)

    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
            "postgres://", "postgresql://", 1
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # This is just here to suppress a warning from SQLAlchemy as it will soon be removed


    UPLOAD_FOLDER = os.path.join("app", "static", "uploads")
