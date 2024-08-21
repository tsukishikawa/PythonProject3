# Aplicação de Gerenciamento de Clientes

Este projeto é uma aplicação de gerenciamento de clientes usando `Tkinter` para a interface gráfica e `sqlite3` para o banco de dados. A aplicação permite visualizar, buscar, inserir, atualizar e excluir informações de clientes armazenadas em um banco de dados SQLite.

## Requisitos

- Python
- `pyinstaller` (para criar executáveis)

## Instalação
cd PythonProject3
pip install pyinstaller
### Clonando o Repositório

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/tsukishikawa/PythonProject3.git

### Uso
Executando a Aplicação
- Para executar a aplicação localmente, use:

python aplicacao.py

## Criando um Executável
Para criar um executável da aplicação, use pyinstaller. Execute o seguinte comando no terminal:

pyinstaller --onefile --windowed --noconsole aplicacao.py

O executável será gerado no diretório 'dist'.

## Estrutura do Projeto
'aplicacao.py': O script principal da aplicação que configura e executa a interface gráfica.
'backend.py': O módulo responsável pela interação com o banco de dados SQLite.
'gui.py': O módulo que define a interface gráfica da aplicação.

##Contribuição
Contribuições são bem-vindas! Para contribuir, siga estas etapas:

Faça um fork do repositório.
Crie uma nova branch (git checkout -b minha-nova-feature).
Faça suas alterações e commit (git commit -am 'Adiciona nova feature').
Faça um push para a branch (git push origin minha-nova-feature).
Abra um Pull Request.
