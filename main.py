import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

import time

janela = ctk.CTk()
# Configrações do aplicativo
#Titulo
janela.title("UploadFiles with Python")
# Tamanho do App
janela.geometry("1280x700")#Tamanho do app
# Tema
janela._set_appearance_mode('dark')
# Icone
# Trava maxix e mini
janela.resizable(False,False)



# Frames
############################################################################ Perfil


frame_perfil = ctk.CTkFrame(janela,width=250,height=700).place(x=0,y=0)
text1 = ctk.CTkLabel(frame_perfil,text='Perfil',bg_color='transparent').place(x=5,y=5)







############################################################################ Área de upload
frame_principal = ctk.CTkFrame(janela,width=1029,height=700).place(x=252,y=0)
text2 = ctk.CTkLabel(frame_principal,text='Área de upload').place(x=750,y=0)


############################################################################ Seleção de arquivos

exibir_arquivo = ctk.CTkEntry(frame_principal, width=730, height=30).place(x=265, y=60)
selecao_arquivos = ctk.CTkButton(frame_principal, text='Selecione o arquivo...', width= 200,height=30).place(x=1000, y=60)
converter_arquivo = ctk.CTkButton(frame_principal, text= 'Converter arquivo', width=200, height=30).place(x=700, y=100)
renomear_arquivo = ctk.CTkButton(frame_principal, text= 'renomear arquivo', width=200, height=30).place(x=400, y=100)

############################################################################ Visualização de arquivos

frame_tabela = ctk.CTkFrame(janela, width=10, height=10)
frame_tabela.pack(padx=200,pady=150)

tabela = ttk.Treeview(frame_tabela, columns=('Descrição', 'Tamanho', 'Tipo'), show='headings')

tabela.heading('Descrição', text='DESCRIÇÃO')
tabela.heading('Tamanho', text='TAMANHO')
tabela.heading('Tipo', text='TIPO')

tabela.column('Descrição', width=200)
tabela.column('Tamanho', width=200)
tabela.column('Tipo', width=200)

tabela.pack(padx=10,pady=10,fill='both',expand=True)

info = [
    ('main.py', '250KBps', 'Projeto'),
    ('UHUM', '123KBps', 'Texto'),
    ('Laucher', '1GB', 'Exe')
]

for item in info:
    tabela.insert('','end',values=item)

############################################################################ Barra de status

barra_status = ctk.CTkProgressBar (frame_principal,width=950, height=10, orientation='horizontal').place(x=270, y=650)


janela.mainloop()