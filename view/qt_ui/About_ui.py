# Form implementation generated from reading ui file 'd:\PJT\PY\py PUC_Image_Converter\view\qt_ui\About.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(449, 222)
        self.lblBuildTime = QtWidgets.QLabel(parent=About)
        self.lblBuildTime.setGeometry(QtCore.QRect(120, 0, 321, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.lblBuildTime.setFont(font)
        self.lblBuildTime.setObjectName("lblBuildTime")
        self.lblApplicationName = QtWidgets.QLabel(parent=About)
        self.lblApplicationName.setGeometry(QtCore.QRect(8, 30, 431, 20))
        self.lblApplicationName.setObjectName("lblApplicationName")
        self.lblMainMessage = QtWidgets.QLabel(parent=About)
        self.lblMainMessage.setGeometry(QtCore.QRect(10, 80, 431, 91))
        self.lblMainMessage.setObjectName("lblMainMessage")
        self.btnClose = QtWidgets.QPushButton(parent=About)
        self.btnClose.setGeometry(QtCore.QRect(190, 190, 75, 24))
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(About)
        self.btnClose.clicked.connect(About.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.lblBuildTime.setText(_translate("About", "<html><head/><body><p align=\"right\"><span style=\" color:#a6a6a6;\">Build time: Aug 2023</span></p></body></html>"))
        self.lblApplicationName.setText(_translate("About", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#0000ff;\">CSV DATA TO BOX PLOT</span></p></body></html>"))
        self.lblMainMessage.setText(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    Author:     Do Trong Khang<br />    Email:     </span><span style=\" font-size:10pt;\">khangdt.work@gmail.com</span><span style=\" font-size:10pt;\"><br />    </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.btnClose.setText(_translate("About", "OK"))
