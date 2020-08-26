import random
import requests
import json
url_base = 'http://127.0.0.1:8000/api/empresas/empresa/'

def test_empresa_deve_retorna_200():
    r = requests.get(url_base)
    assert r.status_code == 200


def test_empresa_post_deve_retorna201():
    nome = str(random.randrange(0, 10000, 20))
    payload = {"empresa": nome, "descricao":'Teste do TDD'}
    r = requests.post(url_base, data=payload)
    assert r.status_code == 201


def test_empresa_deve_retonar_apenas_um():
    data = {'id': '1'}
    r = requests.get(url_base, params=data)
    print(r.url)
    assert r.status_code == 200


def test_empresa_deve_alterar_um_recurso_patch():
    nome = str(random.randrange(0, 10000, 20))
    payload = {"descricao": nome}
    r = requests.patch(url_base+'1/', data=payload)
    print('url aqui')
    print(r.url)
    assert r.status_code == 200


def test_empresa_deve_alterar_um_recurso_put():
    nome = str(random.randrange(0, 10000, 20))
    payload = {"empresa": nome, "descricao": "PUT"}
    r = requests.put(url_base+'1/', data=payload)

    assert r.status_code == 200
