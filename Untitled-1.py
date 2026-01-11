# Trabalho de Lógica Computacional
# Aluno: Myllena Santos
# Turma: EAD
# Professor: Fernando Leonid
# Data: 04/01/2025
# Sistema de Controle de Estoque - Loja de Eletrônicos
# Objetivo: Gerenciar produtos com opções de adicionar, atualizar, excluir e visualizar estoque.

# Estrutura de dados: dicionário para armazenar produtos

# ESTRUTURA DE DADOS PRINCIPAL
# Usamos um dicionário onde:
# - Chave: nome do produto (string)
# - Valor: outro dicionário com preço e quantidade

# LOOP PRINCIPAL DO SISTEMA 

estoque = {}
# MENU PRINCIPAL
while True:
    print("\n" + "="*40)
    print("MENU PRINCIPAL - CONTROLE DE ESTOQUE")
    print("="*40)
    print("1. Adicionar produto")
    print("2. Atualizar produto")
    print("3. Excluir produto")
    print("4. Ver estoque")
    print("5. Sair do sistema")
    print("="*40)
    
    opcao = input("Digite o número da opção desejada: ")
    
    
    # OPÇÃO 1: ADICIONAR PRODUTO 
    if opcao == "1":
        print("\n--- ADICIONAR NOVO PRODUTO ---")
        
        # VALIDAÇÃO: Nome não pode ser vazio
        nome = input("Nome do produto: ").strip()
        if nome == "":
            print("ERRO: O nome do produto não pode ficar em branco!")
            continue  
            
        # VALIDAÇÃO: Verifica se produto já existe
        if nome in estoque:
            print(f"ERRO: O produto '{nome}' já está cadastrado no estoque!")
            continue  
        
        # VALIDAÇÃO DO PREÇO (com tratamento de erro)
        while True:
            try:
                preco = float(input("Preço do produto (R$): ").replace(',', '.'))
                if preco <= 0:  
                    print("ERRO: O preço deve ser maior que zero!")
                    continue
                break  
            except ValueError:  
                print("ERRO: Digite um valor numérico válido (ex: 10.50)")
        
        # VALIDAÇÃO DA QUANTIDADE (com tratamento de erro)
        while True:
            try:
                quantidade = int(input("Quantidade em estoque: "))
                if quantidade < 0:  
                    print("ERRO: A quantidade não pode ser negativa!")
                    continue
                break  
            except ValueError:  
                print("ERRO: Digite um número inteiro válido (ex: 5)")
        
        # ADICIONA O PRODUTO AO ESTOQUE
        estoque[nome] = {"preco": preco, "quantidade": quantidade}
        print(f" SUCESSO: Produto '{nome}' foi adicionado ao estoque!")
    
   
    # OPÇÃO 2: ATUALIZAR PRODUTO 
    elif opcao == "2":
        print("\n--- ATUALIZAR PRODUTO EXISTENTE ---")
        
        nome = input("Nome do produto que deseja atualizar: ").strip()
        
        # VALIDAÇÃO: 
        if nome not in estoque:
            print(f"ERRO: Produto '{nome}' não encontrado no estoque!")
            continue  
        
        print(f"\nProduto encontrado: {nome}")
        print(f"Preço atual: R${estoque[nome]['preco']:.2f}")
        print(f"Quantidade atual: {estoque[nome]['quantidade']} unidades")
        
        # VALIDAÇÃO DO NOVO PREÇO
        while True:
            try:
                novo_preco = float(input("Novo preço (R$): ").replace(',', '.'))
                if novo_preco <= 0:
                    print("ERRO: O preço deve ser maior que zero!")
                    continue
                break
            except ValueError:
                print("ERRO: Digite um valor numérico válido!")
        
        # VALIDAÇÃO DA NOVA QUANTIDADE
        while True:
            try:
                nova_quantidade = int(input("Nova quantidade: "))
                if nova_quantidade < 0:
                    print("ERRO: A quantidade não pode ser negativa!")
                    continue
                break
            except ValueError:
                print("ERRO: Digite um número inteiro válido!")
        
        # ATUALIZA OS DADOS DO PRODUTO
        estoque[nome]["preco"] = novo_preco
        estoque[nome]["quantidade"] = nova_quantidade
        print(f" SUCESSO: Produto '{nome}' foi atualizado!")
    

    # OPÇÃO 3: EXCLUIR PRODUTO 
    elif opcao == "3":
        print("\n--- EXCLUIR PRODUTO DO ESTOQUE ---")
        
        nome = input("Nome do produto que deseja excluir: ").strip()
        
        # VALIDAÇÃO: 
        if nome in estoque:
            # Confirmação para evitar exclusão acidental
            confirmacao = input(f"Tem certeza que deseja excluir '{nome}'? (S/N): ").upper()
            
            if confirmacao == "S":
                del estoque[nome]
                print(f" SUCESSO: Produto '{nome}' foi removido do estoque!")
            else:
                print("Operação cancelada pelo usuário.")
        else:
            print(f"ERRO: Produto '{nome}' não encontrado no estoque!")
    
    
    # OPÇÃO 4: VISUALIZAR ESTOQUE 
    elif opcao == "4":
        print("\n" + "="*50)
        print("VISUALIZAÇÃO COMPLETA DO ESTOQUE")
        print("="*50)
        
        # VERIFICA SE O ESTOQUE ESTÁ VAZIO
        if len(estoque) == 0:  
            print("📭 O estoque está vazio. Adicione produtos primeiro!")
        else:
            # CABEÇALHO DA TABELA
            print(f"{'PRODUTO':<20} | {'PREÇO (R$)':>12} | {'QUANTIDADE':>12}")
            print("-" * 50)
            
            # LOOP PARA PERCORRER TODOS OS PRODUTOS 
            for nome, dados in estoque.items():
                print(f"{nome:<20} | R${dados['preco']:>10.2f} | {dados['quantidade']:>12}")
            
            print("="*50)
            
            # CALCULAR ESTATÍSTICAS 
            total_produtos = len(estoque)
            total_itens = sum(dados['quantidade'] for dados in estoque.values())
            valor_total = sum(dados['preco'] * dados['quantidade'] for dados in estoque.values())
            
            print(f"\n RESUMO:")
            print(f"• Produtos diferentes: {total_produtos}")
            print(f"• Total de itens em estoque: {total_itens}")
            print(f"• Valor total do estoque: R${valor_total:.2f}")
    
    
    # OPÇÃO 5: SAIR DO SISTEMA
    elif opcao == "5":
        print("\n" + "="*40)
        print("OBRIGADO POR USAR O SISTEMA!")
        print("Saindo do controle de estoque...")
        print("="*40)
        break  
    
   
    # TRATAMENTO DE OPÇÃO INVÁLIDA
    else:
        print("\n OPÇÃO INVÁLIDA!")
        print("Por favor, digite apenas números de 1 a 5.")
        print("Exemplo: Para adicionar produto, digite '1'")

# FIM DO PROGRAMA
print("\nPrograma encerrado com sucesso!")




