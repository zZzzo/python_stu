# -*- coding: utf-8 -*-
#https://github.com/lijin-THU/notes-python

def main():
    print('*' * 10 + 'Hello World!' + '*' * 10)
    print('Demo -- 中文测试')

    #simple_function_if(20, 20)
    #simple_function_for()
    #simple_function_list()
    #simple_function_slice()
    #simple_function_tuple()     #元组的生成速度会比列表快很多，迭代速度快一点，索引速度差不多。
    #simple_function_dictionary()
    simple_function_set()


def simple_function_set():
    '''
        集合 set 是一种无序的序列
        唯一性：因为集合是无序的，所以当集合中存在两个同样的元素的时候，Python只会保存其中的一个
        确定性：同时为了确保其中不包含同样的元素，集合中放入的元素只能是不可变的对象
        #1、生成集合
        #2、集合操作
        #3、集合方法
    '''
    print('[simple_function_set]: into function')
#1、 生成集合    (set / )
    print('[simple_function_set]: 1、生成集合')
#1.1 set()生成
    a = set()
    a = set([1, 2, 3, 4, 2])    # 集合会自动去掉重复元素
    print(a)    #集合的符号也是{}和 字典相同，所以创建空集合的时候只能调用set()来创建
    a = {}  #这样是创建空字典
    a = set()   #创建空集合
    print('=' * 60)

#2、集合操作 (  并集 union() 或者 |  /  交集 intersection 或者 &
    #           差 difference 或者 a-b / 对称差集 返回除a和b的交集以外的元素 symmetric_difference 或者 a ^ b
    #           包含关系： a.issubset(b) 或者 a <= b)
    print('[simple_function_set]: 2、集合操作')
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    c = a | b
    d = a.union(b)
    e = b.union(a)
    print('并集( | ) ：' + str(c))
    print('并集(union) ：' + str(d))
    print('并集(union) ：' + str(e))

    c = a.intersection(b)
    d = a & b
    print('并集( intersection ) ：' + str(c))
    print('并集( & ) ：' + str(d))

    c = a.difference(b)
    d = a - b
    e = b - a
    print('差( difference ) ：' + str(c))
    print('差( a - b ) ：' + str(d))
    print('差( b - a ) ：' + str(e))

    c = a.symmetric_difference(b)
    d = a ^ b
    e = b ^ a
    print('对称差( symmetric_difference ) ：' + str(c))
    print('对称差( a ^ b ) ：' + str(d))
    print('对称差( b ^ a ) ：' + str(e))

    #判断包含关系
    a = {1, 2, 3}
    b = {1, 2}
    print('判断b是不是a的子集( b <= a) ：'+ str(b <= a))
    print('判断b是不是a的子集( b.issubset(a)) ：' + str(b.issubset(a)))

    print('判断a是不是b的父集( a >= b) ：'+ str(a >= b))
    print('判断a是不是b的父集( a.issuperset(a)) ：' + str(a.issuperset(b)))

#3、集合方法 ()
    print('[simple_function_set]: 3、集合方法')
    print('[simple_function_set]: add 添加单个元素')
    t = {1, 2, 3}
    t.add(5)
    print('添加元素 5 ： ' + str(t))

    print('[simple_function_set]: update 添加多个元素')
    t.update([4, 5, 6, 7])
    print('添加[4, 5, 6, 7]：' + str(t))

    print('[simple_function_set]: remove 移除单个元素')
    t.remove(1)
    print('移除元素 1 ：' + str(t))

    print('[simple_function_set]: pop删除并返回集合中任意一个元素')
    print('pop 删除任意一个元素： ' + str(t.pop()))
    print('调用pop后的集合： ' + str(t))       # 当集合为空时， 调用pop会出错

    #discard作用与 remove 一样，但是当元素在集合中不存在的时候不会报错
    print('[simple_function_set]: discard 移除单个元素,若无该元素，不会报错')

    #difference_update 从a 中 去除所有属于b的元素


def simple_function_dictionary():
    '''
        字典是另一种可变容器模型，且可存储任意类型对象。
        字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割。
        键必须是唯一的，但值不必
        #1、字典初始化
        #2、字典方法
    '''
    print('[simple_function_dictionary]: into fucntion')

# 1、字典初始化   ( 通过索引 / 通过dict初始化 )
    print('[simple_function_dictionary]: 1、字典初始化')
    aDict = {'one':'this is one', 2:'this is 2',}
    print(aDict)
    bDict = {}
    print('[simple_function_dictionary]: 通过索引来插入键值，也可通过索引查找键值')
    bDict['two'] = 'this is two'
    print('\'tow\'键对应的值：' + bDict['two'])
    print('[simple_function_dictionary]: 使用dict()初始化字典')
    eDict = dict(
        [('first', 12),
         ('second', 34),
         ('third', 56)])
    print(eDict)
    print('=' * 60)

