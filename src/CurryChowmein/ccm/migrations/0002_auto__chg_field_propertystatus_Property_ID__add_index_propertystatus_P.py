# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'PropertyStatus.Property_ID' to match new field type.
        db.rename_column(u'ccm_propertystatus', 'Property_ID', 'Property_ID_id')
        # Changing field 'PropertyStatus.Property_ID'
        db.alter_column(u'ccm_propertystatus', 'Property_ID_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ccm.Property']))
        # Adding index on 'PropertyStatus', fields ['Property_ID']
        db.create_index(u'ccm_propertystatus', ['Property_ID_id'])


    def backwards(self, orm):
        # Removing index on 'PropertyStatus', fields ['Property_ID']
        db.delete_index(u'ccm_propertystatus', ['Property_ID_id'])


        # Renaming column for 'PropertyStatus.Property_ID' to match new field type.
        db.rename_column(u'ccm_propertystatus', 'Property_ID_id', 'Property_ID')
        # Changing field 'PropertyStatus.Property_ID'
        db.alter_column(u'ccm_propertystatus', 'Property_ID', self.gf('django.db.models.fields.CharField')(max_length=15))

    models = {
        u'ccm.broker': {
            'Broker_Email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'Broker_ID': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'Broker_Name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Broker_Phone': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'Company_Address': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Company_City': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'Company_ID': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'Company_Name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Company_Post_Code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'Meta': {'object_name': 'Broker'}
        },
        u'ccm.property': {
            'Address': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Bathroom_Number': ('django.db.models.fields.SmallIntegerField', [], {}),
            'Bedroom_Number': ('django.db.models.fields.SmallIntegerField', [], {}),
            'Broker_ID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ccm.Broker']"}),
            'CD_Communicty_Center_F': ('django.db.models.fields.BooleanField', [], {}),
            'CD_Culture_Center_F': ('django.db.models.fields.BooleanField', [], {}),
            'CD_Garage_Flag': ('django.db.models.fields.BooleanField', [], {}),
            'CD_Highway_Flag': ('django.db.models.fields.BooleanField', [], {}),
            'CD_Metro_Flag': ('django.db.models.fields.BooleanField', [], {}),
            'CD_PARK_Hospital_Flag': ('django.db.models.fields.BooleanField', [], {}),
            'CD_School_Flag': ('django.db.models.fields.BooleanField', [], {}),
            'CD_Shopping_Mall_Flag': ('django.db.models.fields.BooleanField', [], {}),
            'City': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'Description': ('django.db.models.fields.TextField', [], {}),
            'MI_Build_In': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'MI_Build_Type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'MI_Land_Size': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'MI_Land_Size_Unit': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'MI_Municipal_Assessment': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'MI_Storeys_Number': ('django.db.models.fields.SmallIntegerField', [], {}),
            'Meta': {'object_name': 'Property'},
            'Photo_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'Post_code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'Price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'Property_ID': ('django.db.models.fields.CharField', [], {'max_length': '15', 'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'ccm.propertystatus': {
            'Meta': {'object_name': 'PropertyStatus'},
            'Offer_Flag': ('django.db.models.fields.BooleanField', [], {}),
            'Offer_date': ('django.db.models.fields.DateField', [], {}),
            'Offer_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'Property_ID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ccm.Property']"}),
            'Sold_Date': ('django.db.models.fields.DateField', [], {}),
            'Sold_Flag': ('django.db.models.fields.BooleanField', [], {}),
            'Sold_Price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['ccm']