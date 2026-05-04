# 🧹 Smart Directory Organizer (Desktop App)

Um utilitário de Desktop desenvolvido em Python para automação de Sistema Operacional. O aplicativo varre diretórios caóticos (como a pasta Downloads), analisa as extensões dos arquivos e os categoriza automaticamente em subpastas organizadas.

## ⚙️ Tecnologias e Arquitetura
* **Linguagem:** Python
* **Manipulação de SO (I/O):** Bibliotecas nativas `os` e `shutil` para leitura de caminhos, criação de diretórios e movimentação de dados em baixo nível.
* **Interface Gráfica (GUI):** `CustomTkinter` para a construção de um Front-End de Desktop moderno, responsivo e com dark-mode nativo, substituindo o visual obsoleto do Tkinter padrão.
* **Lógica de Roteamento:** Sistema de dicionários (Hash Maps) vinculando arrays de extensões de arquivos às suas respectivas pastas de destino.

## 🚀 Funcionalidades
* **Varredura Segura:** O script ignora subpastas existentes e foca apenas na triagem de arquivos soltos.
* **Criação Dinâmica:** Se a pasta de destino (ex: "Documentos" ou "Imagens") não existir, o motor de I/O a cria em tempo de execução.
* **Tratamento de Exceções:** Arquivos com extensões não mapeadas no dicionário principal são isolados em uma pasta de "Outros_Arquivos", garantindo que nenhum dado seja perdido ou corrompido durante a movimentação em massa.
* **Feedback Visual:** Atualização de status em tempo real na interface e pop-up de relatório ao final da operação indicando o volume de arquivos processados.

## 💻 Como Executar Localmente
1. Clone este repositório.
2. Instale a biblioteca de interface: `pip install -r requirements.txt`
3. Execute o aplicativo: `python app_organizador.py`
4. Selecione o diretório alvo através do prompt do sistema e inicie a varredura.
