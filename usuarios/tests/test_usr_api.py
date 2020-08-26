import requests


def test_cadastro_usr_post_deve_retorna201():

    payload = {"email": 'java@gmail.com', "password": 'python@123', "first_name": "usuario teste2"}
    r = requests.post('http://127.0.0.1:8000/api/usr/registra_usr/', data=payload)
    assert r.status_code == 201


def test_retonra_token_usr():
    payload = {"email": "java@gmail.com", "password": 'python@123'}
    r = requests.post('http://127.0.0.1:8000/api/usr/jwt/', data=payload)
    assert r.status_code == 200
