from binascii import a2b_base64
from PIL import Image
import os
import StringIO
def image_insert():
    name_image=request.vars.name_image
    image_var=request.vars.file
    db.imagestore.insert(name= name_image, picture = image_var)
    return "hello"

def new():
    return session.new

def image_insert2():
    size1=(160,90)
    name_image=request.vars.name_image
    data=request.vars.file
    session.new = data
    return 1


def image_upload():
    return dict()




def cropper():
    return dict()




def upload_demo():
    return dict()

def check_session():
    return session.image
