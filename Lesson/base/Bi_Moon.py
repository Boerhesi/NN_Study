# coding=utf-8
import math
import random

import pylab as pl


class BiMoon(object):
    ''''
        一对非对称的面对面的"月亮"。"区域A"的月亮是关于y轴对称的，而被标志为"区域B"的月亮被安置在y轴右边距离
        半径为r以及x轴下面d的地方。
        每个月亮的半径，r=10
        每个月亮的宽度，w=6
        增加d的正值，表示增加两个月亮之间的距离，两个月亮相互分离
        增加d的负值，表示减少两个月亮之间的距离，两个月亮相互靠近
        训练样本集是由1000对数据点组成的
    '''

    def random_pair(self, radio, w, x_d=0, y_d=0):
        max_radio = radio + w
        theta = random.random() * 2 * math.pi
        x = random.uniform(radio * math.sin(theta), max_radio * math.sin(theta))
        y = abs(random.uniform(radio * math.cos(theta), max_radio * math.cos(theta)))
        return x + x_d, y + y_d

    def generate_data(self, r, w, x_d, y_d, num):
        xa_x, xa_y = self.get_point([self.random_pair(r, w) for i in range(0, num)], 1)
        xb_x, xb_y = self.get_point([self.random_pair(r, w, x_d, y_d) for i in range(0, num)], -1)
        return (xa_x, xa_y), (xb_x, xb_y)

    def get_point(self, pairs, sign):
        x = []
        y = []
        for pair in pairs:
            point_x = pair[0]
            point_y = pair[1] * sign
            x.append(point_x)
            y.append(point_y)
        return x, y

    def plot_moon(self, xa, xb):
        pl.scatter(xa[0], xa[1], c='r')
        pl.scatter(xb[0], xb[1], c='g')
        pl.show()

    # r=10, w=6, d=1, num=1000
    def generate_bi_moon(self, r, w, x_d, y_d, num, flag=False):
        xa, xb = self.generate_data(r, w, x_d, y_d, num)
        if flag:
            self.plot_moon(xa, xb)
        return xa, xb


if __name__ == '__main__':
    bi_moon = BiMoon()
    bi_moon.generate_bi_moon(r=10, w=6, x_d=10, y_d=-4, num=2000, flag=True)
