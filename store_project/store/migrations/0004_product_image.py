# Generated by Django 4.1.7 on 2023-05-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_cats'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default.jfif', upload_to='images/'),
        ),
    ]