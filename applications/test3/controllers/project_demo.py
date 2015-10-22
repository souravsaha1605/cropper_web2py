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
    session.new = len(data)
    binary_data=a2b_base64(data)
    fd = open('image.png', 'wb')
    fd.write(binary_data)
    fd.close()
    fk = open('image.png','rb')
    im=Image.open(fk)
    (width,height)=im.size
    #pic1=im.resize(size1)
    #fd1=open('image1.png','wb')
    #draw_signature(pic1, as_file=True)
    #fd1.write(pic1)
    #fd1.close()
    #fk1=open('image1.png','rb')

    #fk.close()
    #img_size= os.stat(d).st_size   
    image_id = db.imagestore.insert(name= name_image, picture = fk )
    image_select = db(db.imagestore.id == image_id).select().first()                
    return width    
        
    


def image_upload():
    return dict()




def cropper():
    return dict()




def upload_demo():
    return dict()

def check_session():
    return session.image
