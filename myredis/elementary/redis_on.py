# -*- coding: utf-8 -*-
# @Time    : 18-8-31
# @Author  : ErichLee ErichLee@qq.com
# @File    : redis_on.py
# @Comment : 
#            

import redis

from util.logger_util import *


def connect():
    # 创建redis链接对象
    r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
    # 存储键值对
    r.set('site', 'www.qi.cn')
    # 获取值
    print(r.get('site'))
    # 指定decode_responses为True，表示输出为字符串
    red = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)

    # 默认redis入库编码是utf-8，如果要修改的话，需要指明 charset 和 decode_responsers 为True
    # test = myredis.StrictRedis(host='localhost', port=6379, db=0, password=None, socket_timeout=None,
    # connection_pool=None, charset='utf-8', errors='strict', decode_responses=False, unix_socket_path=None)
    red.lpush('list1', 'mongdb', 'myredis', 'mysql')
    print(r.lrange('list1', 0, -1))
    print(r.llen('list1'))


def connect_pool():
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
    # 创建链接对象
    return pool


def connect_redis():
    pool = connect_pool()
    return redis.Redis(connection_pool=pool)


def first():
    pool = connect_pool()
    r = redis.Redis(connection_pool=pool)
    # 设置集合
    r.sadd('set1', 'v1', 'v2', 'v3')
    r.sadd('set1', 'v2')
    # 显示集合的值
    print(r.smembers('set1'))

    # 使用strictRedis连接池
    rs = redis.StrictRedis(connection_pool=pool)
    # r.lpush('l1', 'python', 'memcache', 'redis', 'mongodb')
    print(r.lrange('l1', 0, -1))


def type_string():
    """
        redis中的String在在内存中按照一个name对应一个value来存储的。
        set key value [EX seconds] [PX milliseconds] [NX|XX]
        ex，过期时间（秒）
        px，过期时间（毫秒）
        nx，如果设置为True，则只有name不存在时，当前set操作才执行
        xx，如果设置为True，则只有name存在时，岗前set操作才执行
    """
    r = connect_redis()
    key = 'test'
    r.delete(key)  # 清空KEY
    if not r.get(key):
        infos('INIT KEY')

    r.set(key, 'dddddddddddd', ex=3, nx=True)  # key不存在，赋值成功，nx=True
    infos(r.get(key))

    r.set(key, 'again', nx=True)  # key存在，赋值失败 ，nx=True
    infos(r.get(key))

    r.set(key, 'third')  # key存在，赋值成功，nx=false
    infos(r.get(key))

    """
    setnx(name,value)：设置值，只有在name不存在是才执行操作

    setex(name,value,time)：设置值过期时间，单位为秒
    
    psetex(name,time_ms,value)：设置值，过期时间为毫秒
    
    mset(*args,**kwargs)：批量设置多个值
    
    get(name)：获取值
    
    getrange(key,start,end)：获取子序列,根据字节获取
    
    setrange(name,oofset,value)：修改字符串内容，从指定字符串索引开始向后替换
    """
    r.set(key, '12345', nx=True)
    r.setrange(key, 2, '8888')  # 从index=2开始修改
    infos(r.get(key))
    """
    setbit(name, offset, value)：对name对应值的二进制表示的位进行操作

    getbit(name, offset)：获取name对应的二进制位表示的值，只能是0或1
    """
    r.set(key, '12314124')
    infos('赋值字符串长度,', r.strlen(key))


def type_hash():
    """
     hget(name,key)：获取hash中的value

     hmget(name,keys,*args)：获取过个hash的key的值

     hgetall(name)：获取hash的所有键值对

     hlen(name)：获取hash中键值对的个数

     hkeys(name)：获取hash中所有keys的值

     hvals(name):获取hash中所有value的值

     hexists(name,key)：检查hash中是否存在key

     hdel(name,*key)：删除hash中的key
     """
    r = connect_redis()
    r.hset('haset', 'python', '3.5')
    infos(r.hget('haset', 'python'))
    r.hset('haset', 'redis', '1.8')
    infos(r.hgetall('haset'))


def type_list():
    """
    lpush(name,values)：在列表中添加元素，每个新元素都从左边开始添加
    lpushx(name,value)：在列表中添加元素，只有在name存在时才添加
    llen(name)：name对应的list元素的长度
    set(name,index,value)：对列表中的某个索引位的值修改
    lpop(name)：在name对应的列表的左侧获取第一个元素并删除，并返回参数的元素

    lindex(name,index)：在name对应的列表中根据索引获取列表元素

    ltrim(name,start,end)：在name对应的列表中移除start到end之间的值

    lrange(name,start,end)：列表分片获取数据

    rpoplush(src,dst):获取源列表最后一个元素的值，并将它添加到目标列表中的最左边

    blpop(keys,timeout)：将多个列表排列，按照从左到右去pop对应列表的元素

    brpoplpush(src,dst,timeout=0)：从一个列表的右侧移除一个元素并将其添加到另一个列表的左侧
    """
    r = connect_redis()
    r.lpush('l3', 1, 2)

    print(r.lrange('l3', 0, -1))
    r.lpush('l3', '88')
    print(r.lrange('l3', 0, -1))

    r.lpushx('l4', 1)
    print(r.lrange('l4', 0, -1))
    r.lpush('l4', 2)
    r.lpushx('l4', 1)
    print(r.lrange('l4', 0, -1))


def type_set():
    pass


def type_common():
    """

    delete(*name)：根据删除redis中的任意数据类型
    exists(name)：检测redis的name是否存在
    keys(pattern='*')：根据模型获取redis的name
    expire(name,time)：为某个redis的某个name设置超时时间
    rename(src, dst)：对redis的name重命名为
    move(name,db)：将redis的某个值移动到指定的db下
    randomkey()：随机获取一个redis的name（不删除）
    type(name)：获取name对应值的类型
    scan(cursor=0,match=None,count=None)：同字符串操作，用于增量迭代获取key
    scan_iter(match=None,count=None)：同字符串操作，用于增量迭代获取key

    """


type_list()
