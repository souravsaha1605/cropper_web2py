# -*- coding: utf-8 -*-
def happy_birthday():
    import time
    t = time.ctime()
    open('/tmp/happy_birthday_file','w').write('today is your birhday  \n' %str)
    return t
def generate_status():
    import random, time
    t = time.ctime()
    sentence = ['I am happy at ', 'I am sad at ', 'I am excited at ', 'I am depressed at ']
    open('/tmp/myStatus','a').write(random.choice(sentence) + t + '\n')
    db.new_temp_table.insert(name=random.choice(sentence))
    db.commit()
    return t

def reimagetres():
    import time
    from PIL import Image
    import urllib, cStringIO
    import os
    t = time.ctime()
    imageUploaded = db(db.imagestore.checkfield.like('false')).select().first()
    name_image_dupli=imageUploaded.name.split(',')[0]
    name_image_992558=name_image_dupli+"992*558.jpeg"
    open('/tmp/myPictureget2','a').write(name_image_992558 + t + '\n')
    imageURL = URL('default', 'download', args=[imageUploaded.picture],host=True)
    file = cStringIO.StringIO(urllib.urlopen(imageURL).read())
    newImage = Image.open(file)
    size=(992,558)
    newImage.thumbnail(size,Image.ANTIALIAS) 
    newImage.save(name_image_992558,'jpeg')
    imageDupliFileOpen=open(name_image_992558, 'rb')
    #db.imagestore.insert(name = imageUploaded.name, picture = imageDupliFileOpen)
    db(db.imagestore.id == imageUploaded.id).update(picture992558=imageDupliFileOpen)
    imageDupliFileOpen.close()
    os.remove(name_image_992558)
    db(db.imagestore.id == imageUploaded.id).update(checkfield='True')
    db.commit()
    return imageUploaded.id
from gluon.scheduler import Scheduler
scheduler = Scheduler(db,dict(our_function=happy_birthday, status = generate_status, gimagetrs = reimagetres))