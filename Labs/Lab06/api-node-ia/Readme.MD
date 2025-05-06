# Via CEP API

Este projeto é uma API simples em Node.js que recupera informações de endereço com base em um CEP (Código Postal) fornecido, utilizando a API ViaCEP. Códigos gerado com Copilot com agente GPT-4o.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Endpoint da API](#endpoint-da-api)a
- [Licença](#licença)

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/yourusername/via-cep-api.git
   ```

2. Navegue até o diretório do projeto:
   ```
   cd via-cep-api
   ```

3. Instale as dependências:
   ```
   npm install
   ```

4. Crie um arquivo `.env` no diretório raiz e adicione as variáveis de ambiente necessárias (se aplicável).

## Uso

1. Inicie o servidor:
   ```
   npm start
   ```

2. A API estará rodando em `http://localhost:3000`.

## Endpoint da API

Para buscar informações de endereço com base no CEP, faça uma requisição GET para o seguinte endpoint:

```
GET /cep/:cep
```

Substitua `:cep` pelo CEP que deseja consultar.

### Exemplo de Requisição

```
GET /cep/01001-000
```

### Exemplo de Resposta

```json
{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "complemento": "lado ímpar",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "1004",
  "ddd": "11",
  "siafi": "7087"
}
```

## Licença

Este projeto está licenciado sob a Licença MIT.

