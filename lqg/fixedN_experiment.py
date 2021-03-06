import subprocess
import os

#for delta in [float(x)/100 for x in range(100,0,-5)]:
max_N = 1000000
N_min = 100
N_max = 10000
for delta in [0.95,0.75,0.5,0.25,0.05]:
    for i in range(1):
        for estimator in [1]:
            for bound in [1]:
                if estimator+bound==1:
                    continue
                filename = "results/final/eff_N{}_est{}_bound{}__delta{}_sample{}".format(N_min,estimator,bound,delta,i+1)
                filename = filename.replace(".","_")
                filename = filename + ".out"

                subprocess.call("python lqg_fixedN.py {} {} {} {} {} {} {}".format(N_min,N_max,delta,estimator,bound,filename,max_N), shell=True)

