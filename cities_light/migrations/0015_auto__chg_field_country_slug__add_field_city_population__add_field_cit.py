# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'City', fields ['region', 'name']
        db.delete_unique('cities_light_city', ['region_id', 'name'])


        # Changing field 'Country.slug'
        db.alter_column('cities_light_country', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name_ascii'))
        # Adding field 'City.population'
        db.add_column('cities_light_city', 'population',
                      self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'City.feature_class'
        db.add_column('cities_light_city', 'feature_class',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True),
                      keep_default=False)

        # Adding field 'City.feature_code'
        db.add_column('cities_light_city', 'feature_code',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)


        # Changing field 'City.slug'
        db.alter_column('cities_light_city', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name_ascii'))
        # Adding unique constraint on 'City', fields ['feature_code', 'country', 'region', 'name', 'feature_class']
        db.create_unique('cities_light_city', ['feature_code', 'country_id', 'region_id', 'name', 'feature_class'])


        # Changing field 'Region.slug'
        db.alter_column('cities_light_region', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name_ascii'))
    def backwards(self, orm):
        # Removing unique constraint on 'City', fields ['feature_code', 'country', 'region', 'name', 'feature_class']
        db.delete_unique('cities_light_city', ['feature_code', 'country_id', 'region_id', 'name', 'feature_class'])


        # Changing field 'Country.slug'
        db.alter_column('cities_light_country', 'slug', self.gf('autoslug.fields.AutoSlugField')(max_length=50, unique_with=(), populate_from=None))
        # Deleting field 'City.population'
        db.delete_column('cities_light_city', 'population')

        # Deleting field 'City.feature_class'
        db.delete_column('cities_light_city', 'feature_class')

        # Deleting field 'City.feature_code'
        db.delete_column('cities_light_city', 'feature_code')


        # Changing field 'City.slug'
        db.alter_column('cities_light_city', 'slug', self.gf('autoslug.fields.AutoSlugField')(max_length=50, unique_with=(), populate_from=None))
        # Adding unique constraint on 'City', fields ['region', 'name']
        db.create_unique('cities_light_city', ['region_id', 'name'])


        # Changing field 'Region.slug'
        db.alter_column('cities_light_region', 'slug', self.gf('autoslug.fields.AutoSlugField')(max_length=50, unique_with=(), populate_from=None))
    models = {
        'cities_light.city': {
            'Meta': {'unique_together': "(('country', 'region', 'name', 'feature_class', 'feature_code'),)", 'object_name': 'City'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'feature_class': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'feature_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'population': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Region']", 'null': 'True', 'blank': 'True'}),
            'search_names': ('cities_light.models.ToSearchTextField', [], {'default': "''", 'max_length': '4000', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        'cities_light.country': {
            'Meta': {'object_name': 'Country'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        'cities_light.region': {
            'Meta': {'unique_together': "(('country', 'name'),)", 'object_name': 'Region'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        }
    }

    complete_apps = ['cities_light']