import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import time
from tkinter import filedialog


janela = ctk.CTk()
# Configrações do aplicativo
#Titulo
janela.title("UploadFiles with Python")
# Tamanho do App
janela.geometry("1280x700")#Tamanho do app
# Tema
janela._set_appearance_mode('light')
# Icone
# Trava maxix e mini
janela.resizable(False,False)

### Fontes
perfil_font_text = ctk.CTkFont('Arial',size=20)
status_font_text = ctk.CTkFont('Arial', size=15)


# Functions
def selecione():
    destino = filedialog.askopenfilename()







# Frames
############################################################################ Perfil

############ Imagens

# Icone Nuvem
img= (Image.open("UploadDocument\imagens\\nuvem.png"))
resized_image= img.resize((25,25))
my_imgNuvem=ImageTk.PhotoImage(resized_image)
# Foto perfil
img= (Image.open("UploadDocument\imagens\perfil.png"))
resized_image= img.resize((250,250))
my_img=ImageTk.PhotoImage(resized_image)


frame_perfil = ctk.CTkFrame(janela,width=250,height=700).place(x=0,y=0)
foto_perfil = ctk.CTkLabel(frame_perfil, image=my_img,text="",bg_color='#2B2B2B').place(x=0, y=0)

text_utilizado = ctk.CTkLabel(frame_perfil,text='Armazenamento',bg_color='#2B2B2B',font=perfil_font_text).place(x=35,y=615)
nuvem = ctk.CTkLabel(frame_perfil, image=my_imgNuvem,text="",bg_color='#2B2B2B').place(x=5, y=620)
barra_status_perfil = ctk.CTkProgressBar (frame_perfil,width=210, height=5, orientation='horizontal',bg_color="#2B2B2B",progress_color="Red").place(x=5, y=650)
textInfoArmazenamento = ctk.CTkLabel(frame_perfil,text="7,14 GB de 15 GB usados",bg_color='#2B2B2B',font=status_font_text).place(x=5,y=660)





############################################################################ Área de upload
frame_principal = ctk.CTkFrame(janela,width=1029,height=700).place(x=252,y=0)
text2 = ctk.CTkLabel(frame_principal,text='Área de upload').place(x=750,y=0)


############################################################################ Seleção de arquivos

exibir_arquivo = ctk.CTkEntry(frame_principal, width=730, height=30).place(x=265, y=60)
selecao_arquivos = ctk.CTkButton(frame_principal, text='Selecione o arquivo...', width= 200,height=30,command=selecione).place(x=1000, y=60)
converter_arquivo = ctk.CTkButton(frame_principal, text= 'Converter arquivo', width=200, height=30).place(x=700, y=100)
renomear_arquivo = ctk.CTkButton(frame_principal, text= 'renomear arquivo', width=200, height=30).place(x=400, y=100)

############################################################################ Visualização de arquivos

frame_tabela = ctk.CTkFrame(frame_principal, width=10, height=10)
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
    ('main.py', '250KBps', '.py'),
    ('UHULL', '123KBps', 'Texto'),
    ('Laucher', '1GB', 'Exe')
]

for item in info:
    tabela.insert('','end',values=item)

############################################################################ Barra de status

barra_status = ctk.CTkProgressBar (frame_principal,width=950, height=10, orientation='horizontal').place(x=270, y=650)


janela.mainloop()#### Barra de status
