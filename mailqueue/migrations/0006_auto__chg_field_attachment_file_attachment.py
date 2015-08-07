# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Attachment.file_attachment'
        db.alter_column('mailqueue_attachment', 'file_attachment', self.gf('django.db.models.fields.files.FileField')(max_length=1024, null=True))

    def backwards(self, orm):

        # Changing field 'Attachment.file_attachment'
        db.alter_column('mailqueue_attachment', 'file_attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

    models = {
        'mailqueue.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'email': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailqueue.MailerMessage']", 'null': 'True', 'blank': 'True'}),
            'file_attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'mailqueue.mailermessage': {
            'Meta': {'object_name': 'MailerMessage'},
            'app': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'bcc_address': ('django.db.models.fields.EmailField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'from_address': ('django.db.models.fields.EmailField', [], {'max_length': '250'}),
            'html_content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_attempt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'to_address': ('django.db.models.fields.EmailField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['mailqueue']