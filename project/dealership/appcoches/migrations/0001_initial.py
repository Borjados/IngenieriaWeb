# Generated by Django 3.1.2 on 2020-11-26 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('url_categoria', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('url_marca', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75, null=True)),
                ('apellido', models.CharField(max_length=75, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('telefono', models.IntegerField(default=0, null=True)),
                ('rating', models.IntegerField(default=0, null=True)),
                ('url_vendedor', models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=250)),
                ('caballos', models.IntegerField(default=0)),
                ('puertas', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=50)),
                ('kilometros', models.IntegerField(default=0)),
                ('año', models.IntegerField(default=0)),
                ('matricula', models.CharField(max_length=50)),
                ('url_marca', models.CharField(max_length=2000)),
                ('url_coche', models.CharField(max_length=2000)),
                ('categoria', models.ManyToManyField(to='appcoches.Categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcoches.marca')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcoches.vendedor')),
            ],
        ),
    ]
