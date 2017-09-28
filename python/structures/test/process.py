from multiprocessing.context import Process
import os

def show_info_on(a_topic):
    ''' Postconditions:
    1. a_topic is on the monitor
    2. The name of the module executing this is on the monitor
    3. If available, the ID of the process parent to this is on the monitor
    4. The ID of the process executing this is on the monitor
    '''
    print('Information on ' + a_topic)  # 1.
    print('Name of module executing this: ', __name__)  # 2.
    if hasattr(os, 'getppid'):  # 3: if available on this OS
        print('Parent process: ', os.getppid())
    print('ID of process executing this: ', os.getpid(), '\n')  # 4.

def say_hello(name):
    ''' Postconditions:
    1. = Postconditions of get_info_on('Say-hello process')
    2. "Hello <name>" is on the monitor
    '''
    show_info_on('Say-hello process')
    print('Hello ', name)

if __name__ == '__main__':
    ''' Postconditions:
    1. = Postconditions of get_info_on (this) main process
    2. = Postconditions of get_info_on a new process executing say_hello('Hugh Person')
    '''
    show_info_on('main line')
    p = Process(target=say_hello, args=('Hugh Person',))
    p.start()
    p.join()