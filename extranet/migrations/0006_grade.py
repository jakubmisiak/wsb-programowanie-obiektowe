# Generated by Django 3.1.4 on 2020-12-05 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extranet', '0005_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(choices=[(2.0, '2.0'), (3.0, '3.0'), (3.5, '3.5'), (4.0, '4.0'), (4.5, '4.5'), (5.0, '5.0')], null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extranet.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extranet.student')),
            ],
        ),
    ]