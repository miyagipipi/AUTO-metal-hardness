# -*- coding: utf-8 -*-
"""
@author: LQS
"""
import random
class metalHardness(object):

    def __init__(self, mean, div, _max, _min, nums):
        self._mean = float(mean)
        self._div = float(div)
        self._max = float(_max) 
        self._min = float(_min)
        self._nums = float(nums)

    def HRA79_85(self):
        print('本函数适合于79.5-85HRA的试样\n')
        with open(r'D:\金属硬度\正态分布数据.txt','a') as f:
            i = 1
            while i <= self._nums:
                v = round(random.normalvariate(self._mean, self._div), 1)
                if v < self._min: v = self._min
                elif v > self._max: v = self._max
                if i % 3 == 0:
                    f.write(str(v) + '\n')
            
                else:
                    f.write(str(v) + '\t')
                i += 1
        print('HRA数据已生成，注意在生成新数据时清空记事本！')
    
    def HRC22_34(self):
        print('本函数适合于22-34HRC的试样\n')

        base_mean = 1.688889
        base_div = 1.517283
        base_max = 3.7
        base_min = 0.062222

        with open(r'D:\金属硬度\正态分布数据.txt','a') as f:

            i = 1
            while i <= self._nums:
                #先按正态分布随机出一个数作平均数，
                base_v = round(random.normalvariate(self._mean, self._div), 1)
                if base_v > self._max: base_v = self._max
                elif base_v < self._min: base_v = self._min
                base_count = 0

                if base_v < self._min: base_v = self._min
                elif base_v >= self._max: base_v = self._max

                #再生成一个服从正态分布的方差，然后用这个方差作为base_v的方差
                hrb_div = round(random.normalvariate(base_mean, base_div), 1)
                if hrb_div > base_max: hrb_div = base_max
                elif hrb_div < base_min: hrb_div = base_min

                f.write(str(base_v) + '\t')
                i += 1
                while base_count < 2:
                    if base_count < 1:
                        v = round(random.normalvariate(base_v, hrb_div), 1)
                        if v < self._min: v = self._min
                        elif v > self._max: v = self._max
                        f.write(str(v) + '\t')
                    else:
                        v = round(random.normalvariate(base_v, hrb_div), 1)
                        if v < self._min: v = self._min
                        elif v > self._max: v = self._max
                        f.write(str(v) + '\n')
                    i += 1
                    base_count += 1
        print('HRA数据已生成，注意在生成新数据时清空记事本！')

    def HRC59_64(self):
        print('本函数适合于59-64HRC的试样\n')
        with open(r'D:\金属硬度\正态分布数据.txt','a') as f:

            i = 1
            while i <= self._nums:
                v = round(random.normalvariate(self._mean, self._div), 1)
                if v < self._min: v = self._min
                elif v > self._max: v = self._max
                if i % 3 == 0:
                    f.write(str(v) + '\n')
            
                else:
                    f.write(str(v) + '\t')
                i += 1
        print('HRA数据已生成，注意在生成新数据时清空记事本！')

if __name__ == '__main__':
    print('请输入硬度标准和范围，目前可选的有HRC(59-64)，HRC(22-34)，HRB(60-110)。\n')
    print('正确的输入格式为：HRA79_85，HRC22_34和HRC59_64')

    hardnessName = input('请输入： ')
    nums = int(input('需要多少组数据： ')) * 3

    if hardnessName == 'HRA79_85':
        #(self, mean, div, _max, _min, nums)
        
        res = metalHardness(82.5, 0.840112, 84, 79.5, nums)
        res.HRA79_85()

    elif hardnessName == 'HRC22_34':
        
        res = metalHardness(24.9, 4.361664, 30.4, 22.0, nums)
        res.HRC22_34()

    elif hardnessName == 'HRC59_64':
        res = metalHardness(61.7, 1.08, 63.9, 59.0, nums)
