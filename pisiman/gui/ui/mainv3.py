#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005-2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Please read the COPYING file.
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import QTermWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        
        # Ana widget ve layout
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Ana dikey layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Sekmeli arayüz
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        
        # lsb-release sekmesi
        self.tab_lsb = QtWidgets.QWidget()
        self.tab_lsb.setObjectName("tab_lsb")
        self.verticalLayout_lsb = QtWidgets.QVBoxLayout(self.tab_lsb)
        
        self.lsb_text = QtWidgets.QTextEdit(self.tab_lsb)
        self.lsb_text.setFont(QtGui.QFont("Monospace", 10))
        self.verticalLayout_lsb.addWidget(self.lsb_text)
        
        self.tabWidget.addTab(self.tab_lsb, "lsb-release")
        
        # os-release sekmesi
        self.tab_os = QtWidgets.QWidget()
        self.tab_os.setObjectName("tab_os")
        self.verticalLayout_os = QtWidgets.QVBoxLayout(self.tab_os)
        
        self.os_text = QtWidgets.QTextEdit(self.tab_os)
        self.os_text.setFont(QtGui.QFont("Monospace", 10))
        self.verticalLayout_os.addWidget(self.os_text)
        
        self.tabWidget.addTab(self.tab_os, "os-release")
        
        # pisilinux-release sekmesi
        self.tab_pisilinux = QtWidgets.QWidget()
        self.tab_pisilinux.setObjectName("tab_pisilinux")
        self.verticalLayout_pisilinux = QtWidgets.QVBoxLayout(self.tab_pisilinux)
        
        self.pisilinux_text = QtWidgets.QTextEdit(self.tab_pisilinux)
        self.pisilinux_text.setFont(QtGui.QFont("Monospace", 10))
        self.verticalLayout_pisilinux.addWidget(self.pisilinux_text)
        
        self.tabWidget.addTab(self.tab_pisilinux, "pisilinux-release")
        
        # Terminal sekmesi (mainv2'den alındı)
        self.tab_terminal = QtWidgets.QWidget()
        self.tab_terminal.setObjectName("tab_terminal")
        self.terminalLayout = QtWidgets.QVBoxLayout(self.tab_terminal)
        self.terminalLayout.setObjectName("terminalLayout")
        
        self.terminal = QTermWidget.QTermWidget()
        self.terminal.setHistorySize(-1)
        self.terminal.setScrollBarPosition(2)
        font = QtGui.QFont("Droid Sans Mono")
        font.setPointSize(10)
        self.terminal.setTerminalFont(font)
        self.terminalLayout.addWidget(self.terminal)
        
        self.tabWidget.addTab(self.tab_terminal, "Terminal")
        
        self.verticalLayout.addWidget(self.tabWidget)
        
        # Butonlar için yatay layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # Kaydet butonu
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setText("Değişiklikleri Kaydet")
        self.horizontalLayout.addWidget(self.saveButton)
        
        # İptal butonu
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.setText("Kapat")
        self.horizontalLayout.addWidget(self.cancelButton)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        # Durum çubuğu
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Menü çubuğu
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        
        # Dosya menüsü
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuDosya.setTitle("Dosya")
        
        # İşlemler menüsü
        self.menuIslemler = QtWidgets.QMenu(self.menubar)
        self.menuIslemler.setObjectName("menuIslemler")
        self.menuIslemler.setTitle("İşlemler")
        
        MainWindow.setMenuBar(self.menubar)
        
        # Eylemler
        self.actionKaydet = QtWidgets.QAction(MainWindow)
        self.actionKaydet.setObjectName("actionKaydet")
        self.actionKaydet.setText("Kaydet")
        
        self.actionCikis = QtWidgets.QAction(MainWindow)
        self.actionCikis.setObjectName("actionCikis")
        self.actionCikis.setText("Çıkış")
        
        self.actionYenile = QtWidgets.QAction(MainWindow)
        self.actionYenile.setObjectName("actionYenile")
        self.actionYenile.setText("Yenile")
        
        # Menülere eylemleri ekle
        self.menuDosya.addAction(self.actionKaydet)
        self.menuDosya.addSeparator()
        self.menuDosya.addAction(self.actionCikis)
        
        self.menuIslemler.addAction(self.actionYenile)
        
        # Menü çubuğuna menüleri ekle
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuIslemler.menuAction())
        
        # Sinyal-slot bağlantıları
        self.saveButton.clicked.connect(self.save_changes)
        self.cancelButton.clicked.connect(MainWindow.close)
        self.actionKaydet.triggered.connect(self.save_changes)
        self.actionCikis.triggered.connect(MainWindow.close)
        self.actionYenile.triggered.connect(self.load_files)
        
        # Dosyaları yükle
        self.load_files()
        
    def load_files(self):
        """Dosyaları yükler ve ilgili alanlara yazar."""
        try:
            # lsb-release dosyasını oku
            with open('/etc/lsb-release', 'r') as f:
                self.lsb_text.setPlainText(f.read())
            
            # os-release dosyasını oku
            with open('/etc/os-release', 'r') as f:
                self.os_text.setPlainText(f.read())
            
            # pisilinux-release dosyasını oku
            with open('/etc/pisilinux-release', 'r') as f:
                self.pisilinux_text.setPlainText(f.read())
                
            self.statusBar.showMessage("Dosyalar başarıyla yüklendi", 3000)
            
        except PermissionError:
            self.statusBar.showMessage("Hata: Dosyalara erişim izniniz yok. Lütfen yönetici olarak çalıştırın.", 5000)
        except Exception as e:
            self.statusBar.showMessage("Hata: {}".format(str(e)), 5000)
    
    def save_changes(self):
        """Yapılan değişiklikleri dosyalara kaydeder."""
        try:
            # lsb-release dosyasına yaz
            with open('/etc/lsb-release', 'w') as f:
                f.write(self.lsb_text.toPlainText())
            
            # os-release dosyasına yaz
            with open('/etc/os-release', 'w') as f:
                f.write(self.os_text.toPlainText())
            
            # pisilinux-release dosyasına yaz
            with open('/etc/pisilinux-release', 'w') as f:
                f.write(self.pisilinux_text.toPlainText())
                
            self.statusBar.showMessage("Değişiklikler başarıyla kaydedildi", 3000)
            
        except PermissionError:
            self.statusBar.showMessage("Hata: Dosyalara yazma izniniz yok. Lütfen yönetici olarak çalıştırın.", 5000)
        except Exception as e:
            self.statusBar.showMessage("Hata: {}".format(str(e)), 5000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())