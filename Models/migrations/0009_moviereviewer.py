# Generated by Django 3.1.3 on 2020-11-15 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0008_spamfilter'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieReviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
