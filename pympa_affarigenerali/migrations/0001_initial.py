# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pympa_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('inizio_validita', models.DateTimeField(verbose_name='Data inizio validita', default=django.utils.timezone.now)),
                ('fine_validita', models.DateTimeField(null=True, verbose_name='Data fine validita', blank=True)),
                ('delega', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Assessori',
                'verbose_name': 'Assessore',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CommissioneConsigliare',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('costo_presenza', models.PositiveSmallIntegerField(verbose_name='costo della presenza o gettone', default=0)),
                ('titolo', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Commissioni Consigliari',
                'verbose_name': 'Commissione Consigliare',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Consigliere',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('inizio_validita', models.DateTimeField(verbose_name='Data inizio validita', default=django.utils.timezone.now)),
                ('fine_validita', models.DateTimeField(null=True, verbose_name='Data fine validita', blank=True)),
                ('capogruppo', models.BooleanField(default=False)),
                ('voti', models.PositiveIntegerField(verbose_name='Numero voti', default=0)),
            ],
            options={
                'verbose_name_plural': 'Consiglieri',
                'verbose_name': 'Consigliere',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Consiglio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('costo_presenza', models.PositiveSmallIntegerField(verbose_name='costo della presenza o gettone', default=0)),
            ],
            options={
                'verbose_name_plural': 'Consigli',
                'verbose_name': 'Consiglio',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Giunta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('costo_presenza', models.PositiveSmallIntegerField(verbose_name='costo della presenza o gettone', default=0)),
            ],
            options={
                'verbose_name_plural': 'Giunte',
                'verbose_name': 'Giunta',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GruppoConsigliare',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('inizio_validita', models.DateTimeField(verbose_name='Data inizio validita', default=django.utils.timezone.now)),
                ('fine_validita', models.DateTimeField(null=True, verbose_name='Data fine validita', blank=True)),
                ('titolo', models.CharField(max_length=200)),
                ('voti', models.PositiveIntegerField(editable=False, verbose_name='Numero voti', default=0)),
            ],
            options={
                'verbose_name_plural': 'Gruppo Consigliari',
                'verbose_name': 'Gruppo Consigliare',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mandato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('inizio_validita', models.DateTimeField(verbose_name='Data inizio validita', default=django.utils.timezone.now)),
                ('fine_validita', models.DateTimeField(null=True, verbose_name='Data fine validita', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Mandati',
                'verbose_name': 'Mandato',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('inizio_validita', models.DateTimeField(verbose_name='Data inizio validita', default=django.utils.timezone.now)),
                ('fine_validita', models.DateTimeField(null=True, verbose_name='Data fine validita', blank=True)),
                ('cognome', models.CharField(max_length=80, verbose_name='Cognome')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('ente', models.ForeignKey(to='pympa_core.Ente', blank=True, null=True)),
                ('user', models.OneToOneField(null=True, verbose_name='Utente del sistema', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Persone',
                'verbose_name': 'Persona',
                'ordering': ('cognome', 'nome'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Presenza',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('presenza', models.BooleanField(default=False)),
                ('persona', models.ForeignKey(to='pympa_affarigenerali.Persona')),
            ],
            options={
                'verbose_name_plural': 'Presenze',
                'verbose_name': 'Presenza',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SessioneAssemblea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('data_svolgimento', models.DateField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'Sessioni Assemblea',
                'verbose_name': 'Sessione Assemblea',
                'ordering': ('data_svolgimento',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='sessioneassemblea',
            unique_together=set([('data_svolgimento', 'object_id', 'content_type')]),
        ),
        migrations.AddField(
            model_name='presenza',
            name='sessione',
            field=models.ForeignKey(related_name='presenze', to='pympa_affarigenerali.SessioneAssemblea'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='presenza',
            unique_together=set([('sessione', 'persona')]),
        ),
        migrations.AddField(
            model_name='mandato',
            name='boss',
            field=models.OneToOneField(null=True, verbose_name="Sindaco o Presidente dell'unione", to='pympa_affarigenerali.Persona', related_name='boss_mandato', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mandato',
            name='ente',
            field=models.ForeignKey(to='pympa_core.Ente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mandato',
            name='speacker',
            field=models.OneToOneField(null=True, verbose_name='Presidente del consiglio', to='pympa_affarigenerali.Persona', related_name='speacker_mandato', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mandato',
            name='vice',
            field=models.OneToOneField(null=True, verbose_name="Vicesindaco o Vicepresidente  dell'unione", to='pympa_affarigenerali.Persona', related_name='vice_mandato', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mandato',
            name='vice_speacker',
            field=models.OneToOneField(null=True, verbose_name='Vicepresidente del consiglio', to='pympa_affarigenerali.Persona', related_name='vicespeacker_mandato', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gruppoconsigliare',
            name='mandato',
            field=models.ForeignKey(to='pympa_affarigenerali.Mandato'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='giunta',
            name='mandato',
            field=models.OneToOneField(to='pympa_affarigenerali.Mandato'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consiglio',
            name='mandato',
            field=models.OneToOneField(to='pympa_affarigenerali.Mandato'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consigliere',
            name='gruppoconsigliare',
            field=models.ForeignKey(to='pympa_affarigenerali.GruppoConsigliare', related_name='consiglieri', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consigliere',
            name='mandato',
            field=models.ForeignKey(related_name='consiglieri', to='pympa_affarigenerali.Mandato'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consigliere',
            name='persona',
            field=models.ForeignKey(to='pympa_affarigenerali.Persona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commissioneconsigliare',
            name='boss',
            field=models.OneToOneField(null=True, verbose_name='Presidente della commissione', to='pympa_affarigenerali.Consigliere', related_name='boss_commissione', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commissioneconsigliare',
            name='consiglieri',
            field=models.ManyToManyField(to='pympa_affarigenerali.Consigliere', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commissioneconsigliare',
            name='mandato',
            field=models.ForeignKey(related_name='commissioniconsigliari', to='pympa_affarigenerali.Mandato'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commissioneconsigliare',
            name='vice',
            field=models.OneToOneField(null=True, verbose_name='Vicepresidente della commissione', to='pympa_affarigenerali.Consigliere', related_name='vice_commisione', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessore',
            name='mandato',
            field=models.ForeignKey(related_name='assessori', to='pympa_affarigenerali.Mandato'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessore',
            name='persona',
            field=models.OneToOneField(to='pympa_affarigenerali.Persona'),
            preserve_default=True,
        ),
    ]
