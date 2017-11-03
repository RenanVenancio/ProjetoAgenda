class Agenda:
  def __init__(self):
    self.nome = []
    self.endereco = []
    self.telcomercial = []
    self.telresidencial = []
    self.celular = []
    self.email = []
    
    
  def add_nome(self, n):
    self.nome.append(n)
    
  def add_end(self, n):
    self.endereco.append(n)

  def add_tr(self, n):
    self.telresidencial.append(n)

  def add_tc(self, n):
    self.telcomercial.append(n)
    
  def add_cel(self, n):
    self.celular.append(n)

  def add_em(self, n):
    self.email.append(n)
    
  def remover(self,r):
    self.nome.remove(r) 
    
  def buscar(self,busca):
    ind=0      #VARIAVEL DE INDICE
    encontrados = 0
    for i in self.nome:
    
      if busca == self.nome[ind]:
        print('Encontrado: INDICE: %i | %s | %s | %s |'%(ind ,self.nome[ind],self.endereco[ind],self.telresidencial[ind]))
        encontrados = encontrados+1
      ind = ind+1   #INCREMENTANDO O INDICE
      
    if (encontrados == 0):
      print('Deculpe! Nao Localizei nunguem com esse nome na agenda :(')
    else:
      deletar = int(input('Digite o indice da pessoa para deletar'))
      del self.nome[deletar]
      del self.endereco[deletar]
      del self.telcomercial[deletar]
      del self.telresidencial[deletar]
      del self.celular[deletar]
      del self.email[deletar]
      print('Removido com sucesso!')
  
  def listar(self):
    ind=0
    for i in self.nome:
      print('%i | %s | %s | %s |'%(ind ,self.nome[ind],self.endereco[ind],self.telresidencial[ind]))
      ind=ind+1
      
      
      
a = Agenda()    #VARIAVEL DE OBJETO

def cadastra():           #Essa função é chamada para cadastrar uma nova pessoa
  i=1
  while(i==1):
    n = input('Nome: ')
    a.add_nome(n)

    n = input('Endereco: ')
    a.add_end(n)

    n = input('Telefone Comercial: ')
    a.add_tc(n)

    n = input('Telefone Residencial: ')
    a.add_tr(n)

    n = input('Telefone Celular: ')
    a.add_cel(n)

    n = input('Email: ')
    a.add_em(n)
    print('***********Contato Cadastrado com sucesso!!!**********\n')
    e = '1'
    ##############################################################BLOCO USADO PARA TRATAR ERRO  
    while(type(e)!=int):   #SE 'E' FOR DIFERENTE DE INT INICIA-SE O LOOP ATE QUE SEJA DIGITADO UM NUMERO 
      e = input('Deseja cadastrar outra pessoa? 1=SIM / 0=NÃO: ')
      if (str.isnumeric(e)):  #VERIFICA SE FOI DIGITADO UM NUMERO
        e = int(e)            #CASO SEJA UM NUMERO CONVERTE PARA INTEIRO E SAI DO LOOP
        
    if type(e) == int:
      i=e                     #ATRIBUI A VARIAVEL TRATADA AO 'I' p/ SAIR DO LOOP


    

i=1
while(i==1):
  print('----------------------------------------------------------')
  print('-------------------AGENDA PESSOAL-------------------------')
  print('----------------------------------------------------------')
  print('1-> Cadastrar   2-> Excluir    3-> Listar Todos')
  op = int(input('Digite uma opção:'))
  
  if (op==1):
    cadastra()
    
  if (op==2):
    busca = input('Buscar: ')
    a.buscar(busca)
    
  if (op==3):
    a.listar()
