# Generated by Django 4.1.1 on 2023-07-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.TextField()),
                ('cho1', models.TextField()),
                ('cho2', models.TextField()),
                ('cho3', models.TextField()),
                ('cho4', models.TextField()),
                ('ans', models.TextField()),
                ('exp', models.TextField()),
            ],
        ),
    ]
