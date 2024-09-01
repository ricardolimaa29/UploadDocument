import customtkinter as ctk
import time
from PIL import Image,ImageTk
from pyautogui import mouseInfo



font_text_name = ('Arial 20')

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

# Foto Perfil
img= (Image.open("UploadDocument\imagens\perfil.png"))
resized_image= img.resize((250,240))
my_img=ImageTk.PhotoImage(resized_image)
# Fontes
nome_text_font = ctk.CTkFont(family='Arial',size=20)
perfil_font_text = ctk.CTkFont(family='Arial', size=15)

# Foto Nuvem
img= (Image.open(f"UploadDocument\imagens\\nuvem.png"))
resized_image= img.resize((20,20))
my_imgNuvem=ImageTk.PhotoImage(resized_image)



frame_perfil = ctk.CTkFrame(janela,width=250,height=700).place(x=0,y=0)

#colocando a imagem em Label e customizando
perfil_profile = ctk.CTkLabel(frame_perfil, image=my_img,text="").place(x=0, y=0)
nome = ctk.CTkLabel(frame_perfil,text='Ana Carolina',bg_color='#2B2B2B',font=nome_text_font).place(x=70,y=250)

barra_status = ctk.CTkProgressBar(frame_perfil, width=200,height=2,orientation='horizontal',progress_color='Red').place(x=5,y=650)




############################################################################ Área de upload
frame_principal = ctk.CTkFrame(janela,width=1029,height=700).place(x=252,y=0)
text2 = ctk.CTkLabel(frame_principal,text='Área de upload').place(x=750,y=0)


############################################################################ Seleção de arquivos


exibir_arquivo = ctk.CTkEntry(frame_principal, width=730, height=30).place(x=265, y=60)
selecao_arquivos = ctk.CTkButton(frame_principal, text='Selecione o arquivo...', width= 200,height=30).place(x=1000, y=60)
converter_arquivo = ctk.CTkButton(frame_principal, text= 'Converter arquivo', width=200, height=30).place(x=700, y=100)
renomear_arquivo = ctk.CTkButton(frame_principal, text= 'renomear arquivo', width=200, height=30).place(x=400, y=100)

############################################################################ Barra de status

text_utilizado = ctk.CTkLabel(frame_perfil,text='Armazenamento',bg_color='#2B2B2B',font=perfil_font_text).place(x=35,y=620)
nuvem = ctk.CTkLabel(frame_perfil, image=my_imgNuvem,text="",bg_color='#2B2B2B').place(x=10, y=620)
textInfoArmazenamento = ctk.CTkLabel(frame_perfil,text="7,14 GB de 15 GB usados",bg_color='#2B2B2B',font=perfil_font_text).place(x=5,y=660)

janela.mainloop()