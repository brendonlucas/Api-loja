# Generated by Django 3.0.1 on 2019-12-31 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_auto_20191231_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]