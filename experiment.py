import subprocess

for delta in [float(x)/100 for x in range(100,70,-5)]:
    max_N = 30000000 

    filename = "results/adabatch_gpomdp_d{}_max_{}_e3".format(delta,max_N)
    filename = filename.replace(".","_")
    filename = filename + ".out"

    subprocess.call(" python lqg/lqg_adabatch.py 1000 {} {} {}".format(delta,filename,max_N), shell=True)