#2、字典方法 ( 通过get()获取对应的值 / 通过pop删除并弹出对应的值 / 通过del删除指定的键值对 / 通过update()方法更新字典
    #          in 查询是否有这个键 / keys 返回一个由所有键组成的列表 / values 返回所有值组成的列表 / items 返回所有键值对元组组成的列表)
    print('[simple_function_dictionary]: 2、字典方法')
    fDict = {}
    fDict['1'] = 'one'
    fDict['2'] = 'two'
    fDict['3'] = 'three'
    fDict['4'] = 'four'
    print('[simple_function_dictionary]: get()获取对应的值')
    print('没有这个键时返回(None)：' + str(fDict.get(1)))
    print('正确时返回： ' + str(fDict.get('1')))

    print('[simple_function_dictionary]: pop()删除并返回这个键对应的值')
    print('弹出：' + str(fDict.pop('3')))
    print('弹出后的字典：' + str(fDict))
    print('弹出不存在的键：' + str(fDict.pop('55', 'not exist')))   #这里跟上面的get()不同，get默认返回None，而pop不会默认返回，必须指定

    print('[simple_function_dictionary]: del 删除键值对')
    del fDict['1']
    print('执行del fDict[\'1\'] 结果：' + str(fDict))
    #del fDict['11']    #del 不能删除没有的键(会报错)

    print('[simple_function_dictionary]: update 更新字典')
    person = dict(
        [('first', 'XiaoMing'),
         ('second', 'Jmes')]
        )
    print('更改前： ' + str(person))
    person_modify = {'second':'James', 'Third': 'Huan'}
    person.update(person_modify)
    print('更改后： ' + str(person))
    print('[simple_function_dictionary]: in 判断字典中有没有这个键')
    print('huanhuan' in person)

    print('[simple_function_dictionary]: keys 返回所有键的列表:', end = ' ')
    print(person.keys())
    print('[simple_function_dictionary]: values 返回所有值的列表:', end = ' ')
    print(person.values())
    print('[simple_function_dictionary]: items 返回所有键值对元组组成的列表:', end = ' ')
    print(person.items())
    print('=' * 60)

def simple_function_tuple():
    '''
    与列表相似，元组Tuple也是个有序序列，但是元组是不可变的，用()生成。
    1、基本操作和列表类似，但是不可变。
    2、单个元素的元组生成
    3、元组的方法
    4、元组用在：字典中当作键 / 数据库的返回值
    '''
    print('[simple_function_tuple]: into funciton')
    print('[simple_function_tuple]: 1 基本操作')
    t = (3, 4, 5, 6, 7)
    print('[simple_function_tuple]: 可索引: ' + str(t[1]))
    print('[simple_function_tuple]: 可切片: ' + str(t[1:3]))
    #t[0] = 1   #不可更改
    print('[simple_function_tuple]: 不可更改: ' + str(t[0]))
    print('=' * 60)
    print('[simple_function_tuple]: 2 单个元组生成: ')
    t_only = (223, )    #由于()在表达式中被应用，只含有单个元素的元组容易和表达式混淆.所以要加个逗号
    print(t_only)
    print(type(t_only))
    print('=' * 60)
    print('[simple_function_tuple]: 3 元组的方法: ')
    print('[simple_function_tuple]: 列表转换为元组(返回元组对象) tuple(列表对象): ')
    a = [10, 11, 13 ,15]
    print(tuple(a))
    print('[simple_function_tuple]: 元组转换为列表(返回列表对象) list(元组对象): ')
    b = (11, 13, 15 ,17)
    c = list(b)
    print(c)
    print(type(b))
    print('[simple_function_tuple]: 只能使用一些不改变元素的方法 index 查元素位置/ 查元素个数 : ')
    d = (10, 11, 12 ,13 ,14, 15 ,10 ,10, 10)
    print('count方法: ' + str(d.count(10)))
    print('index方法: ' + str(d.index(15)))

    print('=' *60)

