# Generated by Django 3.2.9 on 2021-11-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('L', 'Low'), ('H', 'High'), ('M', 'Medium')], default='L', max_length=50)),
                ('is_done', models.BooleanField(default=False)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
