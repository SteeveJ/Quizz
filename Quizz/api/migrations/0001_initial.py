# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=200)),
                ('q_image', models.ImageField(null=True, upload_to=b'question', blank=True)),
                ('q_level', models.CharField(default=1, max_length=1, choices=[(1, b'Level 1'), (2, b'Level 2'), (3, b'Level 3')])),
                ('q_category', models.CharField(default=b'Web', max_length=15, choices=[(b'Mangas', b'Mangas'), (b'Mangas', b'Comics'), (b'Web', b'Web'), (b'Management', b'Management'), (b'Art', b'Art')])),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='a_question',
            field=models.ForeignKey(to='api.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='a_response',
            field=models.OneToOneField(related_name='response', to='api.Question'),
        ),
    ]
