from PyQt5 import uic,QtWidgets
#import _mysql_connector

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    print("teste")
    print("codigo:", linha1)
    print("descricao:", linha2)
    print("preco", linha3)

    if formulario.radioButton.isChecked() :
        print("Categoria de Informática foi selecionada")
    elif formulario.radioButton_2.isChecked() :
        print("Categoria de Alimentação foi selecionada")
    else :
        print("Categoria de Eletrônicos foi selecionada")    



app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)    

formulario.show()

app.exec()

# Criando Tabelas:

'''
create table produtos(
    id INT NOT NULL AUTO_INCREMENT,
    codigo INT,
    descricao VARCHAR(50),
    preco DOUBLE,
    categoria VARCHAR(20),
    PRIMARY KEY (id)
);    
'''

# inserindo registros na tabela

#INSERT INTO produtos(codigo, descricao, preco, categoria)
#VALUES (123, "Impressora", 300,00)
