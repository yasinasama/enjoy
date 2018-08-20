# -*- coding: utf-8 -*-

import signal


'''
time func with signal alarm
'''
def timeout_func(timeout):

    class ExecTimeoutError(Exception):
        pass

    def handler(signum,frame):
        raise TimeoutError()

    def decorate(func):
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM,handler)
            signal.alarm(timeout)
            try:
                res = func(*args, **kwargs)
            except ExecTimeoutError:
                raise
            finally:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, signal.SIG_DFL)
            return res

        return wrapper
    return decorate



if __name__=='__main__':
    @timeout_func(3)
    def add():
        import time
        while True:
            print('running')
            time.sleep(1)
    add()
