# Generated by Django 3.1.2 on 2020-11-26 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcoches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('url_marca', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='coches',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcoches.marca'),
        ),
    ]
