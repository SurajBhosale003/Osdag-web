# Generated by Django 3.2.19 on 2023-06-08 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osdag', '0009_alter_equalangle_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equalangle',
            name='Zpy',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='equalangle',
            name='Zpz',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='equalangle',
            name='Zy',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='equalangle',
            name='Zz',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='equalangle',
            name='ru_max',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='equalangle',
            name='rv_min',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='equalangle',
            name='ry',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='equalangle',
            name='rz',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]