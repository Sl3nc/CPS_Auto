# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_cps.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 718)
        MainWindow.setMinimumSize(QSize(500, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.verticalLayout = QVBoxLayout(self.menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_menu = QVBoxLayout()
        self.header_menu.setObjectName(u"header_menu")
        self.logo_menu = QLabel(self.menu)
        self.logo_menu.setObjectName(u"logo_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_menu.sizePolicy().hasHeightForWidth())
        self.logo_menu.setSizePolicy(sizePolicy)
        self.logo_menu.setMinimumSize(QSize(580, 108))
        self.logo_menu.setPixmap(QPixmap(u"../imgs/cps_horizontal.png"))
        self.logo_menu.setScaledContents(True)

        self.header_menu.addWidget(self.logo_menu)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.header_menu.addItem(self.verticalSpacer)

        self.intro = QLabel(self.menu)
        self.intro.setObjectName(u"intro")
        sizePolicy.setHeightForWidth(self.intro.sizePolicy().hasHeightForWidth())
        self.intro.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(26)
        font.setBold(True)
        self.intro.setFont(font)
        self.intro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.header_menu.addWidget(self.intro)


        self.verticalLayout.addLayout(self.header_menu)

        self.options_cps = QGridLayout()
        self.options_cps.setObjectName(u"options_cps")
        self.pb_lucro = QPushButton(self.menu)
        self.pb_lucro.setObjectName(u"pb_lucro")
        self.pb_lucro.setMinimumSize(QSize(100, 50))

        self.options_cps.addWidget(self.pb_lucro, 0, 0, 1, 1)

        self.pb_pessoa = QPushButton(self.menu)
        self.pb_pessoa.setObjectName(u"pb_pessoa")
        self.pb_pessoa.setMinimumSize(QSize(0, 50))

        self.options_cps.addWidget(self.pb_pessoa, 1, 0, 1, 1)

        self.pb_inatividade = QPushButton(self.menu)
        self.pb_inatividade.setObjectName(u"pb_inatividade")
        self.pb_inatividade.setMinimumSize(QSize(100, 50))

        self.options_cps.addWidget(self.pb_inatividade, 0, 1, 1, 1)

        self.pb_simples = QPushButton(self.menu)
        self.pb_simples.setObjectName(u"pb_simples")
        self.pb_simples.setMinimumSize(QSize(0, 50))

        self.options_cps.addWidget(self.pb_simples, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.options_cps)

        self.stackedWidget.addWidget(self.menu)
        self.form = QWidget()
        self.form.setObjectName(u"form")
        self.verticalLayout_3 = QVBoxLayout(self.form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.header_form = QGridLayout()
        self.header_form.setObjectName(u"header_form")
        self.back_button = QPushButton(self.form)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setMaximumSize(QSize(100, 16777215))
        self.back_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.header_form.addWidget(self.back_button, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.header_form.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.header_form.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.header_form.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.titulo_id1 = QLabel(self.form)
        self.titulo_id1.setObjectName(u"titulo_id1")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(26)
        font1.setBold(True)
        self.titulo_id1.setFont(font1)
        self.titulo_id1.setScaledContents(True)
        self.titulo_id1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.header_form.addWidget(self.titulo_id1, 2, 1, 1, 1)

        self.logo_form = QLabel(self.form)
        self.logo_form.setObjectName(u"logo_form")
        self.logo_form.setMaximumSize(QSize(100, 75))
        self.logo_form.setPixmap(QPixmap(u"../imgs/cps_logo.png"))
        self.logo_form.setScaledContents(True)

        self.header_form.addWidget(self.logo_form, 2, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.header_form.addItem(self.verticalSpacer_2, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.header_form)

        self.intro_empresa = QHBoxLayout()
        self.intro_empresa.setObjectName(u"intro_empresa")
        self.titulo_empresa = QLabel(self.form)
        self.titulo_empresa.setObjectName(u"titulo_empresa")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titulo_empresa.sizePolicy().hasHeightForWidth())
        self.titulo_empresa.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(True)
        self.titulo_empresa.setFont(font2)

        self.intro_empresa.addWidget(self.titulo_empresa)

        self.line_3 = QFrame(self.form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 5))
        self.line_3.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.intro_empresa.addWidget(self.line_3)


        self.verticalLayout_3.addLayout(self.intro_empresa)

        self.grid_empresa = QGridLayout()
        self.grid_empresa.setObjectName(u"grid_empresa")
        self.label_cnpj_empresa = QLabel(self.form)
        self.label_cnpj_empresa.setObjectName(u"label_cnpj_empresa")

        self.grid_empresa.addWidget(self.label_cnpj_empresa, 0, 1, 1, 1)

        self.lineEdit_bairro_empresa = QLineEdit(self.form)
        self.lineEdit_bairro_empresa.setObjectName(u"lineEdit_bairro_empresa")

        self.grid_empresa.addWidget(self.lineEdit_bairro_empresa, 3, 1, 1, 1)

        self.lineEdit_cep_empresa = QLineEdit(self.form)
        self.lineEdit_cep_empresa.setObjectName(u"lineEdit_cep_empresa")
        self.lineEdit_cep_empresa.setMaxLength(9)

        self.grid_empresa.addWidget(self.lineEdit_cep_empresa, 1, 2, 1, 1)

        self.label_bairro_empresa = QLabel(self.form)
        self.label_bairro_empresa.setObjectName(u"label_bairro_empresa")

        self.grid_empresa.addWidget(self.label_bairro_empresa, 2, 1, 1, 1)

        self.lineEdit_nome_empresa = QLineEdit(self.form)
        self.lineEdit_nome_empresa.setObjectName(u"lineEdit_nome_empresa")

        self.grid_empresa.addWidget(self.lineEdit_nome_empresa, 1, 0, 1, 1)

        self.label_cep_empresa = QLabel(self.form)
        self.label_cep_empresa.setObjectName(u"label_cep_empresa")

        self.grid_empresa.addWidget(self.label_cep_empresa, 0, 2, 1, 1)

        self.lineEdit_complemento_empresa = QLineEdit(self.form)
        self.lineEdit_complemento_empresa.setObjectName(u"lineEdit_complemento_empresa")

        self.grid_empresa.addWidget(self.lineEdit_complemento_empresa, 3, 2, 1, 2)

        self.label_nome_empresa = QLabel(self.form)
        self.label_nome_empresa.setObjectName(u"label_nome_empresa")

        self.grid_empresa.addWidget(self.label_nome_empresa, 0, 0, 1, 1)

        self.label_endereco_empresa = QLabel(self.form)
        self.label_endereco_empresa.setObjectName(u"label_endereco_empresa")

        self.grid_empresa.addWidget(self.label_endereco_empresa, 0, 3, 1, 1)

        self.lineEdit_cnpj_empresa = QLineEdit(self.form)
        self.lineEdit_cnpj_empresa.setObjectName(u"lineEdit_cnpj_empresa")
        self.lineEdit_cnpj_empresa.setMaxLength(19)

        self.grid_empresa.addWidget(self.lineEdit_cnpj_empresa, 1, 1, 1, 1)

        self.label_numero_empresa = QLabel(self.form)
        self.label_numero_empresa.setObjectName(u"label_numero_empresa")

        self.grid_empresa.addWidget(self.label_numero_empresa, 2, 0, 1, 1)

        self.lineEdit_endereco_empresa = QLineEdit(self.form)
        self.lineEdit_endereco_empresa.setObjectName(u"lineEdit_endereco_empresa")

        self.grid_empresa.addWidget(self.lineEdit_endereco_empresa, 1, 3, 1, 1)

        self.label_complemento_empresa = QLabel(self.form)
        self.label_complemento_empresa.setObjectName(u"label_complemento_empresa")

        self.grid_empresa.addWidget(self.label_complemento_empresa, 2, 2, 1, 1)

        self.lineEdit_numero_empresa = QSpinBox(self.form)
        self.lineEdit_numero_empresa.setObjectName(u"lineEdit_numero_empresa")
        self.lineEdit_numero_empresa.setMinimum(1)
        self.lineEdit_numero_empresa.setMaximum(1000)

        self.grid_empresa.addWidget(self.lineEdit_numero_empresa, 3, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.grid_empresa)

        self.intro_repre = QHBoxLayout()
        self.intro_repre.setObjectName(u"intro_repre")
        self.titulo_repre = QLabel(self.form)
        self.titulo_repre.setObjectName(u"titulo_repre")
        sizePolicy1.setHeightForWidth(self.titulo_repre.sizePolicy().hasHeightForWidth())
        self.titulo_repre.setSizePolicy(sizePolicy1)
        self.titulo_repre.setFont(font2)

        self.intro_repre.addWidget(self.titulo_repre)

        self.line = QFrame(self.form)
        self.line.setObjectName(u"line")
        self.line.setWindowModality(Qt.WindowModality.NonModal)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setMinimumSize(QSize(0, 5))
        self.line.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.intro_repre.addWidget(self.line)

        self.titulo_quantidade = QLabel(self.form)
        self.titulo_quantidade.setObjectName(u"titulo_quantidade")
        sizePolicy1.setHeightForWidth(self.titulo_quantidade.sizePolicy().hasHeightForWidth())
        self.titulo_quantidade.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(True)
        self.titulo_quantidade.setFont(font3)

        self.intro_repre.addWidget(self.titulo_quantidade)

        self.comboBox_repre = QComboBox(self.form)
        self.comboBox_repre.addItem("")
        self.comboBox_repre.addItem("")
        self.comboBox_repre.addItem("")
        self.comboBox_repre.setObjectName(u"comboBox_repre")
        sizePolicy1.setHeightForWidth(self.comboBox_repre.sizePolicy().hasHeightForWidth())
        self.comboBox_repre.setSizePolicy(sizePolicy1)
        self.comboBox_repre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.intro_repre.addWidget(self.comboBox_repre)


        self.verticalLayout_3.addLayout(self.intro_repre)

        self.stackedWidget_2 = QStackedWidget(self.form)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_form_repre = QWidget()
        self.page_form_repre.setObjectName(u"page_form_repre")
        self.grid_repre = QGridLayout(self.page_form_repre)
        self.grid_repre.setObjectName(u"grid_repre")
        self.lineEdit_bairro_repre = QLineEdit(self.page_form_repre)
        self.lineEdit_bairro_repre.setObjectName(u"lineEdit_bairro_repre")

        self.grid_repre.addWidget(self.lineEdit_bairro_repre, 16, 0, 1, 1)

        self.lineEdit_cpf_repre = QLineEdit(self.page_form_repre)
        self.lineEdit_cpf_repre.setObjectName(u"lineEdit_cpf_repre")
        self.lineEdit_cpf_repre.setMaxLength(14)

        self.grid_repre.addWidget(self.lineEdit_cpf_repre, 1, 3, 1, 1)

        self.label_funcao_repre = QLabel(self.page_form_repre)
        self.label_funcao_repre.setObjectName(u"label_funcao_repre")

        self.grid_repre.addWidget(self.label_funcao_repre, 0, 0, 1, 1)

        self.label_rg_repre = QLabel(self.page_form_repre)
        self.label_rg_repre.setObjectName(u"label_rg_repre")

        self.grid_repre.addWidget(self.label_rg_repre, 0, 2, 1, 1)

        self.label_estado_civil_repre = QLabel(self.page_form_repre)
        self.label_estado_civil_repre.setObjectName(u"label_estado_civil_repre")

        self.grid_repre.addWidget(self.label_estado_civil_repre, 2, 0, 1, 1)

        self.label_orgao_repre = QLabel(self.page_form_repre)
        self.label_orgao_repre.setObjectName(u"label_orgao_repre")

        self.grid_repre.addWidget(self.label_orgao_repre, 0, 4, 1, 1)

        self.lineEdit_nome_repre = QLineEdit(self.page_form_repre)
        self.lineEdit_nome_repre.setObjectName(u"lineEdit_nome_repre")

        self.grid_repre.addWidget(self.lineEdit_nome_repre, 1, 1, 1, 1)

        self.label_nome_repre = QLabel(self.page_form_repre)
        self.label_nome_repre.setObjectName(u"label_nome_repre")

        self.grid_repre.addWidget(self.label_nome_repre, 0, 1, 1, 1)

        self.lineEdit_complemento_repre = QLineEdit(self.page_form_repre)
        self.lineEdit_complemento_repre.setObjectName(u"lineEdit_complemento_repre")

        self.grid_repre.addWidget(self.lineEdit_complemento_repre, 16, 3, 1, 2)

        self.label_numero_repre = QLabel(self.page_form_repre)
        self.label_numero_repre.setObjectName(u"label_numero_repre")

        self.grid_repre.addWidget(self.label_numero_repre, 2, 4, 1, 1)

        self.label_complemento_repre = QLabel(self.page_form_repre)
        self.label_complemento_repre.setObjectName(u"label_complemento_repre")

        self.grid_repre.addWidget(self.label_complemento_repre, 5, 3, 1, 1)

        self.label_bairro_repre = QLabel(self.page_form_repre)
        self.label_bairro_repre.setObjectName(u"label_bairro_repre")

        self.grid_repre.addWidget(self.label_bairro_repre, 5, 0, 1, 1)

        self.label_endereco_repre = QLabel(self.page_form_repre)
        self.label_endereco_repre.setObjectName(u"label_endereco_repre")

        self.grid_repre.addWidget(self.label_endereco_repre, 2, 3, 1, 1)

        self.lineEdit_rg_repre = QLineEdit(self.page_form_repre)
        self.lineEdit_rg_repre.setObjectName(u"lineEdit_rg_repre")
        self.lineEdit_rg_repre.setMaxLength(12)

        self.grid_repre.addWidget(self.lineEdit_rg_repre, 1, 2, 1, 1)

        self.lineEdit_orgao_repre = QLineEdit(self.page_form_repre)
        self.lineEdit_orgao_repre.setObjectName(u"lineEdit_orgao_repre")

        self.grid_repre.addWidget(self.lineEdit_orgao_repre, 1, 4, 1, 1)

        self.label_cidade_repre = QLabel(self.page_form_repre)
        self.label_cidade_repre.setObjectName(u"label_cidade_repre")

        self.grid_repre.addWidget(self.label_cidade_repre, 5, 1, 1, 1)

        self.lineEdit_cidade_repre = QLineEdit(self.page_form_repre)
        self.lineEdit_cidade_repre.setObjectName(u"lineEdit_cidade_repre")

        self.grid_repre.addWidget(self.lineEdit_cidade_repre, 16, 1, 1, 1)

        self.comboBox_estado_civil_repre = QComboBox(self.page_form_repre)
        self.comboBox_estado_civil_repre.addItem("")
        self.comboBox_estado_civil_repre.addItem("")
        self.comboBox_estado_civil_repre.addItem("")
        self.comboBox_estado_civil_repre.addItem("")
        self.comboBox_estado_civil_repre.addItem("")
        self.comboBox_estado_civil_repre.addItem("")
        self.comboBox_estado_civil_repre.setObjectName(u"comboBox_estado_civil_repre")

        self.grid_repre.addWidget(self.comboBox_estado_civil_repre, 3, 0, 1, 1)

        self.frame_nacio = QFrame(self.page_form_repre)
        self.frame_nacio.setObjectName(u"frame_nacio")
        sizePolicy1.setHeightForWidth(self.frame_nacio.sizePolicy().hasHeightForWidth())
        self.frame_nacio.setSizePolicy(sizePolicy1)
        self.frame_nacio.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_nacio.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_nacio)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_nacio = QLineEdit(self.frame_nacio)
        self.lineEdit_nacio.setObjectName(u"lineEdit_nacio")

        self.gridLayout_6.addWidget(self.lineEdit_nacio, 1, 0, 1, 1)

        self.pushButton_nacio = QPushButton(self.frame_nacio)
        self.pushButton_nacio.setObjectName(u"pushButton_nacio")

        self.gridLayout_6.addWidget(self.pushButton_nacio, 1, 1, 1, 1)

        self.checkBox_nacio_repre = QCheckBox(self.frame_nacio)
        self.checkBox_nacio_repre.setObjectName(u"checkBox_nacio_repre")

        self.gridLayout_6.addWidget(self.checkBox_nacio_repre, 0, 0, 1, 2)


        self.grid_repre.addWidget(self.frame_nacio, 2, 1, 1, 1)

        self.frame_cargo = QFrame(self.page_form_repre)
        self.frame_cargo.setObjectName(u"frame_cargo")
        sizePolicy1.setHeightForWidth(self.frame_cargo.sizePolicy().hasHeightForWidth())
        self.frame_cargo.setSizePolicy(sizePolicy1)
        self.frame_cargo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_cargo.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_cargo)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEdit_cargo = QLineEdit(self.frame_cargo)
        self.lineEdit_cargo.setObjectName(u"lineEdit_cargo")

        self.gridLayout_7.addWidget(self.lineEdit_cargo, 1, 0, 1, 1)

        self.pushButton_cargo = QPushButton(self.frame_cargo)
        self.pushButton_cargo.setObjectName(u"pushButton_cargo")

        self.gridLayout_7.addWidget(self.pushButton_cargo, 1, 1, 1, 1)

        self.checkBox_cargo_repre = QCheckBox(self.frame_cargo)
        self.checkBox_cargo_repre.setObjectName(u"checkBox_cargo_repre")

        self.gridLayout_7.addWidget(self.checkBox_cargo_repre, 0, 0, 1, 2)


        self.grid_repre.addWidget(self.frame_cargo, 3, 1, 1, 1)

        self.lineEdit_estado_repre = QLineEdit(self.page_form_repre)
        self.lineEdit_estado_repre.setObjectName(u"lineEdit_estado_repre")

        self.grid_repre.addWidget(self.lineEdit_estado_repre, 16, 2, 1, 1)

        self.lineEdit_endereco_repre = QLineEdit(self.page_form_repre)
        self.lineEdit_endereco_repre.setObjectName(u"lineEdit_endereco_repre")

        self.grid_repre.addWidget(self.lineEdit_endereco_repre, 3, 3, 1, 1)

        self.label_estado_repre = QLabel(self.page_form_repre)
        self.label_estado_repre.setObjectName(u"label_estado_repre")

        self.grid_repre.addWidget(self.label_estado_repre, 5, 2, 1, 1)

        self.lineEdit_cep_repre = QLineEdit(self.page_form_repre)
        self.lineEdit_cep_repre.setObjectName(u"lineEdit_cep_repre")
        self.lineEdit_cep_repre.setMaxLength(9)

        self.grid_repre.addWidget(self.lineEdit_cep_repre, 3, 2, 1, 1)

        self.comboBox_funcao_repre = QComboBox(self.page_form_repre)
        self.comboBox_funcao_repre.addItem("")
        self.comboBox_funcao_repre.addItem("")
        self.comboBox_funcao_repre.addItem("")
        self.comboBox_funcao_repre.setObjectName(u"comboBox_funcao_repre")

        self.grid_repre.addWidget(self.comboBox_funcao_repre, 1, 0, 1, 1)

        self.label_cpf_repre = QLabel(self.page_form_repre)
        self.label_cpf_repre.setObjectName(u"label_cpf_repre")

        self.grid_repre.addWidget(self.label_cpf_repre, 0, 3, 1, 1)

        self.label_cep_repre = QLabel(self.page_form_repre)
        self.label_cep_repre.setObjectName(u"label_cep_repre")

        self.grid_repre.addWidget(self.label_cep_repre, 2, 2, 1, 1)

        self.lineEdit_numero_repre = QSpinBox(self.page_form_repre)
        self.lineEdit_numero_repre.setObjectName(u"lineEdit_numero_repre")
        self.lineEdit_numero_repre.setMinimum(1)
        self.lineEdit_numero_repre.setMaximum(1000)

        self.grid_repre.addWidget(self.lineEdit_numero_repre, 3, 4, 1, 1)

        self.stackedWidget_2.addWidget(self.page_form_repre)
        self.page_show_cliente = QWidget()
        self.page_show_cliente.setObjectName(u"page_show_cliente")
        self.gridLayout_3 = QGridLayout(self.page_show_cliente)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.page_show_cliente)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tabWidget.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tab.setStyleSheet(u"background-color: white;")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_nome_clienteA = QLabel(self.tab)
        self.label_nome_clienteA.setObjectName(u"label_nome_clienteA")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_nome_clienteA.sizePolicy().hasHeightForWidth())
        self.label_nome_clienteA.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_nome_clienteA.setFont(font4)

        self.gridLayout_2.addWidget(self.label_nome_clienteA, 0, 0, 1, 1)

        self.label_cpf_clienteA = QLabel(self.tab)
        self.label_cpf_clienteA.setObjectName(u"label_cpf_clienteA")
        sizePolicy3.setHeightForWidth(self.label_cpf_clienteA.sizePolicy().hasHeightForWidth())
        self.label_cpf_clienteA.setSizePolicy(sizePolicy3)
        self.label_cpf_clienteA.setFont(font4)

        self.gridLayout_2.addWidget(self.label_cpf_clienteA, 2, 0, 1, 1)

        self.label_cpf_input_clienteA = QLabel(self.tab)
        self.label_cpf_input_clienteA.setObjectName(u"label_cpf_input_clienteA")
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(False)
        self.label_cpf_input_clienteA.setFont(font5)
        self.label_cpf_input_clienteA.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_cpf_input_clienteA, 2, 1, 1, 1)

        self.pushButton_clienteA = QPushButton(self.tab)
        self.pushButton_clienteA.setObjectName(u"pushButton_clienteA")
        font6 = QFont()
        font6.setFamilies([u"Yu Gothic UI"])
        font6.setPointSize(16)
        self.pushButton_clienteA.setFont(font6)
        self.pushButton_clienteA.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_clienteA.setStyleSheet(u"background-color: #E1E1E1;")
        icon = QIcon()
        icon.addFile(u"../imgs/engine.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_clienteA.setIcon(icon)
        self.pushButton_clienteA.setIconSize(QSize(32, 32))
        self.pushButton_clienteA.setFlat(False)

        self.gridLayout_2.addWidget(self.pushButton_clienteA, 2, 2, 1, 1)

        self.line_clienteA = QFrame(self.tab)
        self.line_clienteA.setObjectName(u"line_clienteA")
        self.line_clienteA.setFrameShape(QFrame.Shape.HLine)
        self.line_clienteA.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_clienteA, 1, 0, 1, 3)

        self.label_nome_input_clienteA = QLabel(self.tab)
        self.label_nome_input_clienteA.setObjectName(u"label_nome_input_clienteA")
        font7 = QFont()
        font7.setPointSize(16)
        self.label_nome_input_clienteA.setFont(font7)
        self.label_nome_input_clienteA.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_nome_input_clienteA, 0, 1, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"background-color: white;")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_nome_input_clienteB = QLabel(self.tab_2)
        self.label_nome_input_clienteB.setObjectName(u"label_nome_input_clienteB")
        self.label_nome_input_clienteB.setFont(font7)
        self.label_nome_input_clienteB.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_nome_input_clienteB, 0, 1, 1, 2)

        self.label_cpf_clienteB = QLabel(self.tab_2)
        self.label_cpf_clienteB.setObjectName(u"label_cpf_clienteB")
        sizePolicy3.setHeightForWidth(self.label_cpf_clienteB.sizePolicy().hasHeightForWidth())
        self.label_cpf_clienteB.setSizePolicy(sizePolicy3)
        self.label_cpf_clienteB.setFont(font4)

        self.gridLayout_4.addWidget(self.label_cpf_clienteB, 2, 0, 1, 1)

        self.label_cpf_input_clienteB = QLabel(self.tab_2)
        self.label_cpf_input_clienteB.setObjectName(u"label_cpf_input_clienteB")
        self.label_cpf_input_clienteB.setFont(font5)
        self.label_cpf_input_clienteB.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_cpf_input_clienteB, 2, 1, 1, 1)

        self.label_nome_clienteB = QLabel(self.tab_2)
        self.label_nome_clienteB.setObjectName(u"label_nome_clienteB")
        sizePolicy3.setHeightForWidth(self.label_nome_clienteB.sizePolicy().hasHeightForWidth())
        self.label_nome_clienteB.setSizePolicy(sizePolicy3)
        self.label_nome_clienteB.setFont(font4)

        self.gridLayout_4.addWidget(self.label_nome_clienteB, 0, 0, 1, 1)

        self.pushButton_clienteB = QPushButton(self.tab_2)
        self.pushButton_clienteB.setObjectName(u"pushButton_clienteB")
        self.pushButton_clienteB.setFont(font6)
        self.pushButton_clienteB.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_clienteB.setStyleSheet(u"background-color: #E1E1E1;")
        self.pushButton_clienteB.setIcon(icon)
        self.pushButton_clienteB.setIconSize(QSize(32, 32))
        self.pushButton_clienteB.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_clienteB, 2, 2, 1, 1)

        self.line_clienteB = QFrame(self.tab_2)
        self.line_clienteB.setObjectName(u"line_clienteB")
        self.line_clienteB.setFrameShape(QFrame.Shape.HLine)
        self.line_clienteB.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_clienteB, 1, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u"background-color: white;")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_nome_clienteC = QLabel(self.tab_3)
        self.label_nome_clienteC.setObjectName(u"label_nome_clienteC")
        sizePolicy3.setHeightForWidth(self.label_nome_clienteC.sizePolicy().hasHeightForWidth())
        self.label_nome_clienteC.setSizePolicy(sizePolicy3)
        self.label_nome_clienteC.setFont(font4)

        self.gridLayout_5.addWidget(self.label_nome_clienteC, 0, 0, 1, 1)

        self.label_nome_input_clienteC = QLabel(self.tab_3)
        self.label_nome_input_clienteC.setObjectName(u"label_nome_input_clienteC")
        self.label_nome_input_clienteC.setFont(font7)
        self.label_nome_input_clienteC.setStyleSheet(u"")
        self.label_nome_input_clienteC.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_nome_input_clienteC, 0, 1, 1, 2)

        self.line_clienteC = QFrame(self.tab_3)
        self.line_clienteC.setObjectName(u"line_clienteC")
        self.line_clienteC.setFrameShape(QFrame.Shape.HLine)
        self.line_clienteC.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_clienteC, 1, 0, 1, 3)

        self.label_cpf_clienteC = QLabel(self.tab_3)
        self.label_cpf_clienteC.setObjectName(u"label_cpf_clienteC")
        sizePolicy3.setHeightForWidth(self.label_cpf_clienteC.sizePolicy().hasHeightForWidth())
        self.label_cpf_clienteC.setSizePolicy(sizePolicy3)
        self.label_cpf_clienteC.setFont(font4)

        self.gridLayout_5.addWidget(self.label_cpf_clienteC, 2, 0, 1, 1)

        self.label_cpf_input_clienteC = QLabel(self.tab_3)
        self.label_cpf_input_clienteC.setObjectName(u"label_cpf_input_clienteC")
        self.label_cpf_input_clienteC.setFont(font5)
        self.label_cpf_input_clienteC.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_cpf_input_clienteC, 2, 1, 1, 1)

        self.pushButton_clienteC = QPushButton(self.tab_3)
        self.pushButton_clienteC.setObjectName(u"pushButton_clienteC")
        self.pushButton_clienteC.setFont(font6)
        self.pushButton_clienteC.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_clienteC.setStyleSheet(u"background-color: #E1E1E1;")
        self.pushButton_clienteC.setIcon(icon)
        self.pushButton_clienteC.setIconSize(QSize(32, 32))
        self.pushButton_clienteC.setFlat(False)

        self.gridLayout_5.addWidget(self.pushButton_clienteC, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_show_cliente)

        self.verticalLayout_3.addWidget(self.stackedWidget_2)

        self.intro_contrato = QHBoxLayout()
        self.intro_contrato.setObjectName(u"intro_contrato")
        self.titulo_contrato = QLabel(self.form)
        self.titulo_contrato.setObjectName(u"titulo_contrato")
        sizePolicy1.setHeightForWidth(self.titulo_contrato.sizePolicy().hasHeightForWidth())
        self.titulo_contrato.setSizePolicy(sizePolicy1)
        self.titulo_contrato.setFont(font2)

        self.intro_contrato.addWidget(self.titulo_contrato)

        self.line_2 = QFrame(self.form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 5))
        self.line_2.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.intro_contrato.addWidget(self.line_2)


        self.verticalLayout_3.addLayout(self.intro_contrato)

        self.grid_contrato = QGridLayout()
        self.grid_contrato.setObjectName(u"grid_contrato")
        self.pushButton_executar = QPushButton(self.form)
        self.pushButton_executar.setObjectName(u"pushButton_executar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_executar.sizePolicy().hasHeightForWidth())
        self.pushButton_executar.setSizePolicy(sizePolicy4)
        self.pushButton_executar.setMinimumSize(QSize(200, 0))
        self.pushButton_executar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.grid_contrato.addWidget(self.pushButton_executar, 0, 5, 3, 1)

        self.lineEdit_dt_inicio_contrato = QLineEdit(self.form)
        self.lineEdit_dt_inicio_contrato.setObjectName(u"lineEdit_dt_inicio_contrato")
        self.lineEdit_dt_inicio_contrato.setMaxLength(10)

        self.grid_contrato.addWidget(self.lineEdit_dt_inicio_contrato, 2, 1, 1, 1)

        self.lineEdit_dt_assinatura_contrato = QLineEdit(self.form)
        self.lineEdit_dt_assinatura_contrato.setObjectName(u"lineEdit_dt_assinatura_contrato")
        self.lineEdit_dt_assinatura_contrato.setMaxLength(10)

        self.grid_contrato.addWidget(self.lineEdit_dt_assinatura_contrato, 2, 2, 1, 1)

        self.lineEdit_valor_contrato = QDoubleSpinBox(self.form)
        self.lineEdit_valor_contrato.setObjectName(u"lineEdit_valor_contrato")
        sizePolicy4.setHeightForWidth(self.lineEdit_valor_contrato.sizePolicy().hasHeightForWidth())
        self.lineEdit_valor_contrato.setSizePolicy(sizePolicy4)
        self.lineEdit_valor_contrato.setMinimumSize(QSize(100, 0))
        self.lineEdit_valor_contrato.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.lineEdit_valor_contrato.setDecimals(2)
        self.lineEdit_valor_contrato.setMaximum(99999.990000000005239)
        self.lineEdit_valor_contrato.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.grid_contrato.addWidget(self.lineEdit_valor_contrato, 2, 0, 1, 1)

        self.lineEdit_num_empreg_contrato = QSpinBox(self.form)
        self.lineEdit_num_empreg_contrato.setObjectName(u"lineEdit_num_empreg_contrato")

        self.grid_contrato.addWidget(self.lineEdit_num_empreg_contrato, 2, 4, 1, 1)

        self.lineEdit_dia_vencimento_contrato = QSpinBox(self.form)
        self.lineEdit_dia_vencimento_contrato.setObjectName(u"lineEdit_dia_vencimento_contrato")
        self.lineEdit_dia_vencimento_contrato.setMinimum(1)
        self.lineEdit_dia_vencimento_contrato.setMaximum(30)

        self.grid_contrato.addWidget(self.lineEdit_dia_vencimento_contrato, 2, 3, 1, 1)

        self.label_valor_contrato = QLabel(self.form)
        self.label_valor_contrato.setObjectName(u"label_valor_contrato")

        self.grid_contrato.addWidget(self.label_valor_contrato, 1, 0, 1, 1)

        self.label_dt_inicio_contrato = QLabel(self.form)
        self.label_dt_inicio_contrato.setObjectName(u"label_dt_inicio_contrato")

        self.grid_contrato.addWidget(self.label_dt_inicio_contrato, 1, 1, 1, 1)

        self.label_dt_assinatura_contrato = QLabel(self.form)
        self.label_dt_assinatura_contrato.setObjectName(u"label_dt_assinatura_contrato")

        self.grid_contrato.addWidget(self.label_dt_assinatura_contrato, 1, 2, 1, 1)

        self.label_dia_vencimento_contrato = QLabel(self.form)
        self.label_dia_vencimento_contrato.setObjectName(u"label_dia_vencimento_contrato")

        self.grid_contrato.addWidget(self.label_dia_vencimento_contrato, 1, 3, 1, 1)

        self.label_num_empreg_contrato = QLabel(self.form)
        self.label_num_empreg_contrato.setObjectName(u"label_num_empreg_contrato")

        self.grid_contrato.addWidget(self.label_num_empreg_contrato, 1, 4, 1, 1)


        self.verticalLayout_3.addLayout(self.grid_contrato)

        self.stackedWidget.addWidget(self.form)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_menu.setText("")
        self.intro.setText(QCoreApplication.translate("MainWindow", u"Selecione o tipo de CPS que deseja fazer", None))
        self.pb_lucro.setText(QCoreApplication.translate("MainWindow", u"CPS Lucro Presumido / Real", None))
        self.pb_pessoa.setText(QCoreApplication.translate("MainWindow", u"CPS Pessoa F\u00edsica", None))
        self.pb_inatividade.setText(QCoreApplication.translate("MainWindow", u"CPS Inatividade", None))
        self.pb_simples.setText(QCoreApplication.translate("MainWindow", u"CPS Simples Nacional", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"Voltar ao menu", None))
        self.titulo_id1.setText(QCoreApplication.translate("MainWindow", u"Titulo", None))
        self.logo_form.setText("")
        self.titulo_empresa.setText(QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.label_cnpj_empresa.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.lineEdit_cep_empresa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"_____-___", None))
        self.label_bairro_empresa.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_cep_empresa.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.label_nome_empresa.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_endereco_empresa.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.lineEdit_cnpj_empresa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"__.___.___/____-__", None))
        self.label_numero_empresa.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.label_complemento_empresa.setText(QCoreApplication.translate("MainWindow", u"Complemento (opcional)", None))
        self.titulo_repre.setText(QCoreApplication.translate("MainWindow", u"Representante", None))
        self.titulo_quantidade.setText(QCoreApplication.translate("MainWindow", u"Quantidade: ", None))
        self.comboBox_repre.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_repre.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_repre.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))

        self.lineEdit_cpf_repre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"___.___.___-__", None))
        self.label_funcao_repre.setText(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o", None))
        self.label_rg_repre.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.label_estado_civil_repre.setText(QCoreApplication.translate("MainWindow", u"Estado Civil", None))
        self.label_orgao_repre.setText(QCoreApplication.translate("MainWindow", u"Org\u00e3o", None))
        self.label_nome_repre.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_numero_repre.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.label_complemento_repre.setText(QCoreApplication.translate("MainWindow", u"Complemento (opcional)", None))
        self.label_bairro_repre.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_endereco_repre.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.lineEdit_rg_repre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XX__.___.___", None))
        self.label_cidade_repre.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.comboBox_estado_civil_repre.setItemText(0, QCoreApplication.translate("MainWindow", u"Solteiro(a)", None))
        self.comboBox_estado_civil_repre.setItemText(1, QCoreApplication.translate("MainWindow", u"Divorciado(a)", None))
        self.comboBox_estado_civil_repre.setItemText(2, QCoreApplication.translate("MainWindow", u"Vi\u00favo(a)", None))
        self.comboBox_estado_civil_repre.setItemText(3, QCoreApplication.translate("MainWindow", u"Casado(a) em Separa\u00e7\u00e3o Total de Bens", None))
        self.comboBox_estado_civil_repre.setItemText(4, QCoreApplication.translate("MainWindow", u"Casado(a) em Comunh\u00e3o Parcial de Bens", None))
        self.comboBox_estado_civil_repre.setItemText(5, QCoreApplication.translate("MainWindow", u"Casado(a) em Comunh\u00e3o Universal de Bens", None))

        self.lineEdit_nacio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira a nacionalidade", None))
        self.pushButton_nacio.setText(QCoreApplication.translate("MainWindow", u"Desfazer", None))
        self.checkBox_nacio_repre.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o \u00e9 Brasileiro?", None))
        self.lineEdit_cargo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira o cargo", None))
        self.pushButton_cargo.setText(QCoreApplication.translate("MainWindow", u"Desfazer", None))
        self.checkBox_cargo_repre.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o \u00e9 Empres\u00e1rio?", None))
        self.label_estado_repre.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.lineEdit_cep_repre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"_____-___", None))
        self.comboBox_funcao_repre.setItemText(0, QCoreApplication.translate("MainWindow", u"S\u00f3cio", None))
        self.comboBox_funcao_repre.setItemText(1, QCoreApplication.translate("MainWindow", u"Adminstrador", None))
        self.comboBox_funcao_repre.setItemText(2, QCoreApplication.translate("MainWindow", u"Procurador", None))

        self.label_cpf_repre.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.label_cep_repre.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.label_nome_clienteA.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.label_cpf_clienteA.setText(QCoreApplication.translate("MainWindow", u"CPF: ", None))
        self.label_cpf_input_clienteA.setText("")
        self.pushButton_clienteA.setText(QCoreApplication.translate("MainWindow", u"Editar ", None))
        self.label_nome_input_clienteA.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Representante A", None))
        self.label_nome_input_clienteB.setText("")
        self.label_cpf_clienteB.setText(QCoreApplication.translate("MainWindow", u"CPF: ", None))
        self.label_cpf_input_clienteB.setText("")
        self.label_nome_clienteB.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.pushButton_clienteB.setText(QCoreApplication.translate("MainWindow", u"Editar ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Representante B", None))
        self.label_nome_clienteC.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.label_nome_input_clienteC.setText("")
        self.label_cpf_clienteC.setText(QCoreApplication.translate("MainWindow", u"CPF: ", None))
        self.label_cpf_input_clienteC.setText("")
        self.pushButton_clienteC.setText(QCoreApplication.translate("MainWindow", u"Editar ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Representante C", None))
        self.titulo_contrato.setText(QCoreApplication.translate("MainWindow", u"Contrato", None))
        self.pushButton_executar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.lineEdit_dt_inicio_contrato.setPlaceholderText(QCoreApplication.translate("MainWindow", u"__/__/____", None))
        self.lineEdit_dt_assinatura_contrato.setPlaceholderText(QCoreApplication.translate("MainWindow", u"__/__/____", None))
        self.lineEdit_valor_contrato.setPrefix(QCoreApplication.translate("MainWindow", u"R$ ", None))
        self.label_valor_contrato.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.label_dt_inicio_contrato.setText(QCoreApplication.translate("MainWindow", u"Data Inicio", None))
        self.label_dt_assinatura_contrato.setText(QCoreApplication.translate("MainWindow", u"Data Assinatura", None))
        self.label_dia_vencimento_contrato.setText(QCoreApplication.translate("MainWindow", u"Dia Vencimento", None))
        self.label_num_empreg_contrato.setText(QCoreApplication.translate("MainWindow", u"Num. Empregados", None))
    # retranslateUi

