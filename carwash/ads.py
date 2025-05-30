# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carwash.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView

class AdvertisingWindow(object):
    def setupUi(self, mainui):
        mainui.setObjectName("mainui")
        mainui.setWindowModality(QtCore.Qt.ApplicationModal)
        mainui.resize(1920, 1080)
        self.layoutWidget = QtWidgets.QWidget(mainui)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.layoutWidget.setObjectName("layoutWidget")
        
        # Create QGridLayout
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Updated to use QWebEngineView
        self.webView = QWebEngineView(self.layoutWidget)
        # self.webView.contextMenuEvent = lambda event: None  # Disable context menu
        self.webView.setUrl(QtCore.QUrl("https://www.youtube.com/watch?v=vr0htZlAQbk&feature=youtu.be"))
        self.webView.setObjectName("webView")
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 3)
        self.gridLayout.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.gridLayout.setRowStretch(0, 1)
        
        # Add auto-scroll text label
        self.font = QtGui.QFont()
        self.font.setFamily("Serif")
        self.font.setPointSize(54)
        self.font.setBold(True)
        self.font.setWeight(75)

        self.scrollLabel = QtWidgets.QLabel(self.layoutWidget)
        self.scrollLabel.setFont(self.font)
        self.scrollLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.scrollLabel.setObjectName("scrollLabel")
        self.gridLayout.addWidget(self.scrollLabel, 2, 0, 1, 1)

        # Initialize scrolling
        self.scroll_text = "Bu avtomatik scroll qiluvchi matnli QLabel misolidir. "
        self.scroll_position = 0
        self.scroll_timer = QtCore.QTimer()
        self.scroll_timer.timeout.connect(self.update_scroll_text)
        self.scroll_timer.start(100)  # Har 100ms da yangilanadi

        self.retranslateUi(mainui)
        QtCore.QMetaObject.connectSlotsByName(mainui)

    def update_scroll_text(self):
        """Matnni avtomatik scroll qilish."""
        self.scroll_position += 1
        if self.scroll_position > len(self.scroll_text):
            self.scroll_position = 0
        display_text = self.scroll_text[self.scroll_position:] + " " + self.scroll_text[:self.scroll_position]
        self.scrollLabel.setText(display_text)

    def retranslateUi(self, mainui):
        _translate = QtCore.QCoreApplication.translate
        mainui.setWindowTitle(_translate("mainui", "Frame"))
        self.scrollLabel.setText(_translate("mainui", self.scroll_text))
