<!--START_SECTION:header-->
<div align="center">
  <p align="center">
    <img 
      alt="DIO Education" 
      src="./assets/AzureCloudnative.webp" 
      width="100px" 
    />
    <h1>Azure Cloud Native - Microsoft - Dio</h1>
  </p>
</div>
<!--END_SECTION:header-->

<br/>

## 💻 Sobre o Projeto

Este bootcamp oferece uma formação prática e intensiva voltada para o desenvolvimento, implantação e gerenciamento de aplicações modernas na plataforma Microsoft Azure. Aprender a utilizar serviços como App Services e Azure Container Apps, além de explorarem os fundamentos de DevOps aplicados ao ecossistema da Microsoft, preparando-se para atuar com soluções em nuvem escaláveis e eficientes.

## 🗄️ Tabela `Produtos` – Azure SQL

A tabela abaixo será criada no banco de dados Azure SQL para armazenar as informações dos produtos da aplicação. Ela inclui um campo image_url, que será utilizado para registrar a URL da imagem associada a cada produto.

```
CREATE TABLE Produtos (
id INT IDENTITY(1,1) PRIMARY KEY,
nome NVARCHAR(200),
descricao NVARCHAR(MAX),
preco DECIMAL(18,2),
imagem_url NVARCHAR(2083)
)
```

## ✅ Pré-requisitos

Antes de executar o projeto, verifique se os seguintes pré-requisitos estão atendidos:

### 🐍 Ambiente Python

- Python 3.8 ou superior
- Gerenciador de pacotes `pip`

📦 Bibliotecas Python utilizadas

Certifique-se de instalar as dependências abaixo (elas também podem ser listadas em um requirements.txt):

🧩 Bibliotecas utilizadas no código:

```
import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pymssql
import uuid
import json
from dotenv import load_dotenv
```

```
pip install -r requirements.txt
# ou
pip install streamlit azure-storage-blob pymssql python-dotenv


```

📁 Variáveis de ambiente

Crie um arquivo .env na raiz do projeto com as seguintes configurações (exemplo):

```
# Configurações do Azure Blob Storage
BLOB_CONNECTION_STRING=""  # Sua string de conexão do Azure Blob Storage
BLOB_CONTAINER_NAME=""      # Nome do container do Azure Blob Storage
BLOB_ACCOUNT_NAME=""        # Nome da conta do Azure Blob Storage

# Configurações do Banco de Dados SQL (Azure SQL)
SQL_SERVER=""               # Nome do servidor SQL no Azure (ex: seu_servidor.database.windows.net)
SQL_DATABASE=""             # Nome do banco de dados no Azure SQL
SQL_USERNAME=""             # Nome de usuário para conexão com o banco de dados SQL
SQL_PASSWORD=""             # Senha para o usuário do banco de dados SQL

```

## 📚 Pré-requisitos de Habilidades e Níveis de Conhecimento

Antes de ingressar neste conteúdo, é necessário possuir conhecimento prévio nas seguintes áreas:

- Azure | Básico

- Git e GitHub | Básico

- Lógica de Programação | Intermediário

- Conhecimentos de Desenvolvimento Web | Intermediário

- Terminal/CLI | Básico

Outros pré-requisitos:

- Desejável experiência com alguma linguagem de programação como C#, JavaScript ou Python.

## 🛠️ Habilidades e Sub-habilidades que vamos aprender neste conteúdo

- Fundamentos da Plataforma Azure

  - App Services

  - Azure CLI e Portal

  - Armazenamento de dados

- Contêineres e Orquestração

  - Azure Container Apps
  - Azure Kubernetes Service (AKS)
  - Deploy de aplicações em contêiner

- Monitoramento e Performance

  - Application Insights
  - Log Analytics
  - Práticas de Observabilidade

- Projeto Final Integrado
  - Construção de solução end-to-end
  - Armazenamento em nuvem
  - Deploy manual

## 🚀 Como Rodar o Projeto

1. Criar o Ambiente Virtual

Primeiro, crie o ambiente virtual. No diretório do projeto, execute o seguinte comando:

- Windows:

```
python -m venv venv
```

- Linux/macOS:

```
python3 -m venv venv

```

2. Ativar o Ambiente Virtual

Após criar o ambiente virtual, ative-o com o comando apropriado para o seu sistema operacional:

- Windows:

```

.\venv\Scripts\activate

```

- Linux/macOS:

```

source venv/bin/activate

```

3. Instalar as Dependências

Antes de rodar o projeto, você precisa instalar as dependências. Para isso, execute o seguinte comando:
Usando pip:

```

pip install -r requirements.txt

```

Ou, se preferir usar pip3:

```

pip3 install -r requirements.txt

```

4. Executar o Projeto

```

streamlit run .\main.py

```

Após instalar as dependências, execute o seguinte comando para iniciar o projeto com o Streamlit:

## 🎯 Objetivos e Resultados Esperados

Após a conclusão do curso/projeto, os estudantes estarão aptos a:

- Criar, configurar e gerenciar aplicações modernas utilizando serviços PaaS e CaaS da Microsoft Azure.

- Realizar deploy de aplicações web e APIs utilizando Azure App Services e Container Apps.

- Monitorar e diagnosticar aplicações usando ferramentas integradas do Azure.

- Construir uma aplicação completa com backend em contêiner, armazenando dados na nuvem e com observabilidade configurada.

🔗 Links Úteis

- [Documentação do Azure App Services](https://learn.microsoft.com/azure/app-service/)

- [Streamlit](https://streamlit.io/)

- [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/)
