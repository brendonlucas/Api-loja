# Generated by Django 3.0.1 on 2020-01-02 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_auto_20191231_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.CharField(default='sem descrição', max_length=300),
            preserve_default=False,
        ),
    ]