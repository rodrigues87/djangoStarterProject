# Generated by Django 3.2.5 on 2021-08-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorreioEletronico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('origem', models.CharField(max_length=200)),
                ('correio_eletronico', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('codigo_verificador', models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
    ]