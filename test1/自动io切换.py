import gevent
def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit 精确的 context内容 to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar')

def func():
    print('running func...')
    gevent.sleep(0)
    print('running func3 again')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(func),
])