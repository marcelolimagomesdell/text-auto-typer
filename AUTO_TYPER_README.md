# Text Auto Typer

Um software local que permite criar botões que, ao serem clicados, digitam automaticamente o texto configurado. A janela permanece sempre no topo para fácil acesso.

## Funcionalidades

- **Criar botões personalizados**: Adicione botões com nomes e textos personalizados
- **Editar botões**: Modifique o nome ou texto de qualquer botão existente
- **Excluir botões**: Remova botões que não precisa mais
- **Sempre no topo**: A janela permanece sempre visível acima de outras janelas
- **Minimizar/Restaurar**: Minimize para um pequeno botão flutuante quando não estiver usando
- **Persistência**: Todos os botões são salvos automaticamente em um arquivo JSON

## Instalação

### Opção 1: Executar como Python (requer Python instalado)

#### Pré-requisitos
- Python 3.7 ou superior instalado

#### Passos
1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o aplicativo:
```bash
python text_auto_typer.py
```

### Opção 2: Compilar para .exe (não requer Python)

#### Pré-requisitos
- Python 3.7 ou superior instalado (apenas para compilar)

#### Passos
1. Execute o script de compilação:
```bash
build_exe.bat
```

2. O executável será criado na pasta `dist`: `TextAutoTyper.exe`

3. Mova o `TextAutoTyper.exe` para onde desejar e execute diretamente (duplo clique)

**Nota**: O arquivo .exe é autônomo e não requer Python instalado para funcionar.

## Como Usar

### Adicionar um Botão

1. Clique no botão **"+ Add New Button"**
2. Digite um nome para o botão (ex: "Email", "Endereço", "Assinatura")
3. Digite o texto que será digitado quando o botão for clicado
4. Clique em **OK**

### Usar um Botão

1. Clique no botão desejado na lista
2. A janela será minimizada temporariamente
3. O texto será digitado automaticamente onde o cursor estiver
4. A janela reaparecerá automaticamente

### Editar um Botão

1. Clique no botão **"Select"** ao lado do botão que deseja editar
2. Clique no botão **"✎ Edit Button"**
3. Modifique o nome ou texto conforme necessário
4. Clique em **OK**

### Excluir um Botão

1. Clique no botão **"Select"** ao lado do botão que deseja excluir
2. Clique no botão **"✕ Delete Button"**
3. Confirme a exclusão

### Minimizar a Janela

Clique no botão **"− Minimize"** para minimizar a janela para um pequeno botão flutuante no canto superior direito da tela. Clique em **"□ Restore"** para restaurar a janela completa.

## Arquivos

- `text_auto_typer.py` - Aplicação principal
- `text_buttons.json` - Arquivo de configuração (criado automaticamente)
- `requirements.txt` - Dependências do Python

## Dicas

- O aplicativo funciona melhor quando você já tem o cursor posicionado onde deseja digitar o texto
- O texto é digitado caractere por caractere, então pode levar alguns segundos para textos longos
- Você pode usar caracteres especiais e quebras de linha no texto
- A janela sempre permanecerá no topo de outras janelas para fácil acesso
