import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Status

def _create_session():
    ''' Criando uma sessão para manipular com o banco '''
    url_bd = settings.database_url
    engine = create_engine(url_bd, echo=True)
    Base.metadata.create_all(engine)
    create_session = sessionmaker(bind=engine)
    return create_session()

session = _create_session()

def add_status(data_utc, url, orgao, cod_resposta, status_postado=0):
    session.add(Status(data_utc=data_utc, url=url, orgao=orgao, cod_resposta=cod_resposta, postado=status_postado))
    session.commit()

def get_status(url,orgao,cod_resp,all):
    ''' Recupera registros da tabela "Status" '''

    if all != '':
        consulta = session.query(Status).all()
    elif url != '' and orgao == '' and cod_resp =='':
        consulta = session.query(Status).filter(Status.url == url).all()
    elif url == '' and orgao != '' and cod_resp == '':
        consulta = session.query(Status).filter(Status.orgao == orgao).filter(Status.postado != 1).all()
    elif url == '' and orgao == '' and cod_resp != '':
        consulta = session.query(Status).filter(Status.cod_resp == cod_resp).all()
    else:
        return 'Nenhuma coluna especificada, por favor etc etc...'
        # consulta = session.query(Status).all()
    return consulta


def update_status(id_status):
    session.query(Status).filter(Status.id == id_status).update({'postado': 1})
    session.commit()




