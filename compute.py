import numpy
import csv
import time
import os
from numpy.linalg import inv

ncolumns = 1000
filename = "highprio.csv"
with open(filename, 'w', newline = '\n') as f1:
    writer = csv.writer(f1, delimiter='\n')
    floatlist = []
    for i in range(100):
        start_time = time.time()
        #create a random 1000 * 1000 for computing
        mat0 = numpy.random.random((nrows, ncolumns))
        mat1 = numpy.random.random((nrows, ncolumns))
        #print(numpy.array(mat))
        inv(numpy.dot(mat0, mat1))
        floatlist.append(time.time() - start_time)
    writer.writerow(floatlist)
