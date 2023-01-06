import sqlite3
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from ui_main import Ui_MainWindow
from PySide2 import QtCore
import sys
from qt_material import apply_stylesheet
from functions import consulta_cnpj
from database import Data_dase
import pandas as pd

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PYTAX - Sistema de cadastro de empresas")
        appIcon = QIcon(":/icons/_imgs/folder.png")
        self.setWindowIcon(appIcon)
        
        self.db = Data_dase()
        self.search_companies()
        ################################################
        #BOTÃO MENU
        self.btn_menu.clicked.connect(self.leftMenu)
        ################################################
        
        ##############################################################################################
        #PÁGINAS DO SISTEMA
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_contatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contatos))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))        
        ###############################################################################################
        
        #######################################################
        # PREENCHER AUTOMATICAMENTE OS DADOS DO CNPJ
        self.txt_cnpj.editingFinished.connect(self.consult_api)
        ########################################################
        
        ###################################
        #CADASTRAR EMPRESA 
        self.btn_cadastrar.clicked.connect(self.register_company)
        #ALTERAR DADOS
        self.btn_alterar.clicked.connect(self.update_company)
        #EXCLUIR EMPRESA
        self.btn_excluir.clicked.connect(self.delete_company)
        #RELATÓRIO EXCEL
        self.btn_excel.clicked.connect(self.excel_report)
    
    def leftMenu(self):
        width = self.left_frame.width()
        
        if width == 0:
            newWidth = 200
        else:
            newWidth = 0
            
        self.animation = QtCore.QPropertyAnimation(self.left_frame, b'maximumWidth')
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    
    def consult_api(self):
        
        campos = consulta_cnpj(self.txt_cnpj.text())
        self.txt_nome.setText(campos[0])
        self.txt_logradouro.setText(campos[1])
        self.txt_num.setText(campos[2])
        self.txt_complemento.setText(campos[3])
        self.txt_bairro.setText(campos[4])
        self.txt_municipio.setText(campos[5])
        self.txt_uf.setText(campos[6])
        self.txt_cep.setText(campos[7])
        self.txt_telefone.setText(campos[8])
        self.txt_email.setText(campos[9])
           
    def register_company(self):
        
        fullDataSet = (
            
            self.txt_cnpj.text(), self.txt_nome.text(), self.txt_logradouro.text(),
            self.txt_num.text(), self.txt_complemento.text(),
            self.txt_bairro.text(), self.txt_municipio.text(),
            self.txt_uf.text(), self.txt_cep.text(), self.txt_telefone.text(),
            self.txt_email.text()
            
        )
        #CADASTAR NO BANCO
        resposta = self.db.register_company(fullDataSet)

        self.msg(resposta[0],resposta[1])
        self.search_companies()
  
    def msg(self, tipo, mensage):
        msgbox = QMessageBox()
        if tipo.lower() == 'ok':
            msgbox.setIcon(QMessageBox.Information)
        elif tipo.lower() == 'erro':
            msgbox.setIcon(QMessageBox.Critical)
        elif tipo.lower() == 'aviso':
            msgbox.setIcon(QMessageBox.Warning)
        
        msgbox.setText(mensage)
        msgbox.exec()
    
    def search_companies(self):
        
        result = self.db.select_all_companies()
        self.tb_empresas.clearContents()
        self.tb_empresas.setRowCount(len(result))
        
        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_empresas.setItem(row, column, QTableWidgetItem(str(data)))
  
    def update_company(self):
        
        data = []
        update_data = []     
        
        for row in range(self.tb_empresas.rowCount()):
            for column in range(self.tb_empresas.columnCount()):
                data.append(self.tb_empresas.item(row,column).text()) 
                
            update_data.append(data)
            data = []
            
        for comp in update_data:
            result = self.db.update_company(tuple(comp))
            
        self.msg(result[0],result[1])
            
        self.search_companies()
    
    def delete_company(self):
        
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído.")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()
        
        if resp == QMessageBox.Yes:
            cnpj = self.tb_empresas.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = self.db.delete_company(cnpj)
            self.search_companies()
            
            self.msg(result[0],result[1])
        
    def excel_report(self):
        cnx = sqlite3.connect('system.db')
        
        empresas = pd.read_sql_query("""SELECT * FROM Empresas""",con=cnx)
        empresas.to_excel("Empresas.xlsx", sheet_name='Empresas', index=False)

        self.msg('ok', 'Relatório gerador com sucesso!')
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    db = Data_dase()
    db.create_table_company()
    
    window = MainWindow()
    window.show()
    app.exec_()