def simple_function_slice():
    '''
    第一个数字表示切片开始位置（默认为0）。
    第二个数字表示切片截止（但不包含）位置（默认为列表长度）。
    第三个数字表示切片的步长（默认为1），当步长省略时可以顺便省略最后一个冒号
    切片操作不会因为下标越界而抛出异常，而是简单地在列表尾部截断或者返回一个空列表
    '''
    print('[simple_function_slice]: into function')
    lst = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print('[simple_function_slice]: [::]返回包含所有元素的新列表', end = ' ')
    alst = lst[::]
    print(alst)

    print('[simple_function_slice]: [::-1]逆序所有元素', end=' ')
    blst = lst[::-1]
    print(blst)

    print('[simple_function_slice]: [3,6]下标在[3,6)的元素', end=' ')
    clst = lst[3:6]
    print(clst)

    print('[simple_function_slice]: [:100]前100个元素,自动截断', end=' ')
    dlst = lst[:100]
    print(dlst)

    print('[simple_function_slice]: 替换前3个元素', end=' ')
    lst[:3] = [1, 2, 3]
    print(lst)

    print('[simple_function_slice]: 删除前3个元素', end=' ')
    lst[:3] = []
    print(lst)

    print('[simple_function_slice]: 替换偶数位置上的元素', end=' ')
    lst[::2] = ['偶数位置'] * (len(lst)//2 + 1)     # a/b 得到浮点数  a//b得到整数部分
    print(lst)

    '''
        切片返回的是列表元素的浅复制，也就是列表元素一样，但是不是同一个对象，内存地址也不同。
        深复制就是 将 blist = alist 。
        但是对于元素中 包含 列表之类的可变数据类型，浅复制时只是将子列表的引用复制过来，这样的话，修改一个会影响另一个。
    '''
    print('[simple_function_slice]: 切片返回的是列表元素的浅复制')
    print('1 == > 复制：')
    aList = [3, 5, 7]
    bList = aList
    bList[1] = 8
    print(aList)
    print('[simple_function_slice]: aList 和 bList是同一个对象，内存地址相同', end=' ')
    print(aList == bList)   #2个列表的元素完全相同
    print(aList is bList)   #2个列表是同一个对象
    print('aList的内存地址：', end = ' ')
    print(id(aList))
    print('bList的内存地址：', end = ' ')
    print(id(bList))

    print('2 == > 切片复制：')
    cList = [2, 3, 4]
    dList = cList[:]
    print(dList)
    print('[simple_function_slice]: cList 和 dList不是同一个对象，内存地址不相同', end=' ')
    print(cList == dList)  # 2个列表的元素完全相同
    print(cList is dList)  # 2个列表不是同一个对象
    print('cList的内存地址：', end=' ')
    print(id(cList))
    print('dList的内存地址：', end=' ')
    print(id(dList))
    '''
        如果源列表中包含除列表外的不可变类型的数据，切片复制后互相不会影响
        如果原列表中包含列表之类的可变数据类型，由于浅复制时只是把子列表的引用复制到新列表中，这样的话修改任何一个都会影响另外一个
    '''
    xList = [1, 2, [3,4]]
    y = xList[:]
    xList[1] = 20       #不会影响到y
    xList[2].append(5)  #会影响到y
    print(y)    

def simple_function_list():     #列表：一个有序序列
    print('[simple_function_list]: into function')
    '''
    #1、向列表添加新元素
    #2、删减列表中的元素
    #3、获取列表里的特定元素
    #4、成员资格判断
    #5、列表分片 
    #6、列表排序
    #6、常用的列表操作符
    #7、其他常见列表操作函数
    #8、列表拷贝
    '''
#1、向列表添加新元素{ append() / extend() / insert() / 乘法拓展列表}
    print('[simple_function_list]: 1：向列表添加新元素')
    m = [1]
    m.append('hello')   #只能添加一个元素在列表末尾
    print('[simple_function_list]:', end=' ')
    print(m)
    m.extend([2, 'world', 3.001, 'python'])  #能添加多个元素到列表末尾
    print('[simple_function_list]:', end=' ')
    print(m)
    m.insert(2, [2.1, 2.2]) #在特定位置添加某元素(可以是列表也可以是值)
    m.insert(3, 2.5)
    print('[simple_function_list]:', end=' ')
    print(m)

    m1 = [[None] * 2] * 3
    print('[simple_function_list]: 乘法拓展列表', end=' ')
    print(m1)
    m1[0][0] = 5
    print('[simple_function_list]: 乘法拓展列表', end=' ')
    print(m1)
    print('[simple_function_list]: 乘法拓展列表: 使用 * 运算符将列表拓展时，不是复制子列表值，而是复制已有元素的引用！所以当修改其中一个值'
          '时，相应的引用也会被修改')
    print('=' * 80)
#2、删减列表中的元素 { remove(object) / del n[x] / pop(index)}
    print('[simple_function_list]: 2：删除列表中的元素')
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('[simple_function_list]:', end=' ')
    print(n)
    n.remove(3)     #删除首次出现的指定元素
    print('[simple_function_list]:', end=' ')
    print(n)
    del n[1]        #删除指定位置的元素
    print('[simple_function_list]:', end=' ')
    print(n)
    tmp = n.pop()   #返回并删除最后一个元素
    print('[simple_function_list]:', end=' ')
    print(n)
    print('[simple_function_list]: 删除的元素:', end=' ')
    print(tmp)

    tmp = n.pop(1)  # 返回并删除指定位置的元素
    print('[simple_function_list]:', end=' ')
    print(n)
    print('[simple_function_list]: 删除的元素:', end=' ')
    print(tmp)
    #删除所有指定元素：
    n1 = [1, 2, 1, 1, 1, 2, 2]
    print('[simple_function_list]: 删除所有的指定元素:', end=' ')
    print(n1)
    for i in n1[::]:    #分片
        if i == 1:
            n1.remove(i)
    print('[simple_function_list]: 删除所有的指定元素:', end=' ')
    print(n1)
    print('=' * 80)
#3、获取列表里的特定元素{ 直接通过下标获取 / index()获取指定元素的下标 /count() 计数指定元素}
    print('[simple_function_list]: 3：获取列表里的特定元素')
    o =[11, 12, 13, 14, 11]
    tmp = o[2]
    print('[simple_function_list]: 读取的元素:', end=' ')
    print(tmp)

    print('[simple_function_list]: 读取的指定元素的下标:', end=' ')
    tmp = o.index(13)
    print(tmp)
    print('[simple_function_list]: 计数指定元素出现次数:', end=' ')
    tmp = o.count(11)
    print(tmp)
    print('=' * 80)
#4、成员资格判断{ 用 in 关键字判断一个值是否存在列表中}
    print('[simple_function_list]: 4：成员资格判断')
    p = [5, 6, 7, 8, 9, 9]
    tmp = 3 in p
    print('[simple_function_list]: 3是否在列表p中:', end=' ')
    print(tmp)

    p1 = [[1], [2], [3]]
    tmp = 1 in p1
    print('[simple_function_list]: 1是否在列表p1中:', end=' ')
    print(tmp)
    tmp = [1] in p1
    print('[simple_function_list]: [1]是否在列表p1中:', end=' ')
    print(tmp)
    print('=' * 80)
#5、列表分片 { 复制(切片复制是一种浅复制 (对比深复制的区别) / 列表逆序... )}
    print('[simple_function_list]: 5：列表分片')
    q = [1, 2, 3, 4, 5, 6, 7]
    print('[simple_function_list]: 复制列表', end=' ')
    q1 = q[:]
    print(q1)
    print('[simple_function_list]: 逆序列表', end=' ')
    q2 = q[::-1]
    print(q2)
    print('=' * 80)
#6、列表排序 { sort(self , key, reverse) / sorted 生成新列表/ }
    print('[simple_function_list]: 6：列表排序')
    r = [3, 4, 5 , 6, 7, 8, 9, 11, 14 ,15]
    import random
    print('[simple_function_list]: 打乱列表', end=' ')
    random.shuffle(r)   # 打乱列表
    print(r)

    print('[simple_function_list]: sort()默认升序排序', end=' ')
    r.sort()  # 默认升序排序
    print(r)

    print('[simple_function_list]: sort(reverse=True)降序', end=' ')
    r.sort(reverse=True)  # 降序排序
    print(r)

    print('[simple_function_list]: sort(key= lambda x:len(str(x)))', end=' ')
    r.sort(key=lambda x: len(str(x)))  # 按转换成字符串的长度升序排序
    print(r)

    print('[simple_function_list]: sorted 排序并生成新列表', end=' ')
    s = [1, 2, 4, 5 ,6, 8, 12, 11]
    t = sorted(s,reverse = True)
    print(t)
    print('[simple_function_list]: sorted 原列表：', end=' ')
    print(s)

    print('[simple_function_list]: reverse()方法将列表原地逆序：', end=' ')
    print(s.reverse())
    print('[simple_function_list]: reversed()方法将列表逆序并返回新列表：', end=' ')
    oldList = [3, 4, 5 ,6, 8, 12, 11]
    newList = reversed(oldList)     #返回reversed对象
    print(list(newList))            #转换为列表对象
    print('[simple_function_list]: reversed()方法源列表(原列表不变)：', end=' ')
    print(oldList)
'''
def simple_function_for():
    print('[simple_function_for]: into function')
    list_demo = ['苹果', '橘子','李子', '梨']
    for i in list_demo:
        print('[simple_function_for]: 水果:' + i)
    print('[simple_function_for]: 数数')
    for i in range(10):     #range() 函数可创建一个整数列表 range(start, stop[, step])
        print('[simple_function_for]: %d' %(i))
'''

'''
def simple_function_if(param_1, param_2):
    print('[simple_function_if]: into function')
    res = param_1 + param_2
    print('[simple_function_if]: %s 加 %s 等于 %s'%(param_1, param_2, res))
    if res < 50:
        print('[simple_function_if]: 结果小于50')
    elif (res > 50) and ((param_1 == 40) or (param_2 == 20)) :
        print('[simple_function_if]: 结果大于50')
    else:
        print('[simple_function]: 等于50')
    return res
'''
if __name__ == '__main__':
    main()