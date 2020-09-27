# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import sys
from PyQt5.QtWidgets import *
import time
from PyQt5.QtCore import *
import os
import pyqrcode
from PyQt5.QtGui import *
from PIL import Image

wd = os.getcwd()
os.chdir(wd + "//")

# find local time/system time
time = QTime()
current_t = time.currentTime()
str_current_t = str(current_t)

a = "Successfully signed into "


# generate qr code function
def qr_gen(string):
	qr_code = pyqrcode.create(string)
	qr_code_img = qr_code.png(wd + "//code.png")
	return qr_code_img


class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(591, 287)

		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(53, 50, 91, 16))
		self.label.setObjectName("label")

		self.label_2 = QtWidgets.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(60, 80, 71, 16))
		self.label_2.setObjectName("label_2")

		self.label_3 = QtWidgets.QLabel(Dialog)
		self.label_3.setGeometry(QtCore.QRect(60, 110, 71, 16))
		self.label_3.setObjectName("label_3")

		self.label_4 = QtWidgets.QLabel(Dialog)
		self.label_4.setGeometry(QtCore.QRect(90, 150, 31, 16))
		self.label_4.setObjectName("label_4")

		self.label_5 = QtWidgets.QLabel(Dialog)
		self.label_5.setGeometry(QtCore.QRect(90, 190, 31, 16))
		self.label_5.setObjectName("label_5")

		self.lineEdit = QtWidgets.QLineEdit(Dialog)
		self.lineEdit.setGeometry(QtCore.QRect(145, 50, 201, 20))
		self.lineEdit.setObjectName("lineEdit")

		self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_2.setGeometry(QtCore.QRect(145, 80, 201, 20))
		self.lineEdit_2.setObjectName("lineEdit_2")

		self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_3.setGeometry(QtCore.QRect(145, 110, 201, 20))
		self.lineEdit_3.setObjectName("lineEdit_3")

		self.dateEdit = QtWidgets.QDateEdit(Dialog)
		self.dateEdit.setGeometry(QtCore.QRect(142, 150, 201, 22))
		self.dateEdit.setObjectName("dateEdit")
		self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

		self.timeEdit = QtWidgets.QTimeEdit(Dialog)
		self.timeEdit.setGeometry(QtCore.QRect(140, 190, 201, 22))
		self.timeEdit.setObjectName("timeEdit")
		self.timeEdit.setTime(current_t)

		self.QR_Code = QtWidgets.QLabel(Dialog)
		self.QR_Code.setGeometry(QtCore.QRect(380, 10, 181, 231))
		self.QR_Code.setText("")
		self.QR_Code.setObjectName("QR_Code")
		self.QR_Code.setScaledContents(True)

		self.pushButton = QtWidgets.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(150, 240, 81, 23))
		self.pushButton.setObjectName("pushButton")

		self.pushButton_2 = QtWidgets.QPushButton(Dialog)
		self.pushButton_2.setGeometry(QtCore.QRect(240, 240, 75, 23))
		self.pushButton_2.setObjectName("pushButton_2")

		self.save_btn = QtWidgets.QPushButton(Dialog)
		self.save_btn.setGeometry(QtCore.QRect(430, 250, 75, 23))
		self.save_btn.setObjectName("save_btn")

		self.pushButton.clicked.connect(self.on_click)
		self.pushButton_2.clicked.connect(self.on_click2)
		self.save_btn.clicked.connect(self.save_btn_func)
		# self.show()

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	# @pyqtSlot()
	def on_click(self):  # code to take user input generate the qr code
		Instructor_name = self.lineEdit.text()
		course_code = self.lineEdit_2.text()
		course_name = self.lineEdit_3.text()

		temp1 = self.timeEdit.time()
		time_class = str(temp1)

		temp = self.dateEdit.date()
		date_class = temp.toPyDate()

		b = a + course_code + ":" + course_name + " date " + str(date_class)  # +":"+time_class
		code = qr_gen(b)
		print(code)

		pixmap = QPixmap('code.png')
		self.QR_Code.setPixmap(pixmap)

	# self.resize(pixmap.width(),pixmap.height())
	# print(b)
	# date=self.dateEdit.text()
	# time=self.timeEdit.text()

	# print(code)

	# @pyqtSlot()
	def on_click2(self):  # code to reset the textfields and labels
		self.lineEdit.setText("")
		self.lineEdit_2.setText("")
		self.lineEdit_3.setText("")
		self.timeEdit.setTime(current_t)
		self.QR_Code.setText("")
		self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

	# self.dateEdit.setText("")
	# self.timeEdit.setText("")

	# @pyqtSlot()  # code to open file dialog to select where the user wants to save the code
	def save_btn_func(self):
		fname, filter = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '//', "Image Files (*.jpg)")

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "QR Code Generator"))
		Dialog.setWhatsThis(_translate("Dialog",
		                               "<html><head/><body><p><span style=\" font-weight:600;\">QR Code Generator</span></p></body></html>"))
		self.label.setText(_translate("Dialog", "<html><head/><body><p>Instructors Name:</p></body></html>"))
		self.label_2.setText(_translate("Dialog", "Course Code:"))
		self.label_3.setText(_translate("Dialog", "Course Name:"))
		self.label_4.setText(_translate("Dialog", "Date:"))
		self.label_5.setText(_translate("Dialog", "Time:"))
		self.pushButton.setText(_translate("Dialog", "Generate Code"))
		self.pushButton_2.setText(_translate("Dialog", "Refresh"))
		self.save_btn.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())
