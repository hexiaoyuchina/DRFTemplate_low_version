# -*- coding: utf-8 -*-
import threading

local = threading.local()

"""

使用 local() 函数创建的变量，可以被各个线程调用，但和公共资源不同，
各个线程在使用 local() 函数创建的变量时，
都会在该线程自己的内存空间中拷贝一份。
这意味着，local() 函数创建的变量看似全局变量（可以被各个线程调用），但各线程调用的都是该变量的副本

可以这么理解，使用 threading 模块中的 local() 函数，
可以为各个线程创建完全属于它们自己的变量（又称线程局部变量）。
正是由于各个线程操作的是属于自己的变量，
该资源属于各个线程的私有资源，因此可以从根本上杜绝发生数据同步问题。

"""

def init_local():
    """初始化线程缓存变量

    :return:
    """
    local.ip = ''
    local.request_id = ''
    local.token = ''
    local.is_agent = 0
    local.language = 'zh-hans'


init_local()