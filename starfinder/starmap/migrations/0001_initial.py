# Generated by Django 2.1.3 on 2018-11-25 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('area_color', models.TextField()),
                ('element_color', models.TextField()),
                ('fill_color', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.DecimalField(decimal_places=8, max_digits=32)),
                ('y', models.DecimalField(decimal_places=8, max_digits=32)),
                ('z', models.DecimalField(decimal_places=8, max_digits=32)),
                ('next', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='starmap.path')),
            ],
        ),
        migrations.CreateModel(
            name='point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.DecimalField(decimal_places=8, max_digits=32)),
                ('y', models.DecimalField(decimal_places=8, max_digits=32)),
                ('z', models.DecimalField(decimal_places=8, max_digits=32)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='starmap.collection')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='starmap.collection'),
        ),
        migrations.AddField(
            model_name='area',
            name='path_root',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='starmap.path'),
        ),
    ]
