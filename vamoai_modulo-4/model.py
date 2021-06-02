import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column,Integer ,String,MetaData,Date
from sqlalchemy import inspect

engine = create_engine(
    "postgresql://postgres:postgres@localhost/postgres",
    execution_options={
        "isolation_level": "REPEATABLE READ"
    }
)
metadata = MetaData()

books = Table('tabela_1', metadata,
    Column('id', Integer, primary_key=True),
    Column('titulo', String),
    Column('autoria', String),
    )

data = Table(
    "tabela_2",
    metadata,
    Column('lancamentos', Date),
    Column('ISBN', Integer, primary_key=True)
    )

metadata.create_all(engine)



inspector = inspect(engine)
print(inspector.get_columns('tabela_2'))
print(inspector.get_columns('tabela_1'))

