# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
def f():
    import time
    t = time.ctime()
    open('/tmp/scheduler','w').write(t+'\n')
    return t
def happy_birthday():
    import time
    t = time.ctime()
    open('/tmp/happy_birthday_file','w').write('today is your birhday  \n' %str)
    return t

def displaytime():
    import time
    t = time.ctime()
    open('/tmp/distime','w').write(t+'\n')
    return t

def displaymultipliply(c):
    import time
    t = time.ctime()
    c = c*3
    open('/tmp/dmultiply','w').write(c+'\n')
    return c

def generate_status():
    import random, time
    t = time.ctime()
    sentence = ['I am happy at ', 'I am sad at ', 'I am excited at ', 'I am depressed at ']
    open('/tmp/myStatus','a').write(random.choice(sentence) + t + '\n')
    return t

from gluon.scheduler import Scheduler
scheduler = Scheduler(db,dict(our_function=f,new_function=happy_birthday, status = generate_status, dtime=displaytime,dm=displaymultipliply))
