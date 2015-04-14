# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Property'
        db.create_table(u'ccm_property', (
            ('Property_ID', self.gf('django.db.models.fields.CharField')(max_length=15, primary_key=True)),
            ('Price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('Bedroom_Number', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('Bathroom_Number', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('Address', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('City', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('Post_code', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('Description', self.gf('django.db.models.fields.TextField')()),
            ('Photo_link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('MI_Build_Type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('MI_Land_Size', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('MI_Land_Size_Unit', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('MI_Build_In', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('MI_Storeys_Number', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('MI_Municipal_Assessment', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('CD_Garage_Flag', self.gf('django.db.models.fields.BooleanField')()),
            ('CD_Metro_Flag', self.gf('django.db.models.fields.BooleanField')()),
            ('CD_Highway_Flag', self.gf('django.db.models.fields.BooleanField')()),
            ('CD_Communicty_Center_F', self.gf('django.db.models.fields.BooleanField')()),
            ('CD_Culture_Center_F', self.gf('django.db.models.fields.BooleanField')()),
            ('CD_Shopping_Mall_Flag', self.gf('django.db.models.fields.BooleanField')()),
            ('CD_PARK_Hospital_Flag', self.gf('django.db.models.fields.BooleanField')()),
            ('CD_School_Flag', self.gf('django.db.models.fields.BooleanField')()),
            ('Broker_ID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ccm.Broker'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'ccm', ['Property'])

        # Adding model 'Broker'
        db.create_table(u'ccm_broker', (
            ('Broker_ID', self.gf('django.db.models.fields.CharField')(max_length=8, primary_key=True)),
            ('Company_ID', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('Company_Name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Broker_Name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Company_Address', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Company_City', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('Company_Post_Code', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('Broker_Phone', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('Broker_Email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
        ))
        db.send_create_signal(u'ccm', ['Broker'])

        # Adding model 'PropertyStatus'
        db.create_table(u'ccm_propertystatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Property_ID', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('Offer_Flag', self.gf('django.db.models.fields.BooleanField')()),
            ('Offer_date', self.gf('django.db.models.fields.DateField')()),
            ('Offer_price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('Sold_Flag', self.gf('django.db.models.fields.BooleanField')()),
            ('Sold_Date', self.gf('django.db.models.fields.DateField')()),
            ('Sold_Price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
        ))
        db.send_create_signal(u'ccm', ['PropertyStatus'])


    def backwards(self, orm):
        # Deleting model 'Property'
        db.delete_table(u'ccm_property')

        # Deleting model 'Broker'
        db.delete_table(u'ccm_broker')

        # Deleting model 'PropertyStatus'
        db.delete_table(u'ccm_propertystatus')


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
            'Property_ID': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'Sold_Date': ('django.db.models.fields.DateField', [], {}),
            'Sold_Flag': ('django.db.models.fields.BooleanField', [], {}),
            'Sold_Price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['ccm']