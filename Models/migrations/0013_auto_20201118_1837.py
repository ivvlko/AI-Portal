# Generated by Django 3.1.3 on 2020-11-18 18:37

import Models.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0012_auto_20201118_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facedetection',
            name='picture',
            field=models.ImageField(error_messages={'required': 'Please Select JPG or PNG file'}, upload_to='submitted_pictures', validators=[Models.validators.validate_pic_type]),
        ),
    ]
