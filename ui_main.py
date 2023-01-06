# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meu_cadastro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMaximumSize(QSize(200, 16777215))
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.PYTHONISTA = QFrame(self.left_frame)
        self.PYTHONISTA.setObjectName(u"PYTHONISTA")
        self.PYTHONISTA.setFrameShape(QFrame.StyledPanel)
        self.PYTHONISTA.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.PYTHONISTA)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.PYTHONISTA)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.PYTHONISTA)

        self.buttons_frame = QFrame(self.left_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMaximumSize(QSize(200, 16777215))
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.buttons_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.toolBox = QToolBox(self.buttons_frame)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMaximumSize(QSize(200, 16777215))
        self.toolBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 160, 382))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_home = QPushButton(self.widget)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.widget)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_cadastrar)

        self.btn_contatos = QPushButton(self.widget)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.widget)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.widget, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 160, 382))
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, u"Informa\u00e7\u00f5es")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.buttons_frame)


        self.horizontalLayout.addWidget(self.left_frame)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_container.sizePolicy().hasHeightForWidth())
        self.main_container.setSizePolicy(sizePolicy)
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_menu = QPushButton(self.top_frame)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu.setStyleSheet(u"background-color: None;")
        icon = QIcon()
        icon.addFile(u":/icons/_imgs/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(45, 45))

        self.horizontalLayout_2.addWidget(self.btn_menu, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy1)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        sizePolicy1.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy1)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.stackedWidget_2 = QStackedWidget(self.pg_home)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(-1, -1, 141, 161))
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.stackedWidget_2.addWidget(self.page_7)
        self.lbl_logo = QLabel(self.pg_home)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setGeometry(QRect(100, 100, 291, 231))
        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.horizontalLayout_4 = QHBoxLayout(self.pg_cadastro)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget = QTabWidget(self.pg_cadastro)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 60, 501, 255))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_telefone = QLineEdit(self.frame_2)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone, 6, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 2, 1, 1)

        self.txt_municipio = QLineEdit(self.frame_2)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio, 5, 0, 1, 3)

        self.txt_uf = QLineEdit(self.frame_2)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_uf, 5, 3, 1, 2)

        self.txt_email = QLineEdit(self.frame_2)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_email, 6, 2, 1, 4)

        self.txt_cep = QLineEdit(self.frame_2)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep, 5, 5, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 2, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 2, 1, 1)

        self.txt_cnpj = QLineEdit(self.frame_2)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        self.txt_cnpj.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cnpj, 2, 0, 1, 2)

        self.txt_logradouro = QLineEdit(self.frame_2)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.txt_logradouro, 3, 0, 1, 6)

        self.txt_num = QLineEdit(self.frame_2)
        self.txt_num.setObjectName(u"txt_num")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_num.sizePolicy().hasHeightForWidth())
        self.txt_num.setSizePolicy(sizePolicy2)
        self.txt_num.setMinimumSize(QSize(100, 0))
        self.txt_num.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_num, 4, 0, 1, 1)

        self.txt_complemento = QLineEdit(self.frame_2)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_complemento, 4, 1, 1, 3)

        self.txt_bairro = QLineEdit(self.frame_2)
        self.txt_bairro.setObjectName(u"txt_bairro")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txt_bairro.sizePolicy().hasHeightForWidth())
        self.txt_bairro.setSizePolicy(sizePolicy3)
        self.txt_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro, 4, 4, 1, 2)

        self.txt_nome = QLineEdit(self.frame_2)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 2, 2, 1, 4)

        self.btn_cadastrar_2 = QPushButton(self.tab)
        self.btn_cadastrar_2.setObjectName(u"btn_cadastrar_2")
        self.btn_cadastrar_2.setGeometry(QRect(190, 340, 180, 29))
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_cadastrar_2.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar_2.setSizePolicy(sizePolicy4)
        self.btn_cadastrar_2.setMinimumSize(QSize(180, 29))
        self.btn_cadastrar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_2.setLayoutDirection(Qt.RightToLeft)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 50, 531, 16))
        self.widget1 = QWidget(self.frame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 70, 531, 311))
        self.horizontalLayout_5 = QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tb_empresas = QTableWidget(self.widget1)
        if (self.tb_empresas.columnCount() < 11):
            self.tb_empresas.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tb_empresas.setObjectName(u"tb_empresas")

        self.horizontalLayout_5.addWidget(self.tb_empresas)

        self.frame_3 = QFrame(self.widget1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_excel = QPushButton(self.frame_3)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_excluir)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_9.addWidget(self.frame)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_11 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.pg_contatos)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_11.addWidget(self.label_7)

        self.frame_4 = QFrame(self.pg_contatos)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_10.setContentsMargins(210, -1, 9, -1)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_10.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_10.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_10.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_10.addWidget(self.label_11)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_12 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_12 = QLabel(self.pg_sobre)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_12.addWidget(self.label_12)

        self.label_13 = QLabel(self.pg_sobre)
        self.label_13.setObjectName(u"label_13")
        font = QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_13)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.footer_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(1)
        self.Pages.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/_imgs/pngegg.png\"/></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIO: Python", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.btn_menu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">SISTEMA DE CADASTRO</span></p></body></html>", None))
        self.lbl_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/_imgs/pngegg.png\"/></p></body></html>", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_num.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome empresarial", None))
        self.btn_cadastrar_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">EMPRESAS</p></body></html>", None))
        ___qtablewidgetitem = self.tb_empresas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tb_empresas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME EMPRESARIAL", None));
        ___qtablewidgetitem2 = self.tb_empresas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tb_empresas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None));
        ___qtablewidgetitem4 = self.tb_empresas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.tb_empresas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tb_empresas.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None));
        ___qtablewidgetitem7 = self.tb_empresas.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.tb_empresas.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.tb_empresas.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.tb_empresas.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"E-MAIL", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">CONTATOS</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/_imgs/whats.png\"/><span style=\" font-size:16pt; vertical-align:super;\">5199999999</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/_imgs/email.png\"/><span style=\" font-size:16pt; vertical-align:super;\">contato@python.com</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/_imgs/instagram.png\"/><span style=\" font-size:16pt; vertical-align:super;\">python</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/_imgs/youtube.png\"/><span style=\" font-size:16pt; vertical-align:super;\">Pythonista</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">SOBRE</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Esse sistema faz consulta de CNPJ utilizando uma API da receita federal e faz o cadastro em um banco de dados SQLITE3.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CopyRight 2022", None))
    # retranslateUi

