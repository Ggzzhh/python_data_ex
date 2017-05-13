#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from random import choice, randint

import matplotlib.pyplot as plt
import pygal

class RandomWalk(object):
    """生成随机漫步的类"""
    
    def __init__(self, walk_num=500):
        self.walk_num = walk_num
        
        # 初始化出发点
        self.x_values = [0]
        self.y_values = [0]
        
    def get_walk(self):
        """获得向那边走几步的方法"""
        direction = choice([1, -1])
        distance = choice([x for x in range(5)])
        return direction * distance
        
    def fill_walk(self):
        """随机走N步的结果"""
        while len(self.x_values) < self.walk_num:
            x_step = self.get_walk()
            y_step = self.get_walk()
            
            if x_step == 0 and y_step == 0:
                continue
            
            # 获得下一次的坐标
            x_next = self.x_values[-1] + x_step
            y_next = self.y_values[-1] + y_step
            
            self.x_values.append(x_next)
            self.y_values.append(y_next)

# # 产生结果
# random_walk = RandomWalk(30)
# random_walk.fill_walk()
# # 对结果进行可视化
# hist = pygal.Line()
#
#
# hist.title = '随机漫步1000次的结果'
# hist.x_labels = [str(x) for x in random_walk.x_values]
# hist.x_title = '漫步的x坐标'
# hist.y_title = '漫步的y坐标'
#
# hist.add('y的坐标', random_walk.y_values)
# hist.render_to_file('random_walk.svg')

class Die(object):
    """产生骰子的类"""
    def __init__(self, sides=6):
        """骰子面数"""
        self.sides = sides
    
    def roll(self):
        """产生一个1与骰子面数之间的数"""
        return randint(1, self.sides)

# 实例化两个骰子
die_1 = Die()
die_2 = Die()

# 计算两个筛子的最大点数与最小点数
x_die = [x for x in range(2, die_1.sides+die_2.sides+1)]
# 随机500次之后各个点数出现了几次的数组
results = [die_1.roll() + die_2.roll() for x in range(500)]
y_die = [results.count(x) for x in x_die]

# 把500次扔2个骰子产生的结果可视化
plt.plot(x_die, y_die, linewidth=10)
plt.show()