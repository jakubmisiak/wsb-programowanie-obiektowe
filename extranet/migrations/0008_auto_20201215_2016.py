# Generated by Django 3.1.4 on 2020-12-15 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extranet', '0007_auto_20201208_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='index',
            field=models.CharField(db_index=True, max_length=5),
        ),
    ]