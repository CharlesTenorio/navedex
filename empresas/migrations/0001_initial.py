# Generated by Django 3.1 on 2020-08-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50, unique=True)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]
