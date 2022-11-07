## Como instalar e iniciar

#### Exemplo:  

Para executar essa aplicação você deverá ter instalado o Python (3.10.x).

Instalação:

`pip install fastapi`
`pip install "uvicorn[standard]"`

Inicialização:

`python -m uvicorn main:app --reload`  

Rotas:

*GET: Retorna itens cadastrados*
`localhost:8000/api/v1/items` 

*POST: Cadastra um novo item*
`localhost:8000/api/v1/items` 

*JSON de cadastro*
```json
    {
        "name": ""
    }
```