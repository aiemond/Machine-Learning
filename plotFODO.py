#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:54:56 2022

@author: emondemoniac
"""

import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d
from matrixFODO import Component
from mainFODO import Cell


def plot_cell(self):
        pos, bx, by = self.evolve_beta()

        bx = np.asarray(bx)
        by = np.asarray(by)
        pos = np.asarray(pos)
        pos[0] = 1e-10

        plt.plot(pos, by, label='beta_y', color=self.rot, linewidth=2, marker='o')

        plt.xlabel('s [m]')
        ax1 = plt.gca()
        ax1.set_ylabel('beta [m]')

        line = plt.gca().get_lines()[0]
        maximum = int(line.get_ydata().max()) - 1
        cnt = 0
        global rect 
        for i in range(self.component_number):
            if self.component_list[i].typ == 'qf':
                rect = mpatches.Rectangle((cnt, maximum), self.length_list[i], 0.5, ec=self.gruen, fill=False,
                                          linewidth=2,
                                          joinstyle='round')
            if self.component_list[i].typ == 'qd':
                rect = mpatches.Rectangle((cnt, maximum - 0.5), self.length_list[i], 0.5, ec=self.rot, fill=False,
                                          linewidth=2,
                                          joinstyle='round')
            if self.component_list[i].typ == 'b':
                rect = mpatches.Rectangle((cnt, maximum - 0.5), self.length_list[i], 1, ec=self.blau, fill=False,
                                          linewidth=2,
                                          joinstyle='round')
            if self.component_list[i].typ == 'd':
                rect = mpatches.Rectangle((cnt, maximum), self.length_list[i], 0.1, ec="black", color='black', )
            cnt = cnt + self.length_list[i]
            plt.gca().add_patch(rect)

        plt.grid(True)
        plt.title(self.title)

        plt.savefig(os.path.splitext(self.filename)[0] + '.png', dpi=300)
        plt.savefig(os.path.splitext(self.filename)[0] + '.pdf')


if __name__ == "__main__":
    c = Cell('willey1.txt')
    print(c.total_matrix())
    print (c.plot_cell())

    
