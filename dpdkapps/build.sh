#!/bin/bash

set -eo pipefail

dpdk_branch=$1
pktgen_branch=$2

echo "DPDK Branch: $dpdk_branch"
echo "PKTGEN Branch: $pktgen_branch"

cd /root

wget https://github.com/ninja-build/ninja/releases/download/v1.10.2/ninja-linux.zip

unzip ninja-linux.zip -d /usr/bin/

git clone https://github.com/DPDK/dpdk.git
cd dpdk && git checkout "$dpdk_branch" && meson build && ninja -C build install

cd /root

git clone https://github.com/pktgen/Pktgen-DPDK.git
cd Pktgen-DPDK && git checkout "$pktgen_branch" && meson build && ninja -C build install 

rm -rf /root/dpdk
rm -rf /root/Pktgen-DPDK

cd /root && ldconfig
