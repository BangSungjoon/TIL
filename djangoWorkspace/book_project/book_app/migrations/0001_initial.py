# Generated by Django 4.2.6 on 2023-10-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookno', models.IntegerField(blank=True, db_column='bookNo', null=True)),
                ('bookname', models.TextField(blank=True, db_column='bookName', null=True)),
                ('bookauthor', models.TextField(blank=True, db_column='bookAuthor', null=True)),
                ('bookprice', models.IntegerField(blank=True, db_column='bookPrice', null=True)),
                ('bookdate', models.TextField(blank=True, db_column='bookDate')),
                ('bookstock', models.IntegerField(blank=True, db_column='bookStock', null=True)),
                ('pubno', models.IntegerField(blank=True, db_column='pubNo', null=True)),
            ],
            options={
                'db_table': 'book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubno', models.IntegerField(blank=True, db_column='pubNo', null=True)),
                ('pubname', models.TextField(blank=True, db_column='pubName', null=True)),
            ],
            options={
                'db_table': 'publisher',
                'managed': False,
            },
        ),
    ]