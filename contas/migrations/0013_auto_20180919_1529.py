# Generated by Django 2.1 on 2018-09-19 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0012_auto_20180919_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.Categoria'),
        ),
    ]
