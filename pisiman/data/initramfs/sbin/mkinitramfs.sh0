#!/bin/bash
set -e

KERNEL=$(uname -r)
OUT=initramfs.img
WORK=initramfs-root

rm -rf $WORK
mkdir -p $WORK/{bin,sbin,proc,sys,dev,ro,rw,newroot,lib/modules}

cp /bin/busybox $WORK/bin/
ln -s busybox $WORK/bin/sh

cp /sbin/switch_root $WORK/sbin/

# init
cp init $WORK/init
chmod +x $WORK/init

# modüller
cp -r /lib/modules/$KERNEL $WORK/lib/modules/

# device nodes
sudo mknod -m 622 $WORK/dev/console c 5 1
sudo mknod -m 666 $WORK/dev/null c 1 3

cd $WORK
find . | cpio -H newc -o | gzip > ../$OUT
cd ..

echo "initramfs created: $OUT"
