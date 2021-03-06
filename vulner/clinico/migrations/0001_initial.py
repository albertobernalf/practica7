# Generated by Django 3.2 on 2022-02-06 22:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosticos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cie10', models.CharField(default='', max_length=15)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=80)),
                ('fechaRegistro', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EspecialidadesMedicos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EstadosSalida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Examenes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('folio', models.IntegerField(default=0)),
                ('fecha', models.DateTimeField()),
                ('motivo', models.CharField(default='', max_length=250)),
                ('subjetivo', models.CharField(default='', max_length=250)),
                ('objetivo', models.CharField(default='', max_length=250)),
                ('analisis', models.CharField(default='', max_length=250)),
                ('plan', models.CharField(default='', max_length=250)),
                ('estado_folio', models.CharField(default='A', max_length=1)),
            ],
            options={
                'ordering': ['id_tipo_doc', 'documento', 'folio', 'fecha', 'id_especialidad', 'id_medico', 'motivo', 'subjetivo', 'objetivo', 'analisis', 'plan'],
            },
        ),
        migrations.CreateModel(
            name='HistoriaExamenes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('folio', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('cantidad', models.IntegerField()),
                ('estado_folio', models.CharField(default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaResultados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('folio', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('consecutivo', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('resultado', models.CharField(default='', max_length=500)),
                ('estado', models.CharField(default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.IntegerField(default=1)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('contacto', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TiposExamen',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
    ]
