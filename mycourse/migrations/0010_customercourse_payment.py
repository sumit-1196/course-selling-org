# Generated by Django 3.1.3 on 2021-01-26 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycourse', '0009_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycourse.course')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycourse.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=500)),
                ('payment_id', models.CharField(max_length=500)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycourse.course')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycourse.customer')),
                ('customer_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mycourse.customercourse')),
            ],
        ),
    ]
