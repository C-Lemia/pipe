import sqlite3
import pandas as pd

# Conectando (ou criando) o banco de dados SQLite
conn = sqlite3.connect('vendas.db')  # Isso cria um arquivo 'vendas.db' no diretório atual

# Carregar os dados de vendas do arquivo CSV
data = pd.read_csv('C:\\Users\\camil\\meu_projeto\\dados_vendas.csv')

# Verificar os dados carregados
print("Visualizando as primeiras linhas dos dados carregados:")
print(data.head())

# Inserindo os dados no SQLite
# Isso cria uma tabela chamada 'vendas' no banco de dados
data.to_sql('vendas', conn, if_exists='replace', index=False)

# Confirmando que os dados foram inseridos no SQLite
print("Dados inseridos no banco de dados SQLite 'vendas.db' com sucesso.")

# Fechar a conexão com o banco de dados SQLite
conn.close()

# Continuar com o processamento dos dados a partir do app.py

# Criar colunas de mês e ano a partir da data da venda
data['Data da Venda'] = pd.to_datetime(data['Data da Venda'])
data['Ano'] = data['Data da Venda'].dt.year
data['Mês'] = data['Data da Venda'].dt.strftime('%Y-%m')

# Somar as vendas por mês e por ano (baseado no valor total da venda)
monthly_sales = data.groupby(['Mês', 'Filial'])['Valor Total da Venda'].sum().reset_index()
annual_sales = data.groupby(['Ano', 'Filial'])['Valor Total da Venda'].sum().reset_index()

# Exportar dados mensais e anuais para Excel
with pd.ExcelWriter('dados_vendas.xlsx') as writer:
    monthly_sales.to_excel(writer, sheet_name='Vendas Mensais', index=False)
    annual_sales.to_excel(writer, sheet_name='Vendas Anuais', index=False)

print("Dados exportados para 'dados_vendas.xlsx' com sucesso.")
