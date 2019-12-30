# Generated by Django 3.0.1 on 2019-12-27 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='telefone',
        ),
        migrations.AddField(
            model_name='compra',
            name='quantidade',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='valor_total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]