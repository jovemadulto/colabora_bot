
def retorna_status():

    from db import get_status

    data = get_status('','Google','','')
    return data
def update_status(status_id):
    from db import update_status

    atualiza = update_status(status_id)

status = retorna_status()

for linha in status:    
    #imagina que eu estou tweetando aqui nesse print lindo
    print(f'id {linha.id} Url: {linha.url}, orgao: {linha.orgao}')
    #aqui nesse update eu atualizo ele com o código 1 pra dizer que já foi postado
    update_status(linha.id)

    #coloca um tratamento, se for vazio não chamar o update, tweet, print... etc

