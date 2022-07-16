# encoding=utf8
import h5py
import argparse
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

psr = argparse.ArgumentParser()
psr.add_argument("-o", dest="opt", type=str, help="output file")
psr.add_argument("-i", dest="ipt", type=str, help="input file")
args = psr.parse_args()

with h5py.File(args.ipt, 'r') as ipt:
    positions = ipt['position'][:]
with PdfPages(args.opt) as pdf:
    # DEMO：简略绘制x,y位置二维分布，你需要加入细节的调整
    fig, ax = plt.subplots()
    ax.hist2d(positions['x'], positions['y'])
    pdf.savefig(fig)