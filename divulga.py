from autenticadores import google_api_auth
from random import choice
import gspread
from datetime import datetime


def google_sshet():
    """
    Função simples para retornar um objeto capaz de manipular as planilhas do Google Sheets.
    """
    session = google_api_auth()
    ggle_cred = gspread.Client(None, session)
    return ggle_cred

def calculo_tempo():
    from db import get_status

def lista_frases(url, orgao):
    momento = datetime.now()
    ano, mes, dia, hora, minuto, segundo, dia_semana, dia_ano, tm_isdst = momento.timetuple()
    horario = f"{mes:02d}/{dia} - {hora}:{minuto}"
    com_orgao = [
        f"🤖 [{horario}] O portal com dados públicos {url} do órgão {orgao} parece não estar funcionando. Poderia me ajudar a checar?",
        f"🤖 [{horario}] Hum, parece que o site {url}, mantido pelo órgão {orgao}, está apresentando erro. Poderia dar uma olhadinha?",
        f"🤖 [{horario}] Poxa, tentei acessar {url} e não consegui. Este site é mantido pelo órgão {orgao}. Você pode confirmar isso?",
        f"🤖 [{horario}] Não consigo acessar {url}, e eu sei que ele é mantido pelo órgão {orgao}. Você pode me ajudar a verificar?",
        f"🤖 [{horario}] Sabe o portal {url}, mantido pelo orgão {orgao}? Ele parece estar fora do ar. Você pode confirmar?",
        f"🤖 [{horario}] Parece que {url} está apresentando probleminhas para ser acessado. Alguém pode avisar a(o) {orgao}?",
        f"🤖 [{horario}] Oi, parece que esse site {url} possui problemas de acesso. {orgao} está sabendo disso?",
        f"🤖 [{horario}] Portais da transparência são um direito ao acesso à informação {orgao}, mas parece que {url} está fora do ar.",
        f"🤖 [{horario}] Opa {orgao}, parece que o site {url} não está acessível como deveria. O que está acontecendo?",
        f"🤖 [{horario}] Tentei acessar o site {url} e não consegui. {orgao} está acontecendo algum problema com essa portal de transparência?"
]
    msg_orgao = choice(com_orgao)
    return msg_orgao


def checar_timelines(twitter_handler, mastodon_handler, url, orgao):
    """
    Recupera os 10 últimos toots da conta do Mastodon.
    Caso a URL não esteja entre as últimas notificadas, é feita a postagem.
    Feature necessária para não floodar a timeline alheia caso um site fique offline por longos períodos de tempo.
    """

    mastodon_bot = mastodon_handler
    twitter_bot = twitter_handler
    urls_postadas = []
    timeline = mastodon_bot.timeline_home(limit=10)
    for toot in timeline:
        urls_postadas.append(toot["content"])
    contem = any(url in toot
                 for toot in urls_postadas)
    # calculo_tempo
    # se calculo_tempo > 1 hora:
    if not contem:
        mastodon_bot.toot(lista_frases(url=url, orgao=orgao))
        twitter_bot.update_status(status=lista_frases(url=url, orgao=orgao))