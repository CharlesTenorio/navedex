from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()


class UsuariosSistema(object):
    def __init__(self, email):
        self.email = email
        self.tem_usr = False
        self.codigo_confere = False


    def existe_usr(self):
        usr = User.objects.filter(email=self.email).first()
        if usr:
            self.tem_usr = True
        else:
            self.tem_usr = False

        return self.tem_usr

    def verificar_codigo_indicacao(self, codigo):
        usr = User.objects.filter(email=self.email, code_indicacao=codigo).first()
        if usr:
            self.codigo_confere=True
        else:
            self.codigo_confere=False

        return self.codigo_confere

    def retorna_codigo_indicacao(self):
        usr = User.objects.filter(email=self.email).first()
        codigo =''

        if usr:
            codigo = usr.code_indicacao

        return codigo

    def add_codigo_indicao(self, codigo):
        try:
            User.objects.filter(email=self.email).update(codigo_pai=codigo)
            return True
        except Exception:
            return False

