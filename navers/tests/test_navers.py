import random
import requests

url_base = 'http://127.0.0.1:8000/api/navedexs/navedex/'

def test_navedexs_deve_retorna_200():
    r = requests.get(url_base)
    assert r.status_code == 200


def test_navedexs_post_deve_retorna201():

    payload = {"id_usuario": 2, "nome": "Charles Tenorio", "data_nascimento": "1973-11-23", "sexo": "Masculino",
               "fone": "999250141"}
    r = requests.post(url_base, data=payload)
    assert r.status_code == 201


def test_navedexs_deve_retonar_apenas_um_navers():
    data = {'id': '1'}
    r = requests.get(url_base, params=data)
    print(r.url)
    assert r.status_code == 200


def test_navedexs_deve_alterar_um_campo_navers():

    payload = {'nome': 'Jose Marcelo'}
    r = requests.patch(url_base+'3/', data=payload)

    assert r.status_code == 200


def test_cargo_deve_alterar_put():
    payload = {"id_usuario": 2, "nome": "Charles Tenorio", "data_nascimento": "1973-11-23", "sexo": "Masculino",
               "fone": "999250141"}
    r = requests.put(url_base+'4/', data=payload)


    assert r.status_code == 200
