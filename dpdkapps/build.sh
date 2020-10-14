#!/bin/bash

cd /root

wget https://github.com/ninja-build/ninja/releases/download/v1.7.1/ninja-linux.zip

unzip ninja-linux.zip -d /usr/bin/

git clone https://github.com/DPDK/dpdk.git
cd dpdk && git checkout main && meson build && ninja -C build install

git clone https://github.com/pktgen/Pktgen-DPDK.git
cd Pktgen-DPDK && git checkout pktgen-20.10.0 && meson build && ninja -C build install 

rm -rf /root/dpdk
rm -rf /root/Pktgen-DPDK

cd /root && ldconfig
