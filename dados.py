import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Função para gerar dados de vendas
def generate_sales_data(num_records=1000):
    np.random.seed(42)
    
    # Nome das lojas e as respectivas cidades
    stores_info = {
        'Loja A': 'São Paulo',
        'Loja B': 'Rio de Janeiro',
        'Loja C': 'Belo Horizonte',
        'Loja D': 'Curitiba'
    }
    
    # Produtos vendidos nas lojas e seus valores unitários
    product_price = {
        'Camiseta': 50,
        'Calça': 120,
        'Jaqueta': 200,
        'Vestido': 150,
        'Saia': 80,
        'Blusa': 70,
        'Short': 60,
        'Casaco': 180
    }
    
    # Gera datas aleatórias no intervalo dos últimos dois anos
    dates = [datetime.now() - timedelta(days=random.randint(0, 730)) for _ in range(num_records)]
    
    # Atribui filiais aleatoriamente
    stores = [random.choice(list(stores_info.keys())) for _ in range(num_records)]
    
    # Atribui cidade correspondente à loja
    cities = [stores_info[store] for store in stores]
    
    # Atribui produtos aleatoriamente e seus valores unitários
    products = [random.choice(list(product_price.keys())) for _ in range(num_records)]
    product_unit_prices = [product_price[product] for product in products]
    
    # Gera quantidade vendida de cada produto (entre 1 e 10 unidades)
    quantities = np.random.randint(1, 10, size=num_records)
    
    # Calcula o valor total da venda (quantidade * valor unitário)
    sales_values = np.array(product_unit_prices) * quantities
    
    # Cria um dataframe
    data = pd.DataFrame({
        'Data da Venda': dates,
        'Filial': stores,
        'Cidade': cities,
        'Produto': products,
        'Quantidade Vendida': quantities,
        'Valor Unitário': product_unit_prices,
        'Valor Total da Venda': sales_values
    })
    
    return data

# Função para salvar os dados em CSV para integração futura com Power BI
def save_to_csv(data, file_path='dados_vendas.csv'):
    data.to_csv(file_path, index=False)
    print(f'Dados salvos em {file_path}')

# Gerando e salvando os dados
sales_data = generate_sales_data()
save_to_csv(sales_data)
