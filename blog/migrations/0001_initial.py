# Generated by Django 2.0 on 2020-10-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('brief_content', models.TextField()),
                ('conTent', models.TextField()),
                ('public_Date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
