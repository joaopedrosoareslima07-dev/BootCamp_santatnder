

class mensagem:
    def __init__(self, mensagem, usuario, *notificadores):
        self.mensagem = mensagem 
        self.usuario = usuario
        
        
    def enviar_mensagem(self):
        pass 
        
class  SMS(mensagem):
    def __init__(self, mensagem, usuario, *notificadores):
        super().__init__(mensagem, usuario, *notificadores)
    def enviar_mensagem(self):
        return f'[SMS] para {self.usuario}: {self.mensagem}'
    
class email(mensagem):
  def __init__(self, mensagem, usuario, email,*notificadores):
      super().__init__(mensagem, usuario, *notificadores)
    
      self.email = email
      
  def enviar_mensagem(self):
        return f'[EMAIL] para {self.email}: {self.mensagem}'
    
    
teste = SMS("Isso é um SMS", 'João')
teste2 = email('Isso é um e-mail', 'Pedro', 'pedrinho123@gamil.com')

lista_envio = [teste, teste2]

for check in lista_envio:
    print(check.enviar_mensagem())