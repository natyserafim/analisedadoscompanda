import pandas as pd

# Criando um DataFrame fictício com dados de atendimentos
data = {
    'ID': [1, 2, 3, 4, 5],
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'Idade': [25, 30, 22, 35, 28],
    'Data Atendimento': ['2024-09-01', '2024-09-02', '2024-09-01', '2024-09-03', '2024-09-02'],
    'Tipo Atendimento': ['Psicologia', 'Assistência Social', 'Psicologia', 'Assistência Social', 'Educação'],
    'Satisfação': [4, 5, 3, 4, 2]  # Escala de 1 a 5
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Convertendo a coluna de Data Atendimento para datetime
df['Data Atendimento'] = pd.to_datetime(df['Data Atendimento'])

# Análise básica
# 1. Resumo dos dados
print("Resumo dos Dados:")
print(df.describe())

# 2. Contagem de atendimentos por tipo
contagem_tipo = df['Tipo Atendimento'].value_counts()
print("\nContagem de Atendimentos por Tipo:")
print(contagem_tipo)

# 3. Média de satisfação
media_satisfacao = df['Satisfação'].mean()
print("\nMédia de Satisfação dos Atendimentos:")
print(media_satisfacao)

# 4. Atendimentos por mês
df['Mês'] = df['Data Atendimento'].dt.month
atendimentos_por_mes = df['Mês'].value_counts()
print("\nAtendimentos por Mês:")
print(atendimentos_por_mes)
