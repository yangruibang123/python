# Generated by Django 2.1.7 on 2019-04-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='douban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myranking', models.CharField(max_length=255)),
                ('myimg', models.CharField(max_length=255)),
                ('mytitle', models.CharField(max_length=255)),
                ('mydirector', models.CharField(max_length=255)),
                ('mystar', models.CharField(max_length=255)),
                ('mytime', models.CharField(max_length=255)),
                ('myadress', models.CharField(max_length=255)),
                ('mymovie_type', models.CharField(max_length=255)),
                ('myscore', models.CharField(max_length=255)),
                ('mynumber', models.CharField(max_length=255)),
                ('myevaluate', models.CharField(max_length=255)),
            ],
        ),
    ]
