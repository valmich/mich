# Generated by Django 3.0 on 2021-03-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informatica', '0008_auto_20210308_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computador',
            name='software',
            field=models.ManyToManyField(blank=True, to='informatica.SoftwareOutro'),
        ),
    ]
