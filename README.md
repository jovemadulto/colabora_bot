# Colaborabot


<a href="https://twitter.com/colaboradados"> <img src="colaboradados_twitter_logo.png" width="200"></a>

O robô que monitora o acesso aos portais de transparência pública governamentais.
Siga [**@colabora_bot**](https://twitter.com/colabora_bot)

## Instalando o bot

### No Twitter

Você deverá obter suas tokens para usar a API do Twitter: 

1. Crie sua conta normalmente, caso não a tenha. 
2. Em seguida solicite uma developer account [aqui](https://developer.twitter.com/en/apply/user). 

Hoje a requisição pode demorar dias (e há relatos de pessoas que nunca receberam). Seja o mais descritivo possível com relação ao seu projeto e fique atento aos e-mails, pois o Twitter poderá pedir informações adicionais. Também é por email que o Twitter avisará que sua requisição foi aceita. Caso isso aconteça: comemore (uhull!) e crie um app clicando [aqui](https://developer.twitter.com/en/apps). Desta forma você terá acesso as suas tokens que são: consumer_key, consumer_secret, access_token e access_token_secret.

Coloque suas tokens no arquivo `dados\env` conforme o exemplo.

### No Mastodon

1. Crie uma conta na instância de sua preferência. Nós escolhemos a [Bots in Space](https://botsin.space/about/more), mas o procedimento deve ser semelhante para qualquer outra. Certifique-se que o bot que você está configurando não irá infringir os termos de conduta da instância de sua escolha, já que as regras podem ser diferentes!

2. Registre o seu bot na instância rodando o código abaixo:

```python
from mastodon import Mastodon

Mastodon.create_app(
     'colaborabot',
     api_base_url = 'https://botsin.space',
     to_file = 'colaboradonte_clientcred.secret'
)
```

Em seguida, rode o código a seguir:

```python
from mastodon import Mastodon

mastodon = Mastodon(
    client_id = 'colaboradonte_clientcred.secret',
    api_base_url = 'https://botsin.space'
)
mastodon.log_in(
    'seu_login@servidor.com',
    'senhamuitoboaesupersegura',
    to_file = 'colaboradonte_usercred.secret'
)
```

Certifique-se de modificar os parâmetros conforme necessário.

3. Recupere as chaves criadas `pytooter_clientcred.secret` e `pytooter_usercred.secret` as insira no arquivo `credenciais\.env`

* [Documentação original](https://mastodonpy.readthedocs.io/en/stable/#) da biblioca usada para autenticação.

### Google Sheets

Para utilizar o Google Sheets, utilizamos a biblioteca [gspread](https://gspread.readthedocs.io/en/latest/) juntamente com a [Authlib](https://blog.authlib.org/2018/authlib-for-gspread) para autenticação.

1. O primeiro passo é conseguir um token de acesso de aplicação do Google Sheets. Acesse o (https://console.developers.google.com/project)[Google API Console] e crie um projeto (ou selecione um que você já tenha criado).

2. No menu do lado esquerdo, selecione "Credenciais" e clique no botão "Criar credenciais", escolhendo a opção de "Chave de conta de serviço". Escolha o formato json e salve o arquivo em seu computador.

3. Este arquivo deverá ser inserido na pasta `dados\colaborabot-gAPI.json`, assim como está descrito no programa `autenticadores.py`.

### Hora da instalação

Este código usa Python 3.7. Instale [aqui](https://www.python.org/downloads/).
Para as bibliotecas, instale todas de uma vez digitando `pip install -r requirements.txt`em seu terminal.

### Abrindo

1. Clone o repositório digitando `$ git clone https://github.com/colaboradados/colaboradadosobot` no Gitbash.
2. Vá até a pasta onde você clonou o repositório em seu computador.
3. Pronto, agora é só editar seu bot!

### Colaborando com o robô (e sendo uma pessoa muito legal)

O **Colaboradados** é uma iniciativa sem fins lucrativos e feita para comunidade e com a ajuda da mesma. Para ajudar com nossa base de dados você poderá resolver nossas issues ou editando diretamente nosso arquivo csv.

Fique atento ao fato de que nosso programa foi criado pensando no escopo nacional brasileiro, portanto seu código é - deverá ser - sempre em português, onde possível. Evite estrangeirismos e colabore para que nosso código seja estudado por todos aqueles interessados em transparência.

Nosso projeto é uma porta de entrada para que pessoas das mais diversas áreas do conhecimento se interessem com o processo tecno-cívico participativo, portanto acreditamos que o robô deve ser de fácil entendimento para aqueles que não possuem tanta familiaridade com técnicas mais avançadas de programação.

_Simples é melhor que complexo_

_Complexo é melhor que complicado_

## Créditos

Este bot foi desenvolvido por [João Ernane](https://github.com/jovemadulto), [João Purger](https://github.com/JCPurger) e [Judite Cypreste](https://juditecypreste.github.io).
Agradecimentos especiais à: [@fillipedornelas](https://github.com/fillipedornelas) e [@jfunez](https://github.com/jfunez).


## The MIT License (MIT)

Copyright (c) 2019 Judite Cypreste

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
