import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pymssql
import uuid
import json
from dotenv import load_dotenv

load_dotenv()

# Load environment variables from .env file
CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")
ACCOUNT_NAME = os.getenv("BLOB_ACCOUNT_NAME")

# Load SQL Server connection details from environment variables
SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

# Título da aplicação
st.title("Azure Blob Storage and SQL Server Integration")
st.title("Cadastro de Produtos")

# Cadastro de Prduto formulário
product_name = st.text_input("Nome do Produto")
product_description = st.text_area("Descrição do Produto")
product_price = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
product_image = st.file_uploader("Imagem do Produto", type=["jpg", "jpeg", "png"])

# Função para enviar imagem para o Blob Storage
def upload_image_to_blob(file):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        blob_name = str(uuid.uuid4()) + "_" + file.name
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(file.read(), overwrite=True)
        image_url = f"https://{ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER_NAME}/{blob_name}"
        
        return image_url

    except Exception as e:
        st.error(f"Erro ao enviar imagem: {e}")
        return None

# Função de inserir os dados no Azure Sql Server usando pymssql
def insert_product(product_data):  
    try:
        #image_url = upload_image_to_blob(product_image)
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USERNAME, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor()

        # Insere os dados do produto
        query_insert = """
        INSERT INTO dbo.Produtos (nome, descricao, preco, imagem_url)
        VALUES (%s, %s, %s, %s)
        """
        
        cursor.execute(query_insert, (product_data["nome"], product_data["descricao"], product_data["preco"], product_data["imagem_url"]))
        conn.commit()
        conn.close()

        return True
    
    except Exception as e:
        st.error(f"Erro ao cadastrar produto: {e}")
        return False

# Função para listar os produtos cadastrados no Azure SQL Server
def list_products_sql():
    try:
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USERNAME, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor(as_dict=True)
        query = "SELECT id, nome, descricao, preco, imagem_url FROM Produtos"
        cursor.execute(query)
        products = cursor.fetchall()
        conn.close()
        return products
    except Exception as e:
        st.error(f"Erro ao listar produtos: {e}")
        return []

# Função para exibir os produtos cadastrados    
def list_products_screen():
    products = list_products_sql()
    if products:
        # Número de colunas para exibir os produtos
        cards_por_linha = 3
        # Cria as colunas para exibir os produtos
        cols = st.columns(cards_por_linha)
        for i, product in enumerate(products):
            col = cols[i % cards_por_linha]
            with col:
                st.markdown(f"Id: {product['id']}")
                st.markdown(f"Nome Produto: {product['nome']}")
                st.write(f"**Descrição:** {product['descricao']}")
                st.write(f"**Preço:** R$ {product['preco']:.2f}")
                if product["imagem_url"]:
                    html_img = f'<img src="{product["imagem_url"]}" alt="Imagem do Produto" width="200" height="200">'
                    st.markdown(html_img, unsafe_allow_html=True)   
                st.markdown("---")
            # Cada cards por linha de produtos , exibe o nome, descrição e preço do produto
            if (i + 1) % cards_por_linha == 0 and (i + 1 ) < len(products):
                cols = st.columns(cards_por_linha)
    else:
        st.info("Nenhum produto cadastrado.")

# Botão para cadastrar o produto
if st.button("Cadastrar Produto"):
    if not product_name or not product_description or not product_price or not product_image:
        st.warning("Por favor, preencha todos os campos!")
    else:
        # Envia a imagem para o Blob Storage e obtém a URL se houver
        image_prod = ""
        if  product_image is not None:
            # Envia a imagem para o Blob Storage e obtém a URL
            image_prod = upload_image_to_blob(product_image)

        # Insere o produto no SQL Server

        product_data = {
            "nome": product_name,
            "descricao": product_description,
            "preco": product_price,
            "imagem_url": image_prod
        }
        # Chama a função para inserir o produto no SQL Server
        if insert_product(product_data):
            st.success("Produto cadastrado com sucesso!")
            list_products_screen()
        else:
            st.error("Erro ao cadastrar o produto.")

        # Opcional: Salva os dados do produto em um arquivo JSON
        file_path = "produtos.json"
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                try:
                    produtos = json.load(file)
                except json.JSONDecodeError:
                    produtos = []   
        else:
            produtos = []

        produtos.append(product_data)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(produtos, file, ensure_ascii=False, indent=4) 

        st.json(product_data)


    return_mensage= "Produto salvo com sucesso!"

st.header("Produtos Cadastrados")

if st.button("Listar Produtos"):
    list_products_screen()
    return_mensage= "Produtos listados com sucesso!"
