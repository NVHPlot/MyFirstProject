# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 13:27
# @Author  : Baoguo.li@mscsoftware.com
# @Site    : 
# @File    : .py
# @Software: MSC
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os
import sys
import pandas as pd
import math
import xml.etree.ElementTree as ET
import csv
import tables as pt
import shutil
import logging
import time

plt.rcParams.update({'figure.max_open_warning': 0})
sys.setrecursionlimit(1000000)

logging.basicConfig(filename='MyLog.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
#
# logging.disable(logging.DEBUG)
#
logging.debug('Start of program')
start =time.clock()




logging.debug("time is: %f s"%(time.clock()-start))
logging.debug('End of program')