# coding=utf-8

import random
import time
#导入timeit和cProfile,进行性能分析
import timeit
import cProfile
#导入pstats，用于分析cProfile输出的文件内容，cProfile输出内容是以二进制保存的，文本编辑器打开时乱码
import pstats

#位图排序
def bit_sort(seq):
    #内部转换为集合,加快成员检测
    a = set(seq)
    #创建位图结构
    bits = [0 for _ in range(10**7)]
    #迭代位图，如果索引位于seq中，则讲位图中该索引对应的数据记为1，注意，索引从1开始
    for index, _ in enumerate(bits, 1):
        if index in a:
            bits[index] = 1
    return (index for index, x in enumerate(bits) if x == 1)

seq = random.sample(range(1, 10**7+1), 100)
print(seq)

b = bit_sort(seq)
print(list(b))

print(cProfile.run('bit_sort(%s)'%seq, filename='result.out'))
print(timeit.timeit('%s.sort()'%seq))

#创建Stats对象
p = pstats.Stats('result.out')

#按照运行时间和函数名进行排序
p.strip_dirs().sort_stats('cumulative', 'name').print_stats()