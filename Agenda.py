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

  def remove(self):
    return self.nome.pop(0)
    return self.telcomercial.pop(0)
    return self.telresidencial.pop(0)
    return self.celular.pop(0)
    return self.email.pop(0)
    return self.endereco.pop(0)

a = Agenda()

i=1
while(i==1):
  n = input('Digite seu nome: ')
  a.add_nome(n)

  n = input('Digite seu endereco: ')
  a.add_end(n)

  n = input('Telefone Comercial: ')
  a.add_tc(n)

  n = input('Telefone Residencial: ')
  a.add_tr(n)

  n = input('Digite o número do celular')
  a.add_cel(n)

  n = input('Digite seu email: ')
  a.add_em(n)
  
  i=int(input('Deseja adicionar algo mais? 1=SIM / 0=NÃO'))
