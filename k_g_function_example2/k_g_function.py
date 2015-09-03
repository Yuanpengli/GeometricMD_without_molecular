__author__ = 'liyuanpeng'
__author__ = 'liyuanpeng'
import math
import logging
import numpy as np
from numpy import *


#given a k(x) function, for example, k(x)=\sqrt{|sin(x^3+2x)|}
def k_function(point):

    dimension = len(point)
    k_vector = np.zeros(dimension)
  #  for i in range(dimension):
    k_vector[0]=-point[0]+point[1]*point[1]
    k_vector[1]=-point[1]-point[0]*point[1]*point[0]
    k_vector[2]=point[0]+point[2]

    return k_vector


def g_function(point):
    dimension = len(point)
    g_matrix = np.zeros([3, dimension])
   # for i in range(dimension):
        # print np.dtype(point[i])
    g_matrix[0][0] = point[0]
    g_matrix[1][0] = point[1]
    g_matrix[2][0] = point[0]*point[1]
    g_matrix[0][1] = -point[0]
    g_matrix[1][1] = -2.0*point[1]
    g_matrix[2][1] = point[0]*point[2]
    g_matrix[0][2] = -point[0]*point[0]*point[1]
    g_matrix[1][2] = -2.0*point[2]*(point[0]+point[1])
    g_matrix[2][2] = point[2]

    return g_matrix

