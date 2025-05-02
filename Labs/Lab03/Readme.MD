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




📦 Blog Fabiano App – Containerização e Deploy no Azure

Este repositório descreve o processo de criação, build, push e deploy de uma aplicação Docker no Azure usando o Azure Container Apps e o Azure Container Registry (ACR).

🧱 1. Build da Imagem Docker

Primeiro, construa a imagem localmente usando o Docker:
```
docker build -t NAMEIMAGE .
```

🚀 2. Testando a Imagem Localmente

Execute a imagem localmente no modo detached (em segundo plano):
```
docker run -d -p 80:80 NAMEIMAGE
```
A aplicação estará acessível em http://localhost.

🔐 3. Login no Azure

Autentique-se no Azure com sua conta e locatário específico (tenant):
```
az login 
# or 
az login --tenant "AQUI COLOCAR TENANT"
```
📁 4. Criando Recursos no Azure
Criar um grupo de recursos:

```
az group create --name NAME --location eastus
```
Criar um Azure Container Registry (ACR):
```
az acr create --resource-group NAME --name NAMEAPP --sku Basic
```
Fazer login no ACR:
```
az acr login --name NAMEACR
```

📤 5. Publicar a Imagem no ACR
Marcar (tag) a imagem:
```
docker tag TAGNAME NAMEIMAGE
```
Fazer o push para o ACR:
```
docker push NAMEIMAGE
```
🌐 6. Criar Ambiente para o Container App
```
az containerapp env create \
  --name NAME \
  --resource-group NAME-RESOUCE-GROUP \
  --location eastus
```

📦 7. Criar o Container App
```
az containerapp create \
  --name NAME \
  --resource-group NAME-RESOUCE-GROUP \
  --image NAMEIMAGE \
  --environment NAME-ENV \
  --target-port 80 \
  --ingress external \
  --registry-username USENAME \
  --registry-password PASSWORD-REGISTER \
  --registry-server NAME-SERVER
```
Importante: Os dados de autenticação do ACR (usuário/senha) devem ser tratados como informações sensíveis e idealmente armazenados em variáveis de ambiente ou serviços de segredo como o Azure Key Vault.

✅ Resultado

A aplicação estará publicada como um Azure Container App, acessível publicamente via endpoint gerado pelo Azure.


⚙️ Automação com Script Bash

Você pode usar o seguinte script (deploy.sh) para automatizar o processo de build, push e deploy do container:
```
#!/bin/bash

# Variáveis
RESOURCE_GROUP=""
ACR_NAME=""
APP_NAME=""
ENV_NAME=""
IMAGE_NAME=""
IMAGE_TAG="$ACR_NAME.azurecr.io/$IMAGE_NAME"
LOCATION="eastus"
REGISTRY_USERNAME=""
REGISTRY_PASSWORD=""

# Login no Azure
az login

# Criar grupo de recursos
az group create --name $RESOURCE_GROUP --location $LOCATION

# Criar ACR
az acr create --resource-group $RESOURCE_GROUP --name $ACR_NAME --sku Basic

# Login no ACR
az acr login --name $ACR_NAME

# Build da imagem
docker build -t $IMAGE_NAME .

# Tag e push para ACR
docker tag $IMAGE_NAME $IMAGE_TAG
docker push $IMAGE_TAG

# Criar ambiente do Container App
az containerapp env create --name $ENV_NAME --resource-group $RESOURCE_GROUP --location $LOCATION

# Criar Container App
az containerapp create \
  --name $APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --image $IMAGE_TAG \
  --environment $ENV_NAME \
  --target-port 80 \
  --ingress external \
  --registry-server "$ACR_NAME.azurecr.io" \
  --registry-username $REGISTRY_USERNAME \
  --registry-password $REGISTRY_PASSWORD

```

🔄 Deploy Contínuo com GitHub Actions

Aqui está um exemplo de workflow do GitHub Actions (.github/workflows/deploy.yml) para buildar e fazer o deploy automaticamente ao fazer push para a main.
```
name: Deploy para Azure Container Apps

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    env:
      ACR_NAME: blogfabianoacr
      IMAGE_NAME: blog-fabiano-app
      IMAGE_TAG: latest
      RESOURCE_GROUP: containerappslab03
      CONTAINER_APP_NAME: blog-fabianoe-app
      ENV_NAME: blog-fabianoe-env
      LOCATION: eastus

    steps:
    - name: Checkout código
      uses: actions/checkout@v3

    - name: Login no Azure
      uses: azure/login@v1
      with:
        creds: ${{ secrets.AZURE_CREDENTIALS }}

    - name: Login no ACR
      run: az acr login --name $ACR_NAME

    - name: Build e Push da imagem Docker
      run: |
        docker build -t $IMAGE_NAME:$IMAGE_TAG .
        docker tag $IMAGE_NAME:$IMAGE_TAG $ACR_NAME.azurecr.io/$IMAGE_NAME:$IMAGE_TAG
        docker push $ACR_NAME.azurecr.io/$IMAGE_NAME:$IMAGE_TAG

    - name: Deploy no Azure Container App
      run: |
        az containerapp create \
          --name $CONTAINER_APP_NAME \
          --resource-group $RESOURCE_GROUP \
          --image $ACR_NAME.azurecr.io/$IMAGE_NAME:$IMAGE_TAG \
          --environment $ENV_NAME \
          --target-port 80 \
          --ingress external \
          --registry-server $ACR_NAME.azurecr.io \
          --registry-username $ACR_NAME \
          --registry-password ${{ secrets.REGISTRY_PASSWORD }}

```

🔐 Secrets Necessários

Configure os seguintes secrets no seu repositório do GitHub:

    AZURE_CREDENTIALS — credenciais do serviço Azure (JSON gerado via az ad sp create-for-rbac)

    REGISTRY_PASSWORD — senha do seu Azure Container Registry   


🔐 Gerando o Secret AZURE_CREDENTIALS (Azure Service Principal)
1. Gere as credenciais com o Azure CLI:

Execute o seguinte comando no seu terminal:
```
az ad sp create-for-rbac --name "github-deploy-sp" --role contributor \
  --scopes /subscriptions/<SEU_ID_DE_ASSINATURA> --sdk-auth
```

Substitua <SEU_ID_DE_ASSINATURA> pelo ID da sua assinatura Azure. Para descobri-lo, use:
```
az account show --query id --output tsv

```

2. Exemplo de Saída (JSON):
```
{
  "clientId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "clientSecret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "subscriptionId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "tenantId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
  "resourceManagerEndpointUrl": "https://management.azure.com/",
  "activeDirectoryGraphResourceId": "https://graph.windows.net/",
  "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
  "galleryEndpointUrl": "https://gallery.azure.com/",
  "managementEndpointUrl": "https://management.core.windows.net/"
}

```
3. Adicione ao GitHub:

    Vá até o repositório no GitHub

    Clique em Settings > Secrets and variables > Actions

    Adicione um novo Secret com o nome: AZURE_CREDENTIALS

    Cole o conteúdo JSON como valor
Com isso, o GitHub Actions poderá se autenticar na sua conta Azure de forma segura para fazer o deploy automático.
