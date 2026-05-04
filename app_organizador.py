import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

# 1. Configuração do Design da Interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# 2. A Inteligência de Classificação (O Dicionário de Regras)
CATEGORIAS = {
    "Imagens": ['.png', '.jpg', '.jpeg', '.gif', '.svg'],
    "Documentos": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.csv'],
    "Instaladores_e_Executaveis": ['.exe', '.msi', '.bat'],
    "Compactados": ['.zip', '.rar', '.7z'],
    "Áudios_e_Vídeos": ['.mp3', '.mp4', '.mkv', '.wav']
}

# 3. O Motor de Varredura (A Lógica Principal)
def organizar_pasta():
    # Abre aquela janela clássica do Windows para o usuário escolher a pasta
    pasta_alvo = filedialog.askdirectory(title="Selecione a pasta bagunçada")
    
    if not pasta_alvo:
        return # Se o usuário fechar a janela sem escolher nada, o robô aborta a missão
        
    lbl_status.configure(text=f"Iniciando varredura em: {pasta_alvo}...", text_color="yellow")
    app.update() # Força a interface a atualizar o texto imediatamente
    
    arquivos_movidos = 0
    
    # O robô lista tudo o que tem dentro da pasta selecionada
    for arquivo in os.listdir(pasta_alvo):
        caminho_completo = os.path.join(pasta_alvo, arquivo)
        
        # Ignora pastas, o alvo são apenas arquivos soltos
        if os.path.isdir(caminho_completo):
            continue
            
        # Separa o nome do arquivo da extensão (ex: "relatorio" e ".pdf")
        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower() # Converte para minúsculo por segurança
        
        # Procura em qual categoria essa extensão se encaixa
        pasta_destino = "Outros_Arquivos" # Categoria padrão caso a extensão seja desconhecida
        
        for categoria, extensoes in CATEGORIAS.items():
            if extensao in extensoes:
                pasta_destino = categoria
                break
                
        # Fabrica o caminho completo de onde o arquivo deveria estar
        caminho_destino_completo = os.path.join(pasta_alvo, pasta_destino)
        
        # Se a pasta da categoria (ex: "Imagens") ainda não existe, ele cria na hora
        if not os.path.exists(caminho_destino_completo):
            os.makedirs(caminho_destino_completo)
            
        # O Ataque: Move o arquivo do local original para dentro da nova pasta
        shutil.move(caminho_completo, os.path.join(caminho_destino_completo, arquivo))
        arquivos_movidos += 1
        
    # Relatório de Sucesso
    lbl_status.configure(text=f"Missão Cumprida! {arquivos_movidos} arquivos organizados.", text_color="#00FF00")
    messagebox.showinfo("Operação Concluída", f"Foram movidos {arquivos_movidos} arquivos para suas respectivas pastas!")

# 4. A Construção da Janela (O Front-End do Desktop)
app = ctk.CTk()
app.title("Central de Limpeza - CEO")
app.geometry("500x300")

lbl_titulo = ctk.CTkLabel(app, text="🧹 Motor de Organização de Diretórios", font=("Arial", 20, "bold"))
lbl_titulo.pack(pady=30)

lbl_desc = ctk.CTkLabel(app, text="Selecione uma pasta caótica (ex: Downloads) para varrer e\norganizar automaticamente todos os arquivos por tipo.", text_color="gray")
lbl_desc.pack(pady=10)

btn_iniciar = ctk.CTkButton(app, text="Selecionar Pasta e Iniciar Varredura", font=("Arial", 14, "bold"), command=organizar_pasta, width=300, height=45)
btn_iniciar.pack(pady=20)

lbl_status = ctk.CTkLabel(app, text="Aguardando ordens...", text_color="white")
lbl_status.pack(pady=10)

# Mantém a janela aberta rodando em loop
app.mainloop()