# Generated by Django 3.2 on 2022-02-06 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sitios', '0001_initial'),
        ('admisiones', '0001_initial'),
        ('usuarios', '0001_initial'),
        ('planta', '0001_initial'),
        ('clinico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresos',
            name='dependenciasActual',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id1', to='sitios.dependencias'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='dependenciasIngreso',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id0', to='sitios.dependencias'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='dependenciasSalida',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id2', to='sitios.dependencias'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='documento',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Documento', to='usuarios.usuarios'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='dxActual',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id4', to='clinico.diagnosticos'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='dxIngreso',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id3', to='clinico.diagnosticos'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='dxSalida',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id5', to='clinico.diagnosticos'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='estadoSalida',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.estadossalida'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='medicoActual',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id7', to='planta.planta'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='medicoIngreso',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id6', to='planta.planta'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='medicoSalida',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id8', to='planta.planta'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='sedesClinica',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='SedesClinica', to='sitios.sedesclinica'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='tipoDoc',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.tiposdocumento'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='usuarioRegistro',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.planta'),
        ),
    ]
