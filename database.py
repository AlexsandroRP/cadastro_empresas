import sqlite3


class Data_dase:
    
    def __init__(self, name = 'system.db') -> None:
        self.name = name
        
    def connect(self):
        self.connection = sqlite3.connect(self.name)
        
    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)
            
    def create_table_company(self):
        self.connect()
        cursor =  self.connection.cursor()
        cursor.execute("""
                    
                    CREATE TABLE IF NOT EXISTS Empresas(
                        
                        CNPJ TEXT,
                        NOME TEXT,
                        LOGRADOURO TEXT,
                        NUMERO TEXT,
                        COMPLEMENTO TEXT,
                        BAIRRO TEXT,
                        MUNICIPIO TEXT,
                        UF TEXT,
                        CEP TEXT,
                        TELEFONE TEXT,
                        EMAIL TEXT,

                        PRIMARY KEY(CNPJ)
                        );

                   
                         
                    """)
        
        self.close_connection()
        
    def register_company(self, fullDataSet):
        
        self.connect()
        campos_tabela = ('CNPJ','NOME','LOGRADOURO','NUMERO','COMPLEMENTO','BAIRRO','MUNICIPIO',
        'UF','CEP','TELEFONE','EMAIL')
        qntd = ("?,?,?,?,?,?,?,?,?,?,?")
        cursor = self.connection.cursor()
        
        try:
            cursor.execute(f"""INSERT INTO Empresas {campos_tabela}
                           
                           VALUES ({qntd})""", fullDataSet)
            self.connection.commit()
            return "OK", "Empresa cadastrada com sucesso!"
        except Exception as e:
            print(e)
            return 'erro', str(e)
            
        finally:
            self.close_connection()
            
    def select_all_companies(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Empresas ORDER BY NOME")
            empresas = cursor.fetchall()
            return empresas
        except Exception as e:
            print(e)
        finally:
            self.close_connection()
    
    def delete_company(self, cnpj):
        
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Empresas WHERE CNPJ = '{cnpj}'")
            self.connection.commit()
            return 'OK', "Empresa deletada com sucesso!"
        except Exception as e:
            return 'erro', str(e)
        finally:
            self.close_connection()
    
    def update_company(self, fullDataSet):
        
        self.connect()
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" UPDATE Empresas set
                        
                    CNPJ = '{fullDataSet[0]}',
                    NOME = '{fullDataSet[1]}',
                    LOGRADOURO = '{fullDataSet[2]}',
                    NUMERO = '{fullDataSet[3]}',
                    COMPLEMENTO = '{fullDataSet[4]}',
                    BAIRRO = '{fullDataSet[5]}',
                    MUNICIPIO = '{fullDataSet[6]}',
                    UF = '{fullDataSet[7]}',
                    CEP = '{fullDataSet[8]}',
                    TELEFONE = '{fullDataSet[9]}',
                    EMAIL = '{fullDataSet[10]}'

                    WHERE CNPJ = '{fullDataSet[0]}'""")                  
            self.connection.commit()
            return 'OK', 'Dados atualizado com sucesso!'
        except Exception as e:
            return "erro", str(e)
        finally:
            self.close_connection()
              
            
            
    