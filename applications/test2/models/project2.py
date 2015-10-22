# -*- coding: utf-8 -*-
db.define_table(

    'imagestore',

    Field('name'),

    Field('picture', 'upload', default=''),

    format = '%(name)s')
