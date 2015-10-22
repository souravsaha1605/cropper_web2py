from binascii import a2b_base64
def image_insert():
    name_image=request.vars.name_image
    image_var=request.vars.file
    db.imagestore.insert(name= name_image, picture = image_var)
    return "hello"

def image_insert2():
    #name_image=request.vars.name_image
    data=request.vars.file
    form = SQLFORM(db.imagestore).process()
    try:
        binary_data=a2b_base64(data)
        fd = open('image.png', 'wb')
        fd.write(binary_data)
        fd.close()
        fk = open('image.png','rb')
        if len(name) > 0:
            image_id = db.imagestore.insert(picture = fk)
            image_select = db(db.imagestore.id == image_id).select().first()
        else:
            return ''
    except :
        return ''
    return URL('default','download',args=[image_select.picture])


def image_upload():
    return dict()




def cropper():
    return dict()




def upload_demo():
    form = SQLFORM(db.imagestore).process()
    return dict(form=form)

def check_session():
    return session.image
