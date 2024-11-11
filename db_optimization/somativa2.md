# Marketplace Online - Especificação do Sistema

## Contexto

Desenvolvimento de um sistema de marketplace online para gerenciar usuários, produtos, transações e avaliações.

## Requisitos Base

### 1. Usuários

- [x] Nome
- E-mail
- Senha
- Endereço

### 2. Produtos

- Nome
- Descrição
- Preço
- Quantidade disponível
- Categoria

### 3. Transações

- Registro de compras entre usuários e produtos

### 4. Avaliações

- Sistema de avaliação de produtos comprados

### 5. Categorias

- Organização em categorias e subcategorias

## Tarefas Iniciais

### 1. Modelagem de Dados

- Desenvolver esquema MongoDB (UML ou DER)
- Considerar documentos incorporados e referências

### 2. Inserção e Validação

- Criar collections com schema validation
- Inserir dados de exemplo (mínimo 5 por collection)

### 3. Consultas

- Buscar produtos por categoria
- Buscar avaliações por produto
- Criar novas transações
- Atualizar estoque após compras

### 4. Índices

- Implementar índices para otimização

### 5. Agregações

- Calcular média de avaliações por produto
- Calcular vendas totais por categoria

## Requisitos Adicionais

### 6. Promoções

- Sistema de descontos temporários

### 7. Pontos de Fidelidade

- Sistema de pontos por compra
- Descontos baseados em pontos

### 8. Resposta a Avaliações

- Interface para vendedores responderem avaliações

### 9. Geolocalização

- Localização geográfica de usuários
- Localização geográfica de vendedores/produtos
- Índices geoespaciais
- Busca por proximidade com filtro de raio
- Análise de distância média entre compradores e vendedores
- Análise de popularidade de categorias por região

### 10. Relatórios

- Sistema de relatórios de vendas para vendedores
