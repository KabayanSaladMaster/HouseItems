# Generated by Django 3.0 on 2019-12-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frozen', '0002_auto_20191212_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frozenitem',
            name='brand',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]
