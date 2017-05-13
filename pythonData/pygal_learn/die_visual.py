#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pygal

from die import Die

# 创建一个D6一个骰子
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 投掷几次骰子 并将结果存储在一个列表中
results = [die_1.roll() + die_2.roll() + die_3.roll() for x in range(50000)]
# for roll_num in range(50000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
    
# 分析结果
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(x) for x in range(3, max_result+1)]

# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
    
# 对结果进行可视化
hist = pygal.Bar()

hist.title = '测试三个六面骰子扔50000次的结果'
hist.x_labels = [str(x) for x in range(3, max_result+1)]
hist.x_title = '点数'
hist.y_title = '点数出现的次数'

hist.add('D8 + D8', frequencies)
hist.render_to_file('die_visual.svg')