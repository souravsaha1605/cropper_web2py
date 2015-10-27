from binascii import a2b_base64
from PIL import Image
import os
import StringIO
def image_insert2():
    size1=(160,90)
    name_image=request.vars.name_image
    data=request.vars.file
    import base64
    dataList = data.split(',')
    imageString = dataList[1]
    size = len(imageString)*3/4
    if size < 4893970:
        session.new = [size]
        session.new.append(size)
        imageString.replace(" ", "+")
        #session.new.append(imageString)
        imageDecode = base64.b64decode(imageString)
        #session.new.append(imageDecode)
        imageFileWrite = open(name_image, 'wb')
        imageFileWrite.write(imageDecode)
        imageFileWrite.close()
        imageFileOpen = open(name_image,'rb')
        #im=Image.open(name_image)
        #(width,height)=im.size
        #name_image_dupli=name_image.split('.')[0]
        #name_image_992558=name_image_dupli+"992*558.jpg"
        y = db.imagestore.insert(name = name_image, picture = imageFileOpen )
        os.remove(name_image)
        return 'inserted'
       
    else:
        return 'Failed to insert, image greater than 5MB'


def upload_demo():
    return dict()
