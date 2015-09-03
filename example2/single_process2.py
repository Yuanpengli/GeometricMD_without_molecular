__author__ = 'liyuanpeng'
from geometricmd.curve_shorten import compute_trajectory
from geometricmd.geometry import Curve
from ase.io import read
#from ase.calculators.emt import EMT
import numpy as np

#start_point = read('x0.xyz')
#start_point.set_calculator(EMT())

start_point = np.asarray([2.0,5.0,3.3])
#end_point = read('xN.xyz')
end_point = np.asarray([100.0,99.0,98.0])

traj = Curve(start_point, end_point, 20, 1E+03)

compute_trajectory(traj, 9, 1, {'processes': 1})

print traj.points