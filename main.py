import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import time
from tkinter import filedialog
from CTkTable import *


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


### Fontes
perfil_font_text = ctk.CTkFont('Arial',size=20)
status_font_text = ctk.CTkFont('Arial', size=15)


# Functions
def selecione():
    
    destino = filedialog.askopenfilename()
    exibir_arquivo.delete(0,ctk.END)
    exibir_arquivo.insert(0, destino)
    selecao_arquivos.configure(text="Arquivo Selecionado")

def selecao_opcoes_drop(resultado):
     print('erro', resultado)

def verificar():
    selecione()

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


############################################################################ Área do Frame Principal
frame_principal = ctk.CTkFrame(janela,width=1209,height=700).place(x=252,y=0)
info = [
    ('main.py', '250KBps', 'py'),
    ('bloco.txt', '123KBps', 'txt'),
    ('Laucher.exe', '1GB', 'exe'),
    ('lua.jpg', '123KBps', 'jpg'),
    ('PB', '4GB', 'exe'),
    ('musica', '250KBps', 'mp3'),
    ('arq.zip', '1GB', 'zip'),
    ('filme', '2GB', 'mp4'),
    ('vscode', '1GB', 'exe')
]


tabela = CTkTable(janela,width=10, values=info,header_color="#4169e1",corner_radius=15,color_phase="horizontal",command=getattr,border_color="white",hover_color="#1f29c6")
tabela.pack(fill="both", padx=252, pady=200)




############################ Seleção de arquivos

exibir_arquivo = ctk.CTkEntry(frame_principal,placeholder_text="Teste", width=730, height=30)
exibir_arquivo.place(x=265, y=60)
selecao_arquivos = ctk.CTkButton(frame_principal, text='Selecione o arquivo...', width= 200,height=30,command=selecione)
selecao_arquivos.place(x=1000, y=60)
verificacao = ctk.CTkButton(frame_principal, text= 'Verificar', width=200, height=30, command=verificar).place(x=700, y=100)



dropdown = ctk.CTkComboBox(janela, values=['Local', 'Nuvem'], command=selecao_opcoes_drop)
dropdown.set('selecione')
dropdown.place(x=265, y=100)



############################ Visualização de arquivos





############################################################################ Barra de status

barra_status = ctk.CTkProgressBar (frame_principal,width=950, height=10, orientation='horizontal').place(x=270, y=650)


janela.mainloop()#### Barra de status
