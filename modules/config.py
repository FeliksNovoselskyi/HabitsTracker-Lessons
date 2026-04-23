import os, dotenv

dotenv_path = os.path.abspath(
    os.path.join(__file__, "..", "..", ".env")
)

dotenv.load_dotenv(dotenv_path = dotenv_path)

ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")