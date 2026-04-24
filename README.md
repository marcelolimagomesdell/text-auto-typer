# Text Auto Typer

Um aplicativo Windows que permite criar botões personalizados que digitam texto automaticamente quando clicados. Ideal para armazenar senhas, respostas frequentes, assinaturas e qualquer texto que você usa frequentemente.

## Funcionalidades

- **Botões Personalizáveis**: Crie botões com nomes e textos personalizados
- **Digitação Automática**: Ao clicar em um botão, o texto é digitado automaticamente onde o cursor estiver
- **Sistema Tray**: Ícone na barra de sistema para acesso rápido
- **Gerenciamento via Tray**: Adicione e remova botões diretamente do menu do sistema tray
- **Sempre no Topo**: Janela permanece visível acima de outras aplicações
- **Movimento Livre**: Arraste a janela para qualquer lugar da tela
- **Criptografia**: Dados armazenados com criptografia AES-128 para segurança
- **Minimizar para Tray**: Minimize para o system tray quando não estiver usando

## Capturas de Tela

*(Adicione capturas de tela aqui após hospedar no GitHub)*

## Requisitos

- Windows 10 ou superior
- Nenhuma dependência adicional necessária (arquivo .exe autônomo)

## Instalação

1. Baixe o arquivo `TextAutoTyper.exe` da seção [Releases](https://github.com/seu-usuario/text-auto-typer/releases)
2. Coloque o arquivo em qualquer pasta do seu computador
3. Execute o arquivo (duplo clique)

**Nota**: Se o Windows Defender bloquear o arquivo, consulte [WDAC_INSTRUCTIONS.md](WDAC_INSTRUCTIONS.md) para soluções.

## Como Usar

### Adicionar um Botão

1. Clique no botão **"+ Add New Button"** na janela principal
2. Digite um nome para o botão (ex: "Email", "Senha", "Assinatura")
3. Digite o texto que será digitado quando o botão for clicado
4. Clique em **Save** para salvar sem fechar ou **OK** para salvar e fechar

### Usar um Botão

1. Clique no botão desejado na lista
2. A janela será minimizada temporariamente
3. O texto será digitado automaticamente onde o cursor estiver
4. A janela reaparecerá automaticamente

### Editar um Botão

1. Clique no botão **"Select"** ao lado do botão que deseja editar
2. Clique no botão **"✎ Edit Button"**
3. Modifique o nome ou texto conforme necessário
4. Clique em **Save** ou **OK**

### Excluir um Botão

**Via Janela Principal:**
1. Clique no botão **"Select"** ao lado do botão que deseja excluir
2. Clique no botão **"✕ Delete Button"**
3. Confirme a exclusão

**Via System Tray:**
1. Clique com o botão direito no ícone do system tray
2. Selecione **"Remove Button"**
3. Selecione o botão que deseja remover
4. Confirme a exclusão

### System Tray

O aplicativo cria um ícone no system tray com as seguintes opções:
- **Show Window**: Mostra a janela principal
- **Add Button**: Abre diálogo para adicionar novo botão
- **Remove Button**: Abre diálogo para remover botão existente
- **Exit**: Fecha completamente o aplicativo

## Segurança

- **Criptografia**: Todos os dados são armazenados encriptados usando AES-128 (Fernet)
- **Chave Específica da Máquina**: A chave de criptografia é gerada baseada no nome do computador e usuário
- **Arquivos de Dados**: 
  - `text_buttons.enc` - Dados encriptados
  - `encryption.key` - Chave de criptografia

**Nota**: Se você mover o aplicativo para outro computador, os dados encriptados não poderão ser lidos pois a chave é específica da máquina.

## Desenvolvimento

### Requisitos de Desenvolvimento

- Python 3.7 ou superior
- pip

### Configuração do Ambiente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/text-auto-typer.git
cd text-auto-typer

# Instale as dependências
pip install -r requirements.txt

# Execute o aplicativo
python text_auto_typer.py
```

### Compilar para .exe

```bash
# Execute o script de compilação (Windows)
build_exe.bat

# Ou manualmente:
pip install pyinstaller
pyinstaller --onefile --windowed --name "TextAutoTyper" text_auto_typer.py
```

O executável será criado na pasta `dist/`.

## Estrutura do Projeto

```
text-auto-typer/
├── text_auto_typer.py       # Código fonte principal
├── requirements.txt          # Dependências Python
├── build_exe.bat            # Script para compilar .exe
├── TextAutoTyper.exe         # Executável compilado
├── README.md                 # Este arquivo
├── LICENSE                   # Licença MIT
├── WDAC_INSTRUCTIONS.md      # Instruções para WDAC
├── SIGNPATH_INSTRUCTIONS.md  # Instruções para SignPath
└── AUTO_TYPER_README.md      # Instruções detalhadas de uso
```

## Solução de Problemas

### Windows Defender Bloqueia o Arquivo

Consulte [WDAC_INSTRUCTIONS.md](WDAC_INSTRUCTIONS.md) para várias soluções:
- Desbloquear via Propriedades
- Adicionar exclusão no Windows Defender
- Executar como Administrador
- Desbloquear via PowerShell

### Botão Save Não Aparece

Se o botão "Save" não aparecer no diálogo:
- Redimensione a janela do diálogo
- A versão mais recente já corrigiu este problema

### Dados Não Carregam Após Mover para Outro Computador

Isso é normal devido à criptografia específica da máquina:
- A chave de criptografia é baseada no nome do computador
- Você precisará recriar os botões no novo computador
- Esta é uma medida de segurança

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Fazer fork do projeto
- Criar pull requests

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Agradecimentos

- [pyautogui](https://pyautogui.readthedocs.io/) - Automação de teclado/mouse
- [pystray](https://github.com/moses-palmer/pystray) - System tray icon
- [PyInstaller](https://pyinstaller.org/) - Criação de executáveis
- [cryptography](https://cryptography.io/) - Criptografia de dados

## Contato

Para questões, sugestões ou feedback, abra uma [issue](https://github.com/seu-usuario/text-auto-typer/issues) no GitHub.

## Changelog

### Versão 1.0.0
- Lançamento inicial
- Botões personalizáveis
- Digitação automática
- System tray com menu
- Criptografia de dados
- Sempre no topo
- Movimento livre da janela
