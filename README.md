# Repositório para entrega do trabalho de microcontainers:

Alunos: Bruna Gomes e Ester Caravalho

Imagens no Docker Hub:
gomesbrunati/movies_db
gomesbrunati/movies_api
gomesbrunati/rating_api

# Passos para utilização:
Clonar o repositório atual: git clone https://github.com/GomesBruna/movies.git

Rodar o docker compose na pasta movies: docker-compose up -d

Testes possiveis nas APIs:

Movie_API:

curl localhost:5000 - retorno: "API Funcionando!"

curl localhost:5000/movies - retorno lista dos filmes na collection basics do mongo

curl localhost:5000/movies/tt0000100 - retorno o filme com o tconst tt0000100 na collection basics do mongo

curl localhost:5000/movies/rate/tt0000100 - retorna o filme e o rate que possui o tconst tt0000100

curl localhost:5001 - retorno: "API Funcionando!"

curl localhost:5001/ratings - retorno lista dos ratings na collection ratings do mongo

curl localhost:5000/ratings/tt0000100 - retorno o ratings do filme com o tconst tt0000100 na collection basics do mongo

É possivel também fazer chamada POST para inserir um filme com o body:
{
        "genres": "Documentary",
        "_id": "61062c948cd39550288ae843",
        "startYear": "1894",
        "runtimeMinutes": "1",
        "originalTitle": "Carmencita",
        "endYear": "\\N",
        "tconst": "tt0000101",
        "primaryTitle": "Carmencita",
        "titleType": "short",
        "isAdult": "0"
}

E também fazer chamada POST para inserir um rate com o body:
{
        "numVotes": "300",
        "tconst": "tt0000101",
        "averageRating": "7.7"
}

Além de deletar um filme com a chamada curl -X "DELETE" localhost:5001/movies/tt0000100

E deletar um rate com a chamada curl -X "DELETE" localhost:5001/ratings/tt0000100

Nessa pasta tem um export da collection do postman para teste da API local.
