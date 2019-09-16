from sqlalchemy import Column, Sequence, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Status(Base):
    ''' Criando tabela chamada "Status", onde gravamos todas as tentativas falhas de acesso aos sites.
    Criamos as colunas:
    id = criado pelo sql para cada requisição;
    data_utc = salva datas e hora no fuso horário utc;
    url = site que falhou;
    orgao = órgão responsável pela manutenção do site que falhou;
    cod_resposta = código resultante da falha de requisição'''

    __tablename__ = 'status'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    data_utc = Column(DateTime(timezone=False))
    url = Column(String(300))
    orgao = Column(String(40))
    cod_resposta = Column(String(300))
    postado = Column(Integer) #0 para falso 1 para verdadeiro ## indica se já foi postado

# Substitui a representação padrão do objeto pelas informações da tabela 'Status'

    def __repr__(self):
        return "< Status ({id}, {data_utc}, {orgao}, {cod_resposta}) >".format(id=self.id, data_utc=self.data_utc, orgao=self.orgao, cod_resposta=self.cod_resposta)
