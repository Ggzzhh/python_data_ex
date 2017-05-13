#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from random import choice

class RandomWalk(object):
    """一个生成随机漫步数据的类"""
    
    def __init__(self, num_points=5000):
        """初始化随机漫步数据的属性"""
        self.num_points = num_points
        
        # 所有随机漫步都始于（0， 0）
        self.x_values = [0]
        self.y_values = [0]
        
    def get_walk(self):
        """计算行走方向并返回"""
        direction = choice([1, -1])
        distance = choice([x for x in range(10)])
        return direction * distance
    
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        
        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进的方向以及距离
            x_step = self.get_walk()
            y_step = self.get_walk()
            
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
                
            # 计算下一个x值和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)