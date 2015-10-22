# -*- coding: utf-8 -*-

db.define_table(

    'imagestore',

    Field('picture', 'upload', default='',requires = [IS_IMAGE(extensions=('bmp', 'gif',
                                                                'jpeg', 'png'),
                                                    maxsize=(1600, 900),
                                                    minsize=(0, 0),
                                         ),IS_LENGTH(5120000, 1024)]),

    format = '%(name)s')
