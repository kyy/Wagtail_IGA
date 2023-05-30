# Generated by Django 4.1.7 on 2023-05-02 19:10

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='Manchester city, Redstreet str. 43-56', max_length=128, verbose_name='Адрес')),
                ('address_ico', models.CharField(blank=True, default='<i class="fa-solid fa-house"></i>', max_length=128, verbose_name='Иконка адреса')),
                ('work_time', models.CharField(blank=True, default='(mon-sut: 8:00-16:00)', max_length=128, verbose_name='Рабочее время')),
                ('work_time_ico', models.CharField(blank=True, default='<i class="fa-solid fa-clock"></i>', max_length=128, verbose_name='Иконка рабочего времени')),
                ('address_live', models.BooleanField(default=False, help_text='Включение/отключение отображения контактов и карты', verbose_name='Скрыть')),
                ('brands_live', models.BooleanField(default=False, help_text='Включение/отключение отображения социальных сетей', verbose_name='Скрыть')),
                ('map', wagtail.fields.StreamField([('map', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(default='Главный офис', label='Имя', max_length=128, required=False)), ('live', wagtail.blocks.BooleanBlock(default=False, help_text='Включение/отключение отображения карты', label='Скрыть', required=False)), ('html', wagtail.blocks.TextBlock(default='<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2416.025752575022!2d27.448263451715075!3d52.731727706084875!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sru!2sby!4v1682684391133!5m2!1sru!2sby"width="100%" height="320" style="border:0;" allowfullscreen="" loading="lazy"referrerpolicy="no-referrer-when-downgrade"></iframe>', help_text='Установите width=100% height=320', label='<HTML>', required=False))], default='[]'))], blank=True, use_json_field=True, verbose_name='Карта')),
                ('phone', wagtail.fields.StreamField([('phone', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(default='Менеджер', label='Имя', max_length=128, required=False)), ('type', wagtail.blocks.ChoiceBlock(choices=[('МТС', 'МТС'), ('A1', 'A1'), ('Life', 'Life'), ('Work', 'Work'), ('Fax', 'Fax')], label='Провайдер')), ('number', wagtail.blocks.CharBlock(default='+375 (29) 666 44 22', help_text='Пример: «+375 (29) 666 44 22»', label='Номер', max_length=32, required=True)), ('ico', wagtail.blocks.CharBlock(default='<i class="fa-solid fa-phone"></i>', label='Иконка', max_length=128, required=False)), ('live', wagtail.blocks.BooleanBlock(default=False, help_text='Включение/отключение отображения номера', label='Скрыть', required=False))], default='[]'))], blank=True, use_json_field=True, verbose_name='Телефоны')),
                ('email', wagtail.fields.StreamField([('email', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(default='Отдел маркетинга', label='Имя', max_length=128, required=False)), ('ico', wagtail.blocks.CharBlock(default='<i class="fa-solid fa-envelope"></i>', label='Иконка', max_length=128, required=False)), ('e_mail', wagtail.blocks.EmailBlock(default='minsk@mail.ru', label='e-mail', max_length=128, required=True)), ('live', wagtail.blocks.BooleanBlock(default=False, help_text='Включение/отключение отображения адреса', label='Скрыть', required=False))], default='[]'))], blank=True, use_json_field=True, verbose_name='Электронные адреса')),
                ('brands', wagtail.fields.StreamField([('brands', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(default='Имя', label='Имя', max_length=128, required=False)), ('ico', wagtail.blocks.CharBlock(default='', label='Иконка', max_length=128, required=False)), ('url', wagtail.blocks.URLBlock(default='', label='url', required=True))], default='[]'))], blank=True, use_json_field=True, verbose_name='Социальные сети')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Контакты',
            },
        ),
    ]