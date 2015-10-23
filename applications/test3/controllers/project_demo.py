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
    x = session.new
    return locals()

def image_insert2():
    size1=(160,90)
    name_image=request.vars.name_image
    data=request.vars.file
    try:
        import base64
        dataList = data.split(',')
        imageString = dataList[1]
        size = len(imageString)*3/4
        session.new = [size]
        imageString.replace(" ", "+")
        session.new.append(imageString)
        imageDecode = base64.b64decode(imageString)
        session.new.append(imageDecode)
        imageFileWrite = open(name_image, 'wb')
        imageFileWrite.write(imageDecode)
        imageFileWrite.close()
        imageFileOpen = open(name_image,'rb')
        im=Image.open(name_image)
        (width,height)=im.size
        y = db.imagestore.insert(name = name_image, picture = imageFileOpen)
        os.remove(name_image)
    except:
        os.remove(name_image)
    return ''


def image_upload():
    return dict()




def cropper():
    return dict()




def upload_demo():
    return dict()

def check_session():
    return session.image
