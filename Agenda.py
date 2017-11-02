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

a = Agenda()


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
    print('***********Contato Cadastrado com sucesso!!!**********')
    e=int(input('Deseja adicionar algo mais? 1=SIM / 0=NÃO: '))
    if (type
    

    
i=1
while(i==1):
  print('----------------------------------------------------------')
  print('-------------------AGENDA PESSOAL-------------------------')
  print('----------------------------------------------------------')
  print('1-> Cadastrar   2-> Pesquisar')
  op = int(input('Digite uma opção:'))
  if (op==1):
    cadastra()
    
#a.remover('Renan')
print (a.nome)
