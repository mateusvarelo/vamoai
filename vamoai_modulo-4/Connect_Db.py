import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column,Integer ,String,MetaData,Date
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates, Session



conexao = create_engine(
    "postgresql://postgres:postgres@localhost/postgres",
    execution_options={
        "isolation_level": "REPEATABLE READ"
    }
)
mdata = MetaData()

"""
books = Table('livros', mdata,
    Column('id', Integer, primary_key=True),
    Column('titulo', String),
    Column('autoria', String),
    )

data = Table("dados", mdata,
    Column('lancamentos', Date),
    Column('ISBN', Integer),
    Column('codigo', Integer, primary_key=True)
    )
"""

mdata.create_all(conexao)

Base = declarative_base(metadata=mdata)


# inspector = inspect(conexao)
# print(inspector.get_columns('livros'))
# print(inspector.get_columns('dados'))

#class
class Livros(Base):
   __tablename__ = 'livros'
   id = Column('id', Integer, primary_key=True)
   _titulo = Column('titulo', String)
   autoria = Column('autoria', String)

class Dados(Base):
    __tablename__ = 'dados'
    lancamentos = Column('lancamentos', Date)
    isbn = Column('ISBN', Integer)
    codigo = Column('codigo', Integer, primary_key=True)
    
@validates('isbn')
def validate_ISBN(self, key, isbn):
    print("entrou")
    print(isbn)
    if len(str(isbn)) != 13:
        raise ValueError(
                    "O ISBN precisa conter 13 dígitos")
    else:
        print("O ISBN está correto")   
        
with Session(conexao) as session:
    dados_do_livro = Dados()
    dados_do_livro.isbn = 12345678901239
    session.add(dados_do_livro)
    session.commit()   
    