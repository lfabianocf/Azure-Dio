<!--START_SECTION:header-->
<div align="center">
  <p align="center">
    <img 
      alt="DIO Education" 
      src="https://raw.githubusercontent.com/lfabianocf/Azure-Dio/refs/heads/main/assets/AzureCloudNative.webp" 
      width="100px" 
    />
    <h1>Azure Cloud Native - Microsoft - Dio</h1>
  </p>
</div>
<!--END_SECTION:header-->

<br/>

Este repositório contém projetos e exemplos desenvolvidos durante o bootcamp da DIO, no módulo de Inteligência Artificial e Desenvolvimento com GitHub Copilot, voltado para a plataforma Microsoft Azure Cloud Native.

## Sobre o Projeto

O objetivo deste repositório é demonstrar o uso de práticas modernas no desenvolvimento de aplicações, integrando:

- **Desenvolvimento Cloud Native** com Azure
- **Integração de Inteligência Artificial** no ciclo de desenvolvimento
- **GitHub Copilot** para acelerar a escrita e a qualidade do código

## Como Usar

### Pré-requisitos

- Conta no [GitHub](https://github.com)
- Conta no [Azure](https://azure.microsoft.com)
- [Node.js](https://nodejs.org) instalado
- VS Code com a extensão [GitHub Copilot](https://github.com/features/copilot) habilitada

## Extensões e Integrações

### GitHub Copilot

- **GitHub Copilot**: Auxilia na geração de código e sugestões inteligentes. Certifique-se de que a extensão está instalada e configurada no VS Code para aproveitar seu potencial.

### Exemplos de Prompts para Geração de Código com GitHub Copilot

#### GPT-4.0

```javascript
// Crie uma função em JavaScript que receba um array de números e retorne a soma dos números pares.
function somaPares(numeros) {
  return numeros
    .filter((num) => num % 2 === 0)
    .reduce((acc, num) => acc + num, 0);
}
```

#### Gemini

```python
# Escreva uma função em Python que calcule o fatorial de um número usando recursão.
def fatorial(n):
   if n == 0 or n == 1:
      return 1
   return n * fatorial(n - 1)
```

#### Cloud 3.5 Sonnet

```csharp
// Implemente um método em C# que verifique se uma string é um palíndromo.
public bool IsPalindrome(string input) {
   string reversed = new string(input.Reverse().ToArray());
   return input.Equals(reversed, StringComparison.OrdinalIgnoreCase);
}
```

#### O3

```java
// Escreva um programa em Java que leia uma lista de nomes e os ordene em ordem alfabética.
import java.util.*;

public class OrdenarNomes {
   public static void main(String[] args) {
      List<String> nomes = Arrays.asList("Ana", "Carlos", "Bruno", "Diana");
      Collections.sort(nomes);
      System.out.println(nomes);
   }
}
```

### Extensões do Azure para VS Code

- **Azure Tools**: Conjunto de ferramentas para facilitar o gerenciamento e o deploy de recursos no Azure.  
  [Azure Tools - Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack)

- **Azure Functions**: Para desenvolvimento e deploy de funções serverless.  
  [Azure Functions - Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)

- **Azure Storage**: Para gerenciamento de serviços de armazenamento do Azure.  
  [Azure Storage - Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureresourcegroups)

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

