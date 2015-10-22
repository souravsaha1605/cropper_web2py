# -*- coding: utf-8 -*-
db.define_table(

    'product',

    Field('name', requires=IS_NOT_EMPTY()),

    Field('picture', 'upload', default='',requires = [IS_IMAGE(extensions=('bmp', 'gif',
                                                                'jpeg', 'png'),
                                                    maxsize=(16, 9),
                                                    minsize=(0, 0),
                                         ),IS_LENGTH(5120000, 1024)]),

    format = '%(name)s')
