#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态 就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk实例 并将其所有的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    
    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))
    
    point_number = list(range(rw.num_points))
    
    plt.plot(rw.x_values, rw.y_values, linewidth=5)
    
    # 突出起点和终点
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
    
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    #keep_running = input('Make another walk? y/n\n>')
    #if keep_running == 'n':
    break