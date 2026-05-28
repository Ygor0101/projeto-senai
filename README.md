Empresa: Mais Química
Desenvolvedor: Ygor Davi Portela Oliveira

### Sistema de cadastro e consulta de Produtos.

# Visão Geral do Projeto

O objetivo deste projeto é desenvolver um sistema em linha de comando (CLI) para gerenciar o cadastro leitura, atualização e exclusão (CRUD) de produto. O sistema deve permitir que o usuário mantenha um controle atualizado do seu catálogo de forma interativa e intuitiva.

# Estrutura de dados (o que vamos guardar)

Cada produto gerenciado pelo sistema deve conter obrigatoriamente as seguintes informações.

- Nome: Texto que identifica o item.
- Valor: Um numero (inteiro ou decimal) que representa o preço unitario do produto.
- Peso: Um número (inteiro ou decimal) que representa o peso/peso liquido do produto.

# Requisitos Funcionais (O que o sistema FAZ)

São as ações que o usuario pode executar dentro do programa. 

- RF01 - Cadastrar: O sistema deve permitir a inserção de um novo produto informando seu nome e valor númerico.

- RF02 - Listar: O sistema deve exibir todos os produto cadastrados, mostrar seu ID (posição na lista), nome e valor.

- RF03 - Editar: O sistema deve permitir a alteração/edição de algum produto especifico.

- RF04 - Excluir: O sistema deve permitir a exclusão definitiva a partir do seu ID.

- RF05 - Menu interativo: o sistema deve exibir um menu de opções e rodar continuamente até que o úsuario escolha a opção "Sair".

# Requisitos não funcionais (Como o sistema É)

- RNF01 - Interface: A interação com o usuario será inteiramente via terminal (linha de comando).

- RNF02 - Armazenamento: Os dados serão salvos temporariamente na memoria RAM usando Listas e Dicionarios do Python (não haverá banco de dados nesta versão).

# Regras de negocio (Restrições)

Condições que o código PRECISA respeitar para não quebrar ou gerar dados inválidos.

- RN01: A tentar editar ou excluir um produto, o sistema deve verificar se o ID digitado realmente existe na lista. Se não existir, deve exibir uma mensagem de erro ("Item não encontrado").

- RN02: Todo novo produto cadastrado deve entrar no sistema com o status padrão como "Verdadeira". (Ex: Ativo).