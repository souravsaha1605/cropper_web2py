from binascii import a2b_base64
from PIL import Image
import os
#import cStringIO
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
    import base64
    dataList = data.split(',')
    imageString = dataList[1]
    size = len(imageString)*3/4
    session.new = [size]
    imageString.replace(" ", "+")
    session.new.append(imageString)
    imageDecode = base64.b64decode(imageString)
    #session.new.append(imageDecode)
    imageFileWrite = open(name_image, 'wb')
    imageFileWrite.write(imageDecode)
    imageFileWrite.close()
    imageFileOpen = open(name_image,'rb')
    im=Image.open(name_image)
    (width,height)=im.size
    name_image_dupli=name_image.split('.')[0]
    name_image_992558=name_image_dupli+"992*558.jpeg"
    y = db.imagestore.insert(name = name_image, picture = imageFileOpen )
    #os.remove(name_image)
    # Changing image size of the uploaded image
    imageUploaded = db(db.imagestore.id == y).select().first()
    imageURL = URL('default', 'download', args=[imageUploaded.picture],host=True)
    imageURL2=imageURL.split('.')
    imageURL3=imageURL2[5]+'.'+imageURL2[6]+'.'+imageURL2[7]
    import urllib, cStringIO
    file = cStringIO.StringIO(urllib.urlopen(imageURL).read())
    newImage = Image.open(file)
    #session.new.append(imageURL3)
    (width,height) = newImage.size
    session.new.append(width)
    size=(992,558)
    newImage.thumbnail(size,Image.ANTIALIAS) 
    newImage.save(name_image_992558,'jpeg')
    
    #imageDupliFileWrite95=open(name_image_992558, 'wb')
    #imageDupliFileWrite95.write(file_like)
    #imageDupliFileWrite95.close()
    imageDupliFileOpen=open(name_image_992558, 'rb')
    db(db.imagestore.id == y).update(picture1=imageDupliFileOpen)
    imageDupliFileOpen.close()
    return newImage


def image_upload():
    return dict()




def cropper():
    return dict()




def upload_demo():
    return dict()

def check_session():
    return session.image
