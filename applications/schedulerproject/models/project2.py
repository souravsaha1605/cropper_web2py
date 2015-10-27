# -*- coding: utf-8 -*-
db.define_table(

    'imagestore',

    Field('name'),

    Field('picture', 'upload', default=''),
    Field('picture992558', 'upload', default=''),
    Field('picture330185625', 'upload', default=''),
    Field('picture16090', 'upload', default=''),
    Field('checkfield',default='false'),
    format = '%(name)s')


db.define_table(
    'new_temp_table',
    Field('name')
    )
