# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-11-08 06:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0006_auto_20181105_2131'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Building',
        ),
        migrations.DeleteModel(
            name='CraftMaterial',
        ),
        migrations.DeleteModel(
            name='Effect',
        ),
        migrations.DeleteModel(
            name='EffectDetail',
        ),
        migrations.DeleteModel(
            name='Fusion',
        ),
        migrations.DeleteModel(
            name='HomunculusSkill',
        ),
        migrations.DeleteModel(
            name='HomunculusSkillCraftCost',
        ),
        migrations.DeleteModel(
            name='LeaderSkill',
        ),
        migrations.DeleteModel(
            name='Monster',
        ),
        migrations.DeleteModel(
            name='MonsterCraftCost',
        ),
        migrations.DeleteModel(
            name='ScalingStat',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
    ]
