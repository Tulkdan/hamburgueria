from app.models import Ingrediente, Lanche
import json
import pprint as pp

def calcula_preco(lanche):
  preco = 0
  with open('mocks/mock-ingredientes.json', 'r') as f:
    ingredientes = json.load(f)
    for ingrediente in ingredientes:
      for ing in lanche.ingredientes:
        if ingrediente['id'] == ing:
          preco += ingrediente['preco']
  
  return preco

def get_ingredientes_lanche(lanche):
  aux = []
  with open('mocks/mock-ingredientes.json', 'r') as f:
    ingredientes = json.load(f)
    for ingrediente in ingredientes:
      for ing in lanche.ingredientes:
        if ingrediente['id'] == ing:
          aux.append(Ingrediente(ingrediente['id'], ingrediente['nome'], ingrediente['preco']))
  lanche.ingredientes = aux
  return lanche

def filtra_lanche(id):
  with open('mocks/mock-lanches.json', 'r') as f:
    lanches = json.load(f)
    for lanche in lanches:
      if lanche['id'] == id:
        aux = Lanche(lanche['nome'], lanche['ingredientes'])
        aux._id = lanche['id']
        return aux

  return None

def get_all_together():
  data = []
  with open('mocks/mock-lanches.json', 'r') as l:
    lanches = json.load(l)
  with open('mocks/mock-ingredientes.json', 'r') as i:
    ingredientes = json.load(i)

  for lanche in lanches:
    auxI = []
    aux = Lanche(lanche['nome'], lanche['ingredientes'])
    aux._id = lanche['id']
    for ingrediente in ingredientes:
      for ing in lanche['ingredientes']:
        if ingrediente['id'] == ing:
          auxI.append(Ingrediente(ingrediente['id'], ingrediente['nome'], ingrediente['preco']))
    aux.ingredientes = auxI
    data.append(aux)

  return data

def get_all_ingredientes():
  datas = []
  with open('mocks/mock-ingredientes.json', 'r') as f:
    data = json.load(f)
    for ingrediente in data:
      aux = Ingrediente(ingrediente['id'], ingrediente['nome'], ingrediente['preco'])
      datas.append(aux)
  return datas