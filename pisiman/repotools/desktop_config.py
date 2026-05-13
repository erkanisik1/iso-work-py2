#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005-2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import os
import shutil

def kde_conf(project):
    
    image_dir = project.image_dir()
    
    #os.system("mkdir -p %s/home/pisi/.config" % image_dir)

    os.system("cp -f ./data/desktop_conf/kde_conf/script/* %s/usr/local/bin" % image_dir)
    os.system("chmod +x %s/usr/local/bin/*" % image_dir)
    
    #os.system("cp -rf ./data/desktop_conf/kde_conf/.local %s/home/pisi" % image_dir)
    #os.system("cp -rf ./data/desktop_conf/kde_conf/usr/share/look-and-feel/maia-light %s/usr/share/look-and-feel/" % image_dir)
    
    os.system("cp -rf ./data/etc/skel/ %s/etc/" % image_dir)
    os.system("cp -rf ./data/desktop_conf/kde_conf/xdg/ %s/etc/" % image_dir)
    
    os.system("cp -rf ./data/etc/skel/.config %s/home/pisi" % image_dir)
    os.system("cp -rf ./data/etc/skel/.config/ %s/etc/skel/" % image_dir)
    os.system("cp -rf ./data/etc/skel/ %s/etc/" % image_dir)
    os.system("cp -rf ./data/etc/profile.d/ %s/etc/" % image_dir)
    
    os.system("cp -rf ./data/etc/xdg/ %s/etc/" % image_dir)
    os.system("cp -rf ./data/desktop_conf/kde_conf/usr %s/" % image_dir)
    
    os.system("cp -rf ./data/desktop_conf/kde_conf/wallpapers %s/usr/share" % image_dir)
    os.system("chroot %s chown -R pisi:wheel /home/pisi/.config" % image_dir)
    os.system("chroot %s chown -R pisi:wheel /home/pisi/.local" % image_dir)

    os.system("mkdir -p %s/home/pisi/Desktop" % image_dir)
    # os.system("mkdir -p %s/home/pisi/Masaüstü" % image_dir)

    shutil.copy("./data/yali/yali.desktop", "%s/home/pisi/Desktop/" % image_dir)
    # shutil.copy("./data/yali/yali.desktop", "%s/home/pisi/Masaüstü/" % image_dir)

    shutil.copy("./data/yali/yali-rescue.desktop", "%s/home/pisi/Desktop/" % image_dir)        
    # shutil.copy("./data/yali/yali-rescue.desktop", "%s/home/pisi/Masaüstü/" % image_dir)

def xfce_conf(image_dir):
    run("mkdir -p {}/home/pisi/Desktop".format(image_dir))

    shutil.copy("./data/yali/yali.desktop", "{}/home/pisi/Desktop/".format(image_dir))
    shutil.copy("./data/yali/yali-rescue.desktop", "{}/home/pisi/Desktop/".format(image_dir)) 
    
    #shutil.copy("./data/xfce4/yali-desktop-copy.sh", "{}/usr/bin/".format(image_dir))
    #shutil.copy("./data/xfce4/etc/xdg/autostart/yali-desktop.desktop", "{}/etc/xdg/autostart/".format(image_dir))
    
    shutil.copy("./data/xfce4/usr/share/backgrounds/xfce/pisiBackground.jpg", "{}/usr/share/backgrounds/xfce/".format(image_dir))
    shutil.copy("./data/xfce4/etc/lightdm/web-greeter.yml", "{}/etc/lightdm/".format(image_dir))
    os.system("cp -rf ./data/xfce4/etc/skel/.config/ {}/home/pisi/".format(image_dir))
    os.system("cp -rf ./data/xfce4/etc/skel/.config/ {}/etc/skel/".format(image_dir))
    #os.system("cp -rf ./data/xfce4/etc/lightdm/ {}/etc/".format(image_dir))

    os.system("cp -rf ./data/xfce4/usr/share/ {}/usr/".format(image_dir))