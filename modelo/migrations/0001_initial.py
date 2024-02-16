# Generated by Django 5.0.2 on 2024-02-13 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=19)),
            ],
        ),
        migrations.CreateModel(
            name='Filho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('dta_nasc', models.DateField(verbose_name='data de nascimento')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='modelo.pessoa')),
            ],
        ),
    ]
