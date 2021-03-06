import random
import requests

url_base = 'http://127.0.0.1:8000/api/cargos/cargo/'
tk = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk4NTM1NDM4LCJqdGkiOiI5M2NhYTk1MGU4ODI0ZTg1YTczYjQzMTdhMWU1YjU1NyIsInVzZXJfaWQiOjJ9.ZrnPoCMTUM3dpUIhOeA_6zcqJIl-W6x5D7IecjJvbF8'
headers={'Authorization': tk}
def test_cargo_deve_retorna_200():
    r = requests.get(url_base, headers=headers)
    assert r.status_code == 200


def test_cargo_post_deve_retorna201():
    nome = str(random.randrange(0, 10000, 20))
    payload = {"cargo": nome}
    r = requests.post(url_base, data=payload)
    assert r.status_code == 201


def test_cargo_deve_retonar_apenas_um():
    data = {'id': '1'}
    r = requests.get(url_base, params=data)
    print(r.url)
    assert r.status_code == 200


def test_cargo_deve_alterar_um_recurso():
    nome = str(random.randrange(0, 10000, 20))
    payload = {'cargo': nome}
    r = requests.patch(url_base+'2/', data=payload)
    print('url aqui')
    print(r.url)
    assert r.status_code == 200


def test_cargo_deve_alterar_um_recurso_put():
    nome = str(random.randrange(0, 10000, 20))
    payload = {'cargo': nome}
    r = requests.put(url_base+'1/', data=payload)
    print('url aqui')
    print(r.url)
    assert r.status_code == 200
