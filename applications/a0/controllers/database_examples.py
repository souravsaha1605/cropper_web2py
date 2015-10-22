# -*- coding: utf-8 -*-
# try something like
def register_product():
    form = SQLFORM(db.product).process()
    if form.accepted:
        response.flash = 'new record inserted'
    return dict(form=form)
