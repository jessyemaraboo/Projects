#Área para funções de validação de emails e senhas

import re

def validar_email(email):
  padrão = r"^\w+(\_\w+)?@\w+\.(com|gov|edu|org|io|dev|net)(\.br)?$"
  if not re.fullmatch(padrão, email):
    raise ValueError("Email inválido")


def validar_senha(senha):
  if len(senha) < 8:
    raise ValueError('A senha deve ter mais de 8 caracteres.')
  if not re.search(r"[a-z]", senha):
    raise ValueError('A senha deve conter pelo menos uma letra minúscula')
  elif not re.search(r"[A-Z]", senha):
    raise ValueError("A senha deve conter pelo menos uma letra maiúscula")
  elif not re.search(r"\d", senha):
    raise ValueError("A senha deve conter pelo menos um número")
  elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
    raise ValueError("A senha deve conter pelo menos um caractere especial")

def validador_email_senha(email, senha):
  validar_email(email)
  validar_senha(senha)
  
  return email, senha