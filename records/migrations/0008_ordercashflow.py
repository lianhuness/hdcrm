# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-11 15:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('records', '0007_orderdeliver'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCashFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField()),
                ('currency', models.CharField(choices=[(b'USD', '\u7f8e\u91d1'), (b'RMB', '\u4eba\u6c11\u5e01')], default=b'RMB', max_length=10)),
                ('account', models.CharField(choices=[(b'CON_US', '\u5efa\u884c-\u7f8e\u91d1'), (b'CON_RMB', '\u5efa\u884c-\u4eba\u6c11\u5e01'), (b'WESTUNION', '\u897f\u8054'), (b'ALIBABA_US', '\u963f\u91cc\u5df4\u5df4-\u7f8e\u91d1'), (b'ALIBABA_RMB', '\u963f\u91cc\u5df4\u5df4-\u4eba\u6c11\u5e01'), (b'PAYPAL1', '\u8d1d\u5b9d-lianhuness@gmail.com'), (b'PAYPAL2', '\u8d1d\u5b9d-yiqizhu@hongdalatex.com'), (b'ZENRONGMEI', '\u66fe-\u519c\u884c')], default=b'CON_RMB', max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('note', models.TextField()),
                ('payto', models.CharField(blank=True, max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
