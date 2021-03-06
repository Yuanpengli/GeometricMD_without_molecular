__author__ = 'liyuanpeng'

from geometricmd.curve_shorten import compute_trajectory
from geometricmd.geometry import Curve
import numpy as np
import time
from multiprocessing import cpu_count
start = time.clock()

start_point = np.asarray([2.0,5.5,3.3])
end_point = np.asarray([100.0,99.0,98.0])
global_number_node=30
traj = Curve(start_point, end_point, global_number_node)
tol=10

compute_trajectory(traj, 9, tol, {'processes': (cpu_count()-1)})

print traj.points

f=open("geodesic.txt",'w')
for i in range(global_number_node):
    t=traj.points[i]
    f.write(str(t)+ "\n")
f.close()

spent_time= (time.clock()-start)

print spent_time