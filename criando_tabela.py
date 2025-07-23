from pathlib import Path

from sqlalchemy import create_engine, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

pasta_atual = Path(__file__).parent 
PATH_TO_BD = pasta_atual / 'bd_usuarios.sqlite'

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True) # quando adicionarmos um novo usuario o sistema ja entende que deve atribuir um id
    nome: Mapped[str] = mapped_column(String(30)) # limitamos a quantidade de caracteres do nome
    senha: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    acesso_gestor: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __repr__(self):
        return f"Usuario({self.id}, {self.nome})"
    
engine = create_engine(f'sqlite:///{PATH_TO_BD}')
Base.metadata.create_all(bind=engine) # cria todas as bases de dados linkadas a classe Base