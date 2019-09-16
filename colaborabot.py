# Importando as libraries
import rows
import datetime
import json
import csv

from pathlib import Path
from time import sleep
from requests import get, exceptions
import settings

import sqlalchemy
from sqlalchemy import create_engine
from db import add_status


from divulga import lista_frases, checar_timelines, google_sshet
from autenticadores import twitter_auth, google_api_auth, masto_auth

# Parametros de acesso das urls

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' + \
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

TOTAL_TENTATIVAS = 10
STATUS_SUCESSO = 200

DIA = datetime.datetime.now().day
MES = datetime.datetime.now().month
ANO = datetime.datetime.now().year

data = '{:02d}/{:02d}/{:02d}'.format(DIA, MES, ANO) # Exemplo: 11/04/2019

def criar_tweet(url, orgao):
    """ 
    Criando o tweet com o status do site recém acessado
    """
    twitter_bot.update_status(lista_frases(url=url, orgao=orgao))

def carregar_dados_site():
    """
    Abrindo a lista de portais da transparência
    """
    return rows.import_from_csv("dados/lista_portais.csv")

def plan_gs(dia, mes, ano):
    """
    Cria planilha no Google Drive, preenche o cabeçalho (data e hora no fuso horário de Brasília,
    data e hora no UTC, url afetada, órgão responsável e código de resposta do acesso).
    A planilha criada possui as permissões de leitura para qualquer pessoa com o link, porém somente a conta da API do
    bot (que não é a mesma conta usada pela equipe) consegue alterar os dados contidos nela.
    Também é acessado uma planilha índice (docs.google.com/spreadsheets/d/1kIwjn2K0XKAOWZLVRBx9lOU5D4TTUanvmhzmdx7bh0w)
    e incluído a planilha de logs nela, na segunda tabela.
    """

    lista_planilhas = []
    todas_planilhas = google_drive_creds.list_spreadsheet_files()

    for item in todas_planilhas:
        lista_planilhas.append(item['name'])

    # Cria tabela no Google Sheets caso não encontre uma com o mesmo nome

    if f'colaborabot-sites-offline-{dia:02d}{mes:02d}{ano:04d}' not in lista_planilhas:
        planilha = google_drive_creds.create(f'colaborabot-sites-offline-{dia:02d}{mes:02d}{ano:04d}')  # Exemplo de nome final: colaborabot-sites-offline-27022019
        cabecalho = planilha.get_worksheet(index=0)
        cabecalho.insert_row(values=['data_bsb', 'data_utc', 'url', 'orgao', 'cod_resposta'])

        plan_indice = google_drive_creds.open_by_key('1kIwjn2K0XKAOWZLVRBx9lOU5D4TTUanvmhzmdx7bh0w')
        tab_indice = plan_indice.get_worksheet(index=1)
        endereco = f'docs.google.com/spreadsheets/d/{planilha.id}/'
        tab_indice.append_row(values=[data, endereco])

    # Caso a tabela já exista, usa a existente

    else:
        planilha = google_drive_creds.open(title=f'colaborabot-sites-offline-{dia:02d}{mes:02d}{ano:04d}') 
    
    # Descanso de 5 segundos para evitar problema de concorrência
    sleep(5)
    # Compartilhando tabela no modo público e de somente leitura
    planilha.share(None, perm_type='anyone', role='reader')
    print(f'https://docs.google.com/spreadsheets/d/{planilha.id}\n')
    return planilha

def preenche_tab_gs(planilha, dados):
    """
    Escrevendo na planilha
    """
    tabela = google_drive_creds.open(planilha.title)
    planilha = tabela.get_worksheet(index=0)
    planilha.append_row(values=dados)

def busca_disponibilidade_sites(sites):
    """
    Percorrendo a lista de sites para verificar
    a sua disponibilidade. Caso o código de status
    seja 200 (OK), então ela está disponível para acesso.
    """
    for row in sites:
        url, arroba, orgao = row.url, row.arroba, row.orgao

        for tentativa in range(TOTAL_TENTATIVAS):
            try:
                momento = datetime.datetime.now()
                resposta = get(url, timeout=30, headers=headers)

                if resposta.status_code == STATUS_SUCESSO:
                    print(f'{momento}; O site {url} funcionou corretamente.')
                    break
                else:
                    if tentativa == TOTAL_TENTATIVAS:
                        if not settings.debug:
                            add_status(data_utc=momento, url=url, orgao=orgao, cod_resposta=resposta.status_code)
                        print(f"""{momento}; url: {url}; orgão: {orgao}; resposta: {resposta.status_code}""")
                        if not settings.debug:
                            pass
                            # checar_timelines(twitter_handler=twitter_bot, mastodon_handler=mastodon_bot, url=url, orgao=orgao)

            except (exceptions.ConnectionError, exceptions.Timeout, exceptions.TooManyRedirects) as e:
                if not settings.debug:
                    add_status(data_utc=momento, url=url, orgao=orgao, cod_resposta=str(e))
                print(f"""{momento}; url: {url}; orgão: {orgao}; resposta:{str(e)}""")
                if not settings.debug:
                    # checar_timelines(twitter_handler=twitter_bot, mastodon_handler=mastodon_bot, url=url, orgao=orgao)
                    pass
                break


if __name__ == '__main__': 
    if not settings.debug:
        mastodon_bot = masto_auth()
        twitter_bot = twitter_auth()
        google_creds = google_api_auth()
        google_drive_creds = google_sshet()
        planilha_google = plan_gs(dia=DIA, mes=MES, ano=ANO)
    sites = carregar_dados_site()
    while True:
        busca_disponibilidade_sites(sites)
        sleep(600)
