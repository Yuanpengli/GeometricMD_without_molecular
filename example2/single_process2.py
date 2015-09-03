__author__ = 'liyuanpeng'
from geometricmd.curve_shorten import compute_trajectory
from geometricmd.geometry import Curve
import numpy as np


start_point = np.asarray([2.0,5.0,3.3])
end_point = np.asarray([100.0,99.0,98.0])

traj = Curve(start_point, end_point, 20)

compute_trajectory(traj, 9, 10, {'processes': 1})

print traj.points

#def write_file(traj.points):


