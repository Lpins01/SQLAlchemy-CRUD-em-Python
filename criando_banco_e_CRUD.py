from pathlib import Path

from sqlalchemy import create_engine, String, Boolean, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# Aula 3 - Criando tabela

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
        return f"Usuario({self.id=}, {self.nome=})"
    
engine = create_engine(f'sqlite:///{PATH_TO_BD}')
Base.metadata.create_all(bind=engine) # cria todas as bases de dados linkadas a classe Base

# Aula 4 - parte inicial do CRUD (Create + Read)

def cria_usuarios(nome, senha, email, **kwargs):
    with Session(bind=engine) as session:
        usuario = Usuario(
            nome=nome,
            senha=senha,
            email=email,
            **kwargs
        )
        session.add(usuario)
        session.commit()

def le_usuarios():
    with Session(bind=engine) as session:
        comando_sql = select(Usuario)
        usuarios = session.execute(comando_sql).fetchall()
        usuarios = [usuario[0] for usuario in usuarios]
        return usuarios
    
def le_usuario_id(id):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuario = session.execute(comando_sql).fetchall()
        return usuario[0][0]


if __name__ == '__main__':
    # cria_usuarios(
    #     'Leonardo Pinheiro',
    #     senha='minha_senha',
    #     email='meuemail.com'
    # )

    # usuarios = le_usuarios()
    # usuario_0 = usuarios[0]
    # print(usuario_0)
    # print(usuario_0.nome, usuario_0.senha, usuario_0.email)

    usuario_leonardo = le_usuario_id(id=1)
    print(usuario_leonardo)
    print(usuario_leonardo.nome, usuario_leonardo.senha, usuario_leonardo.email)