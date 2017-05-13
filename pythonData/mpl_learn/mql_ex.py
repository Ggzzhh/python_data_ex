#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40)
plt.title('LiFang', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('LiFang of Value', fontsize = 14)

# 设定取值范围
#plt.axis([0, 510, 0, 100000000])

plt.show()