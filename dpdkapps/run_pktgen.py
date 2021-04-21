import sys
import os

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

steps='''
set 0 src mac 0a:5a:42:75:0a:ca
set 1 src mac 3e:08:fb:12:51:57
set 0 dst mac {}
set 1 dst mac {}
set 0,1 proto udp
set 0,1 count 10000
set 0,1 size 1024
start 0,1
'''

#open("/tmp/test.pkt", "w").write(steps.format(sys.argv[1], sys.argv[2]))

#command = "pktgen -v -l {} -w {} -w {} -n 4 --socket-mem=2048,0 --in-memory -- -m [{}:{}].0 -m [{}:{}].1 -f /tmp/test.pkt"
command = "pktgen -v -l {} -w {} -w {} -n 4 --socket-mem=2048,0 --in-memory -- -m [{}:{}].0 -m [{}:{}].1 -T"

command = command.format(cpus, net1, net2, *cores[1:5])

print(command)
os.system(command)

