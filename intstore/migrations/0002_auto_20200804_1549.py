# Generated by Django 3.0.3 on 2020-08-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(db_index=True, max_length=40, verbose_name='Название'),
        ),
    ]
