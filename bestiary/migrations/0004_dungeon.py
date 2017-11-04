# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-03 19:48
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


def copy_dungeons(apps, schema_editor):
    OldDungeon = apps.get_model('sw_parser', 'Dungeon')
    Dungeon = apps.get_model('bestiary', 'Dungeon')

    for dungeon in OldDungeon.objects.all():
        Dungeon.objects.create(**{f.name: getattr(dungeon, f.name, None) for f in dungeon._meta._get_fields(reverse=False)})

def uncopy_dungeons(apps, schema_editor):
    # No operations are actually required. This exists so migrating backwards doesn't raise an exception
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0003_auto_20170718_1631'),
        ('sw_parser', '0006_auto_20171023_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dungeon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.IntegerField(blank=True, choices=[(0, 'Scenarios'), (1, 'Rune Dungeons'), (2, 'Elemental Dungeons'), (3, 'Other Dungeons'), (4, 'Raids'), (5, 'Hall of Heroes')], null=True)),
                ('max_floors', models.IntegerField(default=10)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('energy_cost', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), size=None), blank=True, null=True, size=None)),
                ('xp', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), size=None), blank=True, null=True, size=None)),
                ('monster_slots', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), size=None), blank=True, null=True, size=None)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.RunPython(copy_dungeons, uncopy_dungeons)
    ]
