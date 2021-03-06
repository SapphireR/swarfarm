# Generated by Django 2.1.7 on 2019-06-16 04:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herders', '0005_auto_20190613_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runecraftinstance',
            name='type',
            field=models.IntegerField(choices=[(0, 'Grindstone'), (1, 'Enchant Gem'), (2, 'Immemorial Grindstone'), (3, 'Immemorial Gem'), (4, 'Ancient Grindstone'), (5, 'Ancient Gem')]),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_1_craft',
            field=models.IntegerField(blank=True, choices=[(0, 'Grindstone'), (1, 'Enchant Gem'), (2, 'Immemorial Grindstone'), (3, 'Immemorial Gem'), (4, 'Ancient Grindstone'), (5, 'Ancient Gem')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_2_craft',
            field=models.IntegerField(blank=True, choices=[(0, 'Grindstone'), (1, 'Enchant Gem'), (2, 'Immemorial Grindstone'), (3, 'Immemorial Gem'), (4, 'Ancient Grindstone'), (5, 'Ancient Gem')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_3_craft',
            field=models.IntegerField(blank=True, choices=[(0, 'Grindstone'), (1, 'Enchant Gem'), (2, 'Immemorial Grindstone'), (3, 'Immemorial Gem'), (4, 'Ancient Grindstone'), (5, 'Ancient Gem')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_4_craft',
            field=models.IntegerField(blank=True, choices=[(0, 'Grindstone'), (1, 'Enchant Gem'), (2, 'Immemorial Grindstone'), (3, 'Immemorial Gem'), (4, 'Ancient Grindstone'), (5, 'Ancient Gem')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_crafts',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, choices=[(0, 'Grindstone'), (1, 'Enchant Gem'), (2, 'Immemorial Grindstone'), (3, 'Immemorial Gem'), (4, 'Ancient Grindstone'), (5, 'Ancient Gem')], null=True), blank=True, null=True, size=4),
        ),
    ]
