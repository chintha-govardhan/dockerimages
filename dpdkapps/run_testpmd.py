import sys
import os

if len(sys.argv) != 3:
    print("Usage: python3 run_testpmd.py <mac of ethpeer0> <mac of ethpeer1>")
    exit(1)

def expand_cpus(cpus):

    temp = cpus.split(',')
    exp_cpus = []
    for i in temp:
        exp_cpus.extend(list(range(int(i.split('-')[0]),int(i.split('-')[-1])+1)))

    return sorted(exp_cpus)


devices = [ v for k,v in os.environ.items() if 'PCIDEVICE' in k ][0]

net1 = devices.split(',')[0]
net2 = devices.split(',')[1]

cpus=open('/sys/fs/cgroup/cpuset/cpuset.cpus').read().strip('\n')
#cpus="5-6,26,28-29"
cores=expand_cpus(cpus)

command = "dpdk-testpmd -l {} -n 4 -w {} -w {} --socket-mem=2048,0 --log-level=10 -- --socket-num=0 --port-numa-config=0,0,1,0 --nb-cores=2 --mbcache=512 --rxq=1 --txq=1 --rxd=2048 --txd=2048 --burst=64 --portmask=3 --forward-mode=mac --eth-peer=0,{} --eth-peer=1,{} -a"

command = command.format(cpus, net1, net2, sys.argv[1], sys.argv[2])
#command = command.format(cpus, net1, net2, "0a:5a:42:75:0a:ca", "3e:08:fb:12:51:57")

print(command)
os.system(command)

