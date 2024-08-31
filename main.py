import customtkinter as ctk


janela = ctk.CTk()
# Configrações do aplicativo
#Titulo
janela.title("UploadFiles with Python")
# Tamanho do App
janela.geometry("1280x700")#Tamanho do app
# Tema
janela._set_appearance_mode('dark-green')
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



janela.mainloop()