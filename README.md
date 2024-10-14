# Data Pipeline (Pipeline de Dados)

  ![image](https://github.com/user-attachments/assets/abbd5fdd-1a8a-4c07-9453-df766f01f497)


Um pipeline de dados refere-se ao fluxo automatizado de dados através de várias etapas, desde a origem até o destino final. No seu caso, o pipeline inclui:

-Criação dos dados (geração simulada),

-Armazenamento no banco de dados (SQLite),

-Visualização dos dados no Power BI.


### Criar um pequeno Data Warehouse no seu próprio PC:
Escolhi aqui o SQLite que é um banco de dados leve, que pode ser útil para protótipos ou pequenos Data Warehouses.

Baixe o arquivo executavel do SQLite do site https://www.sqlite.org/download.html

Extraia o arquivo zip > Adicione o SQLite ao seu caminho do sistema > Vá até Configurações Avançadas do Sistema > Variáveis de Ambiente. Em Variáveis do Sistema, selecione Path e clique em Editar, adicione o caminho do arquivo SQLite e clique em ok.

Abra o Prompt de Comando e digite > caminhe até a pasta do arquivo e digite o nome do executavel: sqlite3

Baixe o DB Browser for SQLite : https://sqlitebrowser.org/dl/

Faça a instalação.

#### Dados.py : Criação dos dados usados.
#### App.py : Aqui criei um dash para visualização dos dados e apresentação rápida.
![image](https://github.com/user-attachments/assets/04d8ba3d-401a-43f6-a7a9-e1a7eceacdad)

#### BD.py : Aqui exporto os dados já tratados para o banco de dados, SQLite.

### SQLite para Power BI

Consumo os dados criados, tratados e exportados para o banco de dados, para o Power Bi, criando dashboards.
- Primeiro baixe o DevartODBCSQLite.exe > https://marketplace.visualstudio.com/items?itemName=DevartSoftware.SQLiteODBCDriver3264bit
- Faça a instalação do arquivo acima.
- Vá em fontes de dados ODBC na pesquisa do windowns.
- Adicionar > procure, na pasta do seu projeto, o banco de dados > vá em configuração > database e coloque o caminho correto, caso não tenha ido automaticamente.
![image](https://github.com/user-attachments/assets/05bc30e9-58b0-42b5-85b1-c706ab41d0ef)

#### Power Bi:
- No power Bi vá em obter dados, na pagina inicial > ODBC > o DSN dos dados deve aparecer > ok
 ![image](https://github.com/user-attachments/assets/28bc3641-d320-4a3b-989f-a8123c0dc66e)

- Pronto!

  ![image](https://github.com/user-attachments/assets/a9729d55-05d1-4584-bbbe-ffef0d4ec4ea)



