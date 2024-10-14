import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Carregar dados de vendas do arquivo CSV gerado
data = pd.read_csv('C:\\Users\\camil\\meu_projeto\\dados_vendas.csv')

# Verificar os dados carregados
print(data.head())

# Criar colunas de mês e ano a partir da data da venda
data['Data da Venda'] = pd.to_datetime(data['Data da Venda'])
data['Ano'] = data['Data da Venda'].dt.year
data['Mês'] = data['Data da Venda'].dt.strftime('%Y-%m')

# Somar as vendas por mês e por ano (baseado no valor total da venda)
monthly_sales = data.groupby(['Mês', 'Filial', 'Cidade', 'Produto'])['Valor Total da Venda'].sum().reset_index()
annual_sales = data.groupby(['Ano', 'Filial', 'Cidade', 'Produto'])['Valor Total da Venda'].sum().reset_index()

# Criar a aplicação Dash
app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Dashboard de Vendas e Faturamento"),

    html.Label("Selecione uma Filial:"),
    dcc.Dropdown(
        id='filial-dropdown',
        options=[{'label': filial, 'value': filial} for filial in data['Filial'].unique()],
        value='Loja A',  # Valor padrão
        clearable=False
    ),

    html.Label("Selecione uma Cidade:"),
    dcc.Dropdown(
        id='cidade-dropdown',
        options=[{'label': cidade, 'value': cidade} for cidade in data['Cidade'].unique()],
        value=None,
        clearable=True
    ),

    html.Label("Selecione um Produto:"),
    dcc.Dropdown(
        id='produto-dropdown',
        options=[{'label': produto, 'value': produto} for produto in data['Produto'].unique()],
        value=None,
        clearable=True
    ),

    dcc.Graph(id='grafico-mensal'),
    dcc.Graph(id='grafico-anual')
])

# Callback para atualizar os gráficos com base nas seleções
@app.callback(
    [Output('grafico-mensal', 'figure'), Output('grafico-anual', 'figure')],
    [Input('filial-dropdown', 'value'), 
     Input('cidade-dropdown', 'value'), 
     Input('produto-dropdown', 'value')]
)
def update_graphs(selected_store, selected_city, selected_product):
    # Filtrar os dados da filial selecionada
    filtered_monthly_sales = monthly_sales[monthly_sales['Filial'] == selected_store]
    filtered_annual_sales = annual_sales[annual_sales['Filial'] == selected_store]

    # Filtrar por cidade, se uma cidade for selecionada
    if selected_city:
        filtered_monthly_sales = filtered_monthly_sales[filtered_monthly_sales['Cidade'] == selected_city]
        filtered_annual_sales = filtered_annual_sales[filtered_annual_sales['Cidade'] == selected_city]

    # Filtrar por produto, se um produto for selecionado
    if selected_product:
        filtered_monthly_sales = filtered_monthly_sales[filtered_monthly_sales['Produto'] == selected_product]
        filtered_annual_sales = filtered_annual_sales[filtered_annual_sales['Produto'] == selected_product]

    # Criar gráfico mensal
    fig_monthly = px.bar(
        filtered_monthly_sales, x='Mês', y='Valor Total da Venda',
        title=f'Faturamento Mensal - {selected_store}',
        labels={'Valor Total da Venda': 'Faturamento (R$)', 'Mês': 'Mês'}
    )
    
    # Criar gráfico anual
    fig_annual = px.line(
        filtered_annual_sales, x='Ano', y='Valor Total da Venda', 
        title=f'Faturamento Anual - {selected_store}',
        labels={'Valor Total da Venda': 'Faturamento (R$)', 'Ano': 'Ano'}
    )
    
    return fig_monthly, fig_annual

# Executar o app
if __name__ == '__main__':
    app.run_server(debug=True)
