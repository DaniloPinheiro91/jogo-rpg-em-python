import subprocess

# Executar pip freeze para obter as dependências instaladas
requirements = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
requirements_text = requirements.stdout

# Salvar no arquivo requirements.txt na raiz do projeto
with open("requirements.txt", "w") as f:
    f.write(requirements_text)

print("Arquivo requirements.txt gerado com sucesso.")
