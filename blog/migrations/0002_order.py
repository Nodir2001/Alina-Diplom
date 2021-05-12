# Generated by Django 2.2.20 on 2021-05-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('master', models.CharField(choices=[('B1', 'Алина Биккинина'), ('B2', 'Марина Касаткина'), ('B3', 'Екатерина Колесникова'), ('B4', 'Альфина Юнусова'), ('B5', 'Аделина Илькаева'), ('B6', 'Ильвира Зорина'), ('B7', 'Анна Баникова'), ('B8', 'Валерия Хайруллина')], max_length=2)),
                ('good', models.CharField(choices=[('A1', 'Уход за ногтями'), ('A2', 'Легкий маникюр'), ('A3', 'Педикюр'), ('A4', 'Наращивание'), ('A5', 'Уходы'), ('A6', 'Педикюр + '), ('A7', 'Маникюр + гель лак')], max_length=2)),
                ('message', models.TextField()),
            ],
        ),
    ]
