# Generated by Django 2.1.7 on 2019-05-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('departamento', models.CharField(max_length=512)),
                ('uds', models.IntegerField()),
            ],
        ),
    ]
