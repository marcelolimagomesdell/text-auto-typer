# Como Hospedar o TextAutoTyper no GitHub

## Passo 1: Criar Conta no GitHub

1. Acesse: https://github.com/
2. Clique em "Sign up"
3. Preencha os dados e crie sua conta (gratuita)

## Passo 2: Criar Novo Repositório

1. Após fazer login, clique no botão **"+"** no canto superior direito
2. Selecione **"New repository"**
3. Preencha:
   - **Repository name**: `text-auto-typer`
   - **Description**: `Windows application for automated text typing with system tray and encryption`
   - **Public**: ✅ (marque para tornar público - necessário para SignPath)
   - **Add a README file**: ❌ (não marque, já temos um)
   - **Add .gitignore**: ❌ (não marque, já temos um)
   - **Choose a license**: Selecione "MIT License"
4. Clique em **"Create repository"**

## Passo 3: Fazer Upload dos Arquivos

### Opção A: Upload via Interface Web (Mais Simples)

1. No repositório criado, clique em **"uploading an existing file"**
2. Arraste os seguintes arquivos para a área de upload:
   - `text_auto_typer.py`
   - `requirements.txt`
   - `build_exe.bat`
   - `README.md` (sobrescreva o padrão)
   - `LICENSE` (sobrescreva o padrão)
   - `.gitignore` (sobrescreva o padrão)
   - `AUTO_TYPER_README.md`
   - `WDAC_INSTRUCTIONS.md`
   - `SIGNPATH_INSTRUCTIONS.md`
   - `GITHUB_UPLOAD_INSTRUCTIONS.md` (opcional)
3. Role até o final e clique em **"Commit changes"**
4. Digite uma mensagem de commit: "Initial commit"
5. Clique em **"Commit changes"**

### Opção B: Usar Git (Recomendado para Desenvolvimento)

```bash
# Navegue até a pasta do projeto
cd c:\Users\Marcelo_LimaGomes\CascadeProjects\network-diagnostics-tool\text-auto-typer

# Inicialize o repositório git
git init

# Adicione todos os arquivos
git add .

# Faça o primeiro commit
git commit -m "Initial commit"

# Adicione o remote (substitua SEU_USUARIO pelo seu nome de usuário)
git remote add origin https://github.com/SEU_USUARIO/text-auto-typer.git

# Faça push para o GitHub
git branch -M main
git push -u origin main
```

## Passo 4: Adicionar o Executável (Opcional)

Você pode adicionar o arquivo .exe ao GitHub para download direto:

1. Crie uma pasta chamada `releases` no repositório
2. Faça upload do `TextAutoTyper.exe` para essa pasta
3. Ou use o GitHub Releases (veja Passo 5)

## Passo 5: Criar Release no GitHub

Para distribuir o executável oficialmente:

1. No repositório, clique em **"Releases"** no menu lateral
2. Clique em **"Create a new release"**
3. Preencha:
   - **Tag version**: `v1.0.0`
   - **Release title**: `TextAutoTyper v1.0.0`
   - **Description**: Descreva as funcionalidades desta versão
4. Em **"Binary files"**, arraste o arquivo `TextAutoTyper.exe`
5. Clique em **"Publish release"**

## Passo 6: Configurar SignPath (Para Assinatura de Código)

Após hospedar no GitHub, siga as instruções em `SIGNPATH_INSTRUCTIONS.md` para assinar o código gratuitamente.

## Arquivos que NÃO Devem Ser Uploadados

De acordo com o `.gitignore`, estes arquivos não devem ser uploadados:
- `text_buttons.enc` (dados encriptados - contém suas senhas)
- `encryption.key` (chave de criptografia)
- `build/` e `dist/` (arquivos de compilação)
- `__pycache__/` (cache Python)
- Arquivos temporários

## Verificação

Após fazer o upload:

1. Acesse: `https://github.com/SEU_USUARIO/text-auto-typer`
2. Verifique se todos os arquivos estão visíveis
3. Verifique se o README.md aparece corretamente
4. Verifique se a licença MIT aparece

## Próximos Passos

Após hospedar com sucesso:

1. **Configurar SignPath**: Siga `SIGNPATH_INSTRUCTIONS.md`
2. **Testar Download**: Baixe o código do GitHub para verificar
3. **Documentar**: Adicione capturas de tela ao README
4. **Divulgar**: Compartilhe o link do repositório

## Solução de Problemas

### Erro: "Repository already exists"

Se o repositório já existir:
- Use um nome diferente
- Ou delete o repositório existente e recrie

### Erro: "File too large"

O GitHub tem limite de 100MB por arquivo:
- O `TextAutoTyper.exe` pode ser grande (~20MB), deve funcionar
- Se falhar, use GitHub Releases em vez de upload direto

### Erro: "Permission denied"

Verifique se você está logado corretamente no GitHub.

## Suporte

Se tiver problemas:
- GitHub Docs: https://docs.github.com/
- GitHub Support: https://support.github.com/
