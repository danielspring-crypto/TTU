# Generated by Django 3.1.5 on 2021-02-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ပုဒ်မ', models.CharField(max_length=255)),
                ('အကြောင်းအရာ', models.TextField()),
                ('ကျူးလွန်သည့်အကြောင်းအရာ', models.TextField()),
            ],
        ),
    ]