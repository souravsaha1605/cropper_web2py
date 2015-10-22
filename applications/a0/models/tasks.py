# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
def f():
    import time
    t = time.ctime()
    open('/tmp/tasks','w').write(t+'\n')
    return t

from gluon.scheduler import Scheduler
scheduler = Scheduler(db,dict(our_function=f))
