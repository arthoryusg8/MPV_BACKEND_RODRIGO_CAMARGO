# MPV_TREINAMENTO
CONTROLE DE TREINAMENTO - BACK END
# Sistema de Gerenciamento de Treinamento

Este é um aplicativo Flask simples para gerenciar treinamentos. Ele usa SQLAlchemy para interagir com um banco de dados SQLite e Flasgger para gerar uma documentação da API Swagger.

## Instalação

1. Clone este repositório.
2. Instale as dependências do projeto com os seguintes comandos:
    - `pip install Flask`
    - `pip install flask_sqlalchemy`
    - `pip install Flasgger`
3. Execute o aplicativo com `python app.py`.

## Uso

O aplicativo fornece várias rotas para interagir com o banco de dados de treinamento:

- `POST /pessoa`: Cria uma nova pessoa. O corpo da solicitação deve ser um JSON que inclui o campo `nome`.
- `DELETE /pessoa/<id>`: Deleta uma pessoa com o ID especificado.
- `POST /treinamento`: Cria um novo treinamento. O corpo da solicitação deve ser um JSON que inclui os campos `titulo` e `pessoa_id`.
- `DELETE /treinamento/<id>`: Deleta um treinamento com o ID especificado.

## Documentação da API

A documentação completa da API está disponível em `/apidocs` quando o aplicativo está em execução.

## Contribuindo

Pull requests são bem-vindos. Para mudanças importantes, abra um problema primeiro para discutir o que você gostaria de mudar.

## Licença

Rodrigo Camargo
