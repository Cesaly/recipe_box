# Generated by Django 3.0.5 on 2020-06-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='likes',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
