# -*- coding:utf-8 -*-

x1, x2, y1, y2 = -2.13, 0.77, -1.3, 1.3

def calculate_z_serial_purepython(q, maxiter, z):
    output = [0] * len(q)
    for i in range(len(q)):
        if i % 1000 == 0:
            ## print out some progress info since it is so slow...
            print("%0.2f%% complete" % (1.0 / len(q) * i * 100))
    for iteration in range(maxiter):
        z[i] = z[i] * z[i] + q[i]
        if abs(z[i]) > 2.0:
            output[i] = iteration
            break
    return output

