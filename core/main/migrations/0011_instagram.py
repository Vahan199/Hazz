# Generated by Django 4.1 on 2022-08-28 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_aboutbg_about2_indexabout_about2"),
    ]

    operations = [
        migrations.CreateModel(
            name="Instagram",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("img", models.ImageField(upload_to="media", verbose_name="img")),
                ("img2", models.ImageField(upload_to="media", verbose_name="img2")),
                ("img3", models.ImageField(upload_to="media", verbose_name="img3")),
                ("img4", models.ImageField(upload_to="media", verbose_name="img4")),
                ("img5", models.ImageField(upload_to="media", verbose_name="img5")),
                ("img6", models.ImageField(upload_to="media", verbose_name="img6")),
            ],
            options={
                "verbose_name": "Instagram",
                "verbose_name_plural": "Instagrames",
            },
        ),
    ]