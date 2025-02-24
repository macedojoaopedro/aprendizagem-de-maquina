import os
import csv

# Caminho do arquivo CSV (garantindo que está no diretório correto)
file_path = "C:\\Users\\negre\\OneDrive\\Documentos\\Aprendizagemdemaquina\\dados_cadastro.csv"

# Criar o arquivo caso não exista
if not os.path.exists(file_path):
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Data de Nascimento", "Dia do Cadastro", "Hora do Cadastro"])
        writer.writerow(["João Pedro", "1990-05-14", "2024-02-24", "14:30:15"])
        writer.writerow(["Pablo Vegetti", "1985-08-22", "2024-02-24", "10:12:45"])
        writer.writerow(["Dimitri Payet", "1992-11-30", "2024-02-24", "09:45:20"])
        writer.writerow(["Leo Jardim", "1998-04-10", "2024-02-24", "16:05:50"])
        writer.writerow(["Lamine Yamal", "2000-07-25", "2024-02-24", "12:22:33"])

print("Arquivo CSV verificado/criado com sucesso.")

# Solicita o número do registro ao usuário
n = int(input("Digite o número do registro (1 a 5): "))

# Lendo o arquivo CSV
def ler_registro(n):
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = list(csv.reader(file))
        if 1 <= n < len(reader):  # Ajuste na verificação do índice
            nome, data_nasc, data_cad, hora_cad = reader[n]
            data_nasc = "/".join(reversed(data_nasc.split("-")))  # Ajuste na formatação da data
            data_cad = "/".join(reversed(data_cad.split("-")))
            print(f"{nome}, {data_nasc}, {data_cad}, {hora_cad}")
        else:
            print("Registro inválido.")

ler_registro(n)
