import os
import shutil

def apagar_tudo(path):
    # Verifica se o caminho existe e se é um diretório
    if os.path.exists(path) and os.path.isdir(path):
        try:
            shutil.rmtree(path)  # Remove o diretório e seu conteúdo de forma segura
            print(f"A pasta '{path}' foi apagada com sucesso.")
        except Exception as e:
            print(f"Erro ao apagar a pasta '{path}': {e}")
    else:
        print(f"O caminho '{path}' não existe ou não é um diretório válido.")

# Exemplo de uso
apagar_tudo("/home/arthur/Área de trabalho/apagaapaga")
