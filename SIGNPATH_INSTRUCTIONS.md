# Como Usar SignPath para Assinatura Gratuita de Código

## O que é SignPath?
SignPath é um serviço que oferece assinatura de código gratuita para projetos open source. Eles usam seus próprios certificados para assinar seu aplicativo.

## Requisitos

1. **Projeto deve ser Open Source**: Seu código deve estar disponível publicamente com licença open source (MIT, Apache, GPL, etc.)
2. **Registro no GitHub/GitLab/Bitbucket**: O projeto deve estar hospedado em um repositório público
3. **Verificação**: O SignPath precisa verificar que você é o proprietário do projeto

## Passo a Passo

### 1. Tornar o Projeto Open Source

1. Crie um repositório público no GitHub
2. Faça upload do código do TextAutoTyper
3. Adicione uma licença open source (recomendo MIT por ser simples e permissiva)
4. Crie um arquivo `LICENSE` com o texto da licença MIT

### 2. Criar Conta no SignPath

1. Acesse: https://signpath.io/
2. Clique em "Sign Up"
3. Registre-se usando sua conta do GitHub (recomendado)
4. Confirme seu email

### 3. Criar Organização

1. Após login, crie uma organização
2. Escolha "Free for Open Source" como plano
3. Preencha os dados da organização

### 4. Adicionar Projeto

1. Na organização, clique em "Add Project"
2. Conecte seu repositório do GitHub
3. Selecione o repositório do TextAutoTyper
4. Configure as informações do projeto

### 5. Configurar CI/CD (Opcional mas Recomendado)

O SignPath funciona melhor com integração contínua. Você pode usar:
- GitHub Actions (gratuito para repositórios públicos)
- GitLab CI
- Outras ferramentas de CI/CD

### 6. Submeter para Assinatura

1. Crie um "release" no seu repositório GitHub com o arquivo .exe
2. No SignPath, crie uma "Signing Request"
3. Selecione o artefato (o .exe) para assinar
4. Submeta para assinatura

### 7. Download do Arquivo Assinado

1. Após a assinatura ser aprovada (geralmente automática para open source)
2. Baixe o arquivo .exe assinado
3. Substitua o arquivo original pelo assinado

## Limitações

- **Apenas para open source**: Seu código deve ser público
- **Processo burocrático**: Requer verificação e configuração
- **Tempo**: Pode levar dias para a primeira aprovação
- **Limites**: Pode haver limites no número de assinaturas gratuitas

## Alternativa Mais Rápida: Self-Signed Certificate

Se você não quer tornar o projeto open source, pode criar um certificado autoassinado:

```powershell
# Criar certificado autoassinado
New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=TextAutoTyper" -CertStoreLocation "Cert:\CurrentUser\My"

# Assinar o .exe
$cert = Get-ChildItem -Path Cert:\CurrentUser\My -CodeSigningCert
Set-AuthenticodeSignature -FilePath "TextAutoTyper.exe" -Certificate $cert
```

**Problema**: Você precisará adicionar o certificado à lista de confiança em cada máquina onde o aplicativo será executado.

## Recomendação

Para uso pessoal ou pequeno grupo:
- Use as soluções de desbloqueio do `WDAC_INSTRUCTIONS.md`
- É mais rápido e não requer burocracia

Para uso corporativo com muitos usuários:
- Considere comprar um certificado de assinatura de código
- Custo: ~$100-500/ano
- Resolvido de forma profissional

## Licença MIT (Exemplo)

Se decidir usar SignPath, adicione este conteúdo ao arquivo `LICENSE`:

```
MIT License

Copyright (c) 2024 TextAutoTyper

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
