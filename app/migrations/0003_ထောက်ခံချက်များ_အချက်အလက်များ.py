# Generated by Django 3.1.5 on 2021-02-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210204_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='ထောက်ခံချက်များ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='thumbs_up')),
            ],
        ),
        migrations.CreateModel(
            name='အချက်အလက်များ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('အကြောင်းအရာ', models.CharField(max_length=255)),
                ('link', models.URLField(max_length=255)),
                ('image', models.ImageField(upload_to='data')),
            ],
        ),
    ]
