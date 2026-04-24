# WDAC (Windows Defender Application Control) - Como Resolver Bloqueio

## O que é WDAC?
WDAC (Windows Defender Application Control) é uma política de segurança do Windows que bloqueia a execução de aplicativos não assinados ou não confiáveis.

## Soluções para Executar o TextAutoTyper.exe

### Opção 1: Adicionar Exceção no Windows Defender (Mais Simples)

1. Clique com o botão direito no arquivo `TextAutoTyper.exe`
2. Selecione "Propriedades"
3. Na parte inferior, marque "Desbloquear" se aparecer
4. Clique em "Aplicar" e "OK"

### Opção 2: Adicionar ao Windows Defender Security Center

1. Abra "Windows Security" (Segurança do Windows)
2. Vá para "Virus & threat protection" (Proteção contra vírus e ameaças)
3. Clique em "Manage settings" (Gerenciar configurações)
4. Role até "Exclusions" (Exclusões)
5. Clique em "Add or remove exclusions" (Adicionar ou remover exclusões)
6. Clique em "Add an exclusion" (Adicionar uma exclusão)
7. Selecione "File" (Arquivo)
8. Navegue até o arquivo `TextAutoTyper.exe` e selecione-o

### Opção 3: Executar como Administrador

1. Clique com o botão direito no arquivo `TextAutoTyper.exe`
2. Selecione "Executar como administrador"

### Opção 4: Desabilitar temporariamente o SmartScreen (Não Recomendado)

1. Abra o Windows Security
2. V para "App & browser control" (Controle de aplicativos e navegador)
3. Em "Reputation-based protection settings" (Configurações de proteção baseada em reputação)
4. Desative "Check apps and files" (Verificar aplicativos e arquivos)
5. Execute o TextAutoTyper.exe
6. Reative a proteção após usar

### Opção 5: Usar PowerShell para Desbloquear

1. Abra PowerShell como Administrador
2. Navegue até a pasta do arquivo:
   ```powershell
   cd "caminho\para\text-auto-typer"
   ```
3. Execute o comando:
   ```powershell
   Unblock-File -Path ".\TextAutoTyper.exe"
   ```

## Solução Permanente: Assinar o Código (Para Empresas)

Para ambientes corporativos com WDAC estrito, a solução permanente é assinar o aplicativo com um certificado digital:

1. Obter um certificado de assinatura de código (Code Signing Certificate)
2. Assinar o arquivo .exe usando o certificado
3. Adicionar o certificado à lista de confiança da organização

## Informações sobre a Criptografia

O aplicativo agora usa criptografia para proteger os dados armazenados:

- **Arquivo de dados**: `text_buttons.enc` (encriptado)
- **Chave de criptografia**: Gerada automaticamente baseada no nome do computador e usuário
- **Arquivo da chave**: `encryption.key` (mantido na mesma pasta)
- **Algoritmo**: Fernet (AES-128 em CBC mode com HMAC)

**Nota**: Se você mover o aplicativo para outro computador, os dados encriptados não poderão ser lidos pois a chave é específica da máquina.
