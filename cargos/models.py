from django.db import models

class Cargo(models.Model):
    cargo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.cargo
