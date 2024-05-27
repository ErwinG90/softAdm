# Generated by Django 4.1 on 2024-05-25 22:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0003_remove_cliente_comuna_remove_comuna_region_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_chat', models.TextField()),
                ('fecha_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', default=1, on_delete=django.db.models.deletion.CASCADE, to='adm.cliente')),
                ('id_trabajador', models.ForeignKey(db_column='id_trabajador', default=1, on_delete=django.db.models.deletion.CASCADE, to='adm.trabajador')),
            ],
            options={
                'db_table': 'chat',
            },
        ),
    ]