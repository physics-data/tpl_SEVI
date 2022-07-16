# encoding=utf8
import numpy as np
import h5py
import argparse

R0, DeltaR = 0.8, 0.02
E_k = 300

def sample(size):
    '''
    采样电子的位置和动能，速度方向'''
    nums = np.array(np.abs(np.random.poisson(100,size=size)), dtype=np.int64)
    totalnum = np.sum(nums)
    # 采样r
    r = np.random.uniform(R0, R0+DeltaR, size=(totalnum))
    '''
    你需要在这里采样 theta, phi, v_x, v_y, v_z
    '''

    eventID = np.repeat(np.arange(size), nums)
    return eventID, positionx, positiony, v_x, v_y, v_z

psr = argparse.ArgumentParser()
psr.add_argument("-i", dest="size", type=int, default=5000, help="sample size")
psr.add_argument("-o", dest="opt", help="output h5 file")
args = psr.parse_args()
eventID, positionx, positiony, v_x, v_y, v_z = sample(args.size)

positions = np.zeros(eventID.shape[0], dtype=[('EventID', np.int64), ('x', np.float64), ('y', np.float64), ('vx', np.float64), ('vy', np.float64), ('vz', np.float64), ('Ek', np.float64)])
positions['EventID'] = eventID
positions['x'] = positionx
positions['y'] = positiony
positions['vx'] = v_x
positions['vy'] = v_y
positions['vz'] = v_z
positions['Ek'] = E_k

with h5py.File(args.opt, 'w') as opt:
    opt.create_dataset('position', data=positions, compression='gzip')