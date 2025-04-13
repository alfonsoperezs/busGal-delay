from sqlmodel import create_engine, Session, SQLModel, text


SQLITE_FILE_NAME = "delay.db"
SQLITE_URL = f"sqlite:///{SQLITE_FILE_NAME}"

engine = create_engine(SQLITE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def create_db():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        session.exec(text("PRAGMA foreign_keys = ON"))