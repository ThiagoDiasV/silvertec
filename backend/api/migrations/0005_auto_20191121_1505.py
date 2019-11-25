# Generated by Django 2.2.7 on 2019-11-21 18:05

from django.db import migrations


def create_graphic_cards(apps, schema_editor) -> None:
    """
    Create graphic cards to populate database.
    """
    GraphicCard = apps.get_model("api", "GraphicCard")
    [
        GraphicCard(
            graphic_card_description="Gigabyte Geforce GTX 1060 6GB"
        ).save(),
        GraphicCard(graphic_card_description="PNY RTX 2060 6GB").save(),
        GraphicCard(graphic_card_description="Radeon RX 580 8GB").save(),
    ]


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_auto_20191121_1502"),
    ]

    operations = [migrations.RunPython(create_graphic_cards)]
