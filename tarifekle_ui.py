# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tarifekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(727, 877)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 130, 341, 171))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        spacerItem = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.kisiBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.kisiBox.setFont(font)
        self.kisiBox.setMinimum(1)
        self.kisiBox.setObjectName("kisiBox")
        self.horizontalLayout_2.addWidget(self.kisiBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.hazirlamaBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.hazirlamaBox.setFont(font)
        self.hazirlamaBox.setMinimum(5)
        self.hazirlamaBox.setMaximum(480)
        self.hazirlamaBox.setObjectName("hazirlamaBox")
        self.horizontalLayout_3.addWidget(self.hazirlamaBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pisirmeBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pisirmeBox.setFont(font)
        self.pisirmeBox.setMinimum(5)
        self.pisirmeBox.setMaximum(480)
        self.pisirmeBox.setObjectName("pisirmeBox")
        self.horizontalLayout_4.addWidget(self.pisirmeBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(430, 179, 261, 121))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.adimBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.adimBox.setFont(font)
        self.adimBox.setMinimum(1)
        self.adimBox.setMaximum(9)
        self.adimBox.setProperty("value", 4)
        self.adimBox.setObjectName("adimBox")
        self.horizontalLayout_6.addWidget(self.adimBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        spacerItem4 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.malzemeBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.malzemeBox.setFont(font)
        self.malzemeBox.setMinimum(1)
        self.malzemeBox.setMaximum(8)
        self.malzemeBox.setProperty("value", 4)
        self.malzemeBox.setObjectName("malzemeBox")
        self.horizontalLayout_5.addWidget(self.malzemeBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(30, 30, 341, 80))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.tarifAdLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.tarifAdLine.setFont(font)
        self.tarifAdLine.setObjectName("tarifAdLine")
        self.verticalLayout_5.addWidget(self.tarifAdLine)
        self.ekleButon = QtWidgets.QPushButton(Form)
        self.ekleButon.setGeometry(QtCore.QRect(490, 100, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ekleButon.setFont(font)
        self.ekleButon.setObjectName("ekleButon")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(430, 322, 259, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.malzeme3Line = QtWidgets.QLineEdit(Form)
        self.malzeme3Line.setGeometry(QtCore.QRect(430, 489, 259, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.malzeme3Line.setFont(font)
        self.malzeme3Line.setObjectName("malzeme3Line")
        self.malzeme7label = QtWidgets.QLabel(Form)
        self.malzeme7label.setGeometry(QtCore.QRect(430, 689, 259, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.malzeme7label.setFont(font)
        self.malzeme7label.setObjectName("malzeme7label")
        self.malzeme6Line = QtWidgets.QLineEdit(Form)
        self.malzeme6Line.setGeometry(QtCore.QRect(430, 658, 259, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.malzeme6Line.setFont(font)
        self.malzeme6Line.setObjectName("malzeme6Line")
        self.malzeme8label = QtWidgets.QLabel(Form)
        self.malzeme8label.setEnabled(True)
        self.malzeme8label.setGeometry(QtCore.QRect(430, 745, 259, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.malzeme8label.setFont(font)
        self.malzeme8label.setObjectName("malzeme8label")
        self.malzeme7Line = QtWidgets.QLineEdit(Form)
        self.malzeme7Line.setGeometry(QtCore.QRect(430, 714, 259, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.malzeme7Line.setFont(font)
        self.malzeme7Line.setObjectName("malzeme7Line")
        self.malzeme6label = QtWidgets.QLabel(Form)
        self.malzeme6label.setGeometry(QtCore.QRect(430, 632, 259, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.malzeme6label.setFont(font)
        self.malzeme6label.setObjectName("malzeme6label")
        self.malzeme2label = QtWidgets.QLabel(Form)
        self.malzeme2label.setGeometry(QtCore.QRect(430, 407, 259, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.malzeme2label.setFont(font)
        self.malzeme2label.setObjectName("malzeme2label")
        self.malzeme1Line = QtWidgets.QLineEdit(Form)
        self.malzeme1Line.setGeometry(QtCore.QRect(430, 376, 259, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.malzeme1Line.setFont(font)
        self.malzeme1Line.setObjectName("malzeme1Line")
        self.malzeme2Line = QtWidgets.QLineEdit(Form)
        self.malzeme2Line.setEnabled(True)
        self.malzeme2Line.setGeometry(QtCore.QRect(430, 433, 259, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.malzeme2Line.setFont(font)
        self.malzeme2Line.setObjectName("malzeme2Line")
        self.malzeme5label = QtWidgets.QLabel(Form)
        self.malzeme5label.setEnabled(True)
        self.malzeme5label.setGeometry(QtCore.QRect(430, 576, 259, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.malzeme5label.setFont(font)
        self.malzeme5label.setObjectName("malzeme5label")
        self.malzeme1label = QtWidgets.QLabel(Form)
        self.malzeme1label.setGeometry(QtCore.QRect(430, 351, 259, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.malzeme1label.setFont(font)
        self.malzeme1label.setObjectName("malzeme1label")
        self.malzeme5Line = QtWidgets.QLineEdit(Form)
        self.malzeme5Line.setGeometry(QtCore.QRect(430, 601, 259, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.malzeme5Line.setFont(font)
        self.malzeme5Line.setObjectName("malzeme5Line")
        self.malzeme4Line = QtWidgets.QLineEdit(Form)
        self.malzeme4Line.setGeometry(QtCore.QRect(430, 545, 259, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.malzeme4Line.setFont(font)
        self.malzeme4Line.setObjectName("malzeme4Line")
        self.malzeme3label = QtWidgets.QLabel(Form)
        self.malzeme3label.setGeometry(QtCore.QRect(430, 464, 259, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.malzeme3label.setFont(font)
        self.malzeme3label.setObjectName("malzeme3label")
        self.malzeme8Line = QtWidgets.QLineEdit(Form)
        self.malzeme8Line.setEnabled(True)
        self.malzeme8Line.setGeometry(QtCore.QRect(430, 770, 259, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.malzeme8Line.setFont(font)
        self.malzeme8Line.setFrame(True)
        self.malzeme8Line.setObjectName("malzeme8Line")
        self.malzeme4label = QtWidgets.QLabel(Form)
        self.malzeme4label.setGeometry(QtCore.QRect(430, 520, 259, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.malzeme4label.setFont(font)
        self.malzeme4label.setObjectName("malzeme4label")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(40, 325, 339, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.adim6label = QtWidgets.QLabel(Form)
        self.adim6label.setGeometry(QtCore.QRect(40, 634, 339, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adim6label.setFont(font)
        self.adim6label.setObjectName("adim6label")
        self.adim6Line = QtWidgets.QLineEdit(Form)
        self.adim6Line.setGeometry(QtCore.QRect(40, 659, 339, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.adim6Line.setFont(font)
        self.adim6Line.setObjectName("adim6Line")
        self.adim1Line = QtWidgets.QLineEdit(Form)
        self.adim1Line.setGeometry(QtCore.QRect(40, 379, 339, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.adim1Line.setFont(font)
        self.adim1Line.setObjectName("adim1Line")
        self.adim5Line = QtWidgets.QLineEdit(Form)
        self.adim5Line.setGeometry(QtCore.QRect(40, 603, 339, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.adim5Line.setFont(font)
        self.adim5Line.setObjectName("adim5Line")
        self.adim1label = QtWidgets.QLabel(Form)
        self.adim1label.setGeometry(QtCore.QRect(40, 354, 339, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adim1label.setFont(font)
        self.adim1label.setObjectName("adim1label")
        self.adim3label = QtWidgets.QLabel(Form)
        self.adim3label.setGeometry(QtCore.QRect(40, 466, 339, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adim3label.setFont(font)
        self.adim3label.setObjectName("adim3label")
        self.adim4Line = QtWidgets.QLineEdit(Form)
        self.adim4Line.setGeometry(QtCore.QRect(40, 547, 339, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.adim4Line.setFont(font)
        self.adim4Line.setObjectName("adim4Line")
        self.adim7label = QtWidgets.QLabel(Form)
        self.adim7label.setGeometry(QtCore.QRect(40, 690, 339, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adim7label.setFont(font)
        self.adim7label.setObjectName("adim7label")
        self.adim4label = QtWidgets.QLabel(Form)
        self.adim4label.setGeometry(QtCore.QRect(40, 522, 339, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adim4label.setFont(font)
        self.adim4label.setObjectName("adim4label")
        self.adim3Line = QtWidgets.QLineEdit(Form)
        self.adim3Line.setGeometry(QtCore.QRect(40, 491, 339, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.adim3Line.setFont(font)
        self.adim3Line.setObjectName("adim3Line")
        self.adim7Line = QtWidgets.QLineEdit(Form)
        self.adim7Line.setGeometry(QtCore.QRect(40, 715, 339, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.adim7Line.setFont(font)
        self.adim7Line.setObjectName("adim7Line")
        self.adim8label = QtWidgets.QLabel(Form)
        self.adim8label.setGeometry(QtCore.QRect(40, 746, 339, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adim8label.setFont(font)
        self.adim8label.setObjectName("adim8label")
        self.adim9Line = QtWidgets.QLineEdit(Form)
        self.adim9Line.setGeometry(QtCore.QRect(40, 827, 339, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.adim9Line.setFont(font)
        self.adim9Line.setObjectName("adim9Line")
        self.adim8Line = QtWidgets.QLineEdit(Form)
        self.adim8Line.setGeometry(QtCore.QRect(40, 771, 339, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.adim8Line.setFont(font)
        self.adim8Line.setObjectName("adim8Line")
        self.adim2Line = QtWidgets.QLineEdit(Form)
        self.adim2Line.setEnabled(True)
        self.adim2Line.setGeometry(QtCore.QRect(40, 435, 339, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.adim2Line.setFont(font)
        self.adim2Line.setObjectName("adim2Line")
        self.adim9label = QtWidgets.QLabel(Form)
        self.adim9label.setGeometry(QtCore.QRect(40, 802, 339, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adim9label.setFont(font)
        self.adim9label.setObjectName("adim9label")
        self.adim5label = QtWidgets.QLabel(Form)
        self.adim5label.setGeometry(QtCore.QRect(40, 578, 339, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adim5label.setFont(font)
        self.adim5label.setObjectName("adim5label")
        self.adim2label = QtWidgets.QLabel(Form)
        self.adim2label.setGeometry(QtCore.QRect(40, 410, 339, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adim2label.setFont(font)
        self.adim2label.setObjectName("adim2label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tarif Ekle"))
        self.label_10.setText(_translate("Form", "Kaç Kişilik:"))
        self.label_11.setText(_translate("Form", "Hazırlama Süresi (dk):"))
        self.label_12.setText(_translate("Form", "Pişirme Süresi (dk):"))
        self.label_16.setText(_translate("Form", "Adım Sayısı:"))
        self.label_14.setText(_translate("Form", "Malzeme Sayısı:"))
        self.label.setText(_translate("Form", "Tarifin Adı:"))
        self.ekleButon.setText(_translate("Form", "Ekle"))
        self.label_15.setText(_translate("Form", "Malzemeler"))
        self.malzeme7label.setText(_translate("Form", "7. Malzeme"))
        self.malzeme8label.setText(_translate("Form", "8. Malzeme"))
        self.malzeme6label.setText(_translate("Form", "6. Malzeme"))
        self.malzeme2label.setText(_translate("Form", "2. Malzeme"))
        self.malzeme5label.setText(_translate("Form", "5. Malzeme"))
        self.malzeme1label.setText(_translate("Form", "1. Malzeme"))
        self.malzeme3label.setText(_translate("Form", "3. Malzeme"))
        self.malzeme4label.setText(_translate("Form", "4. Malzeme"))
        self.label_13.setText(_translate("Form", "Yapılışı"))
        self.adim6label.setText(_translate("Form", "6. Adım"))
        self.adim1label.setText(_translate("Form", "1. Adım"))
        self.adim3label.setText(_translate("Form", "3. Adım"))
        self.adim7label.setText(_translate("Form", "7. Adım"))
        self.adim4label.setText(_translate("Form", "4. Adım"))
        self.adim8label.setText(_translate("Form", "8. Adım"))
        self.adim9label.setText(_translate("Form", "9. Adım"))
        self.adim5label.setText(_translate("Form", "5. Adım"))
        self.adim2label.setText(_translate("Form", "2. Adım"))
