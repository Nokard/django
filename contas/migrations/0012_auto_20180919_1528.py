# Generated by Django 2.1 on 2018-09-19 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0011_auto_20180919_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='test',
        ),
        migrations.AlterField(
            model_name='transacao',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.Categoria'),
        ),
    ]