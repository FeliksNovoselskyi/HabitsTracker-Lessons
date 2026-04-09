import sqlalchemy
import sqlalchemy.orm as orm

engine = sqlalchemy.create_engine(url = "sqlite:///db.sqlite3")

base_model = orm.declarative_base()

sessionmaker = orm.sessionmaker(bind = engine)
