import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column,Integer ,String,MetaData,Date,Float
from sqlalchemy import inspect

conector = create_engine(
    "postgresql://postgres:postgres@localhost/postgres",
    execution_options={
        "isolation_level": "REPEATABLE READ"
    }
)
mdata = MetaData()

parceiro = Table(
                'Motoca', mdata,
                    Column('id', Integer, primary_key=True),
                    Column('nome', String),
                    Column('cnh', String),
                    Column('conta_bancaria', String),
                    Column('saldo', Float),
                    Column('email',String),
                    Column('Modal',String),
                    Column('Age',Integer)
                )
pedidos = Table(
                "Pedidos", mdata,
                    Column('Cod', String, primary_key=True),
                    Column('Data', Date),
                    Column('Valor',Float),
                    Column('Restaurante',String),
                    Column('Entregador',String),
                    Column('Cliente',String)
                )

mdata.create_all(conector)
inspector = inspect(conector)
print(inspector.get_columns('Pedidos'))

