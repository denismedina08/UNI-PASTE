from sys import exit

def gold_room(): 
  print("Esta sala está cheia de ouro. Quanto você pega?") 
  choice = input("> ")
  if "0" in choice or "1" in choice:
    how_much = int(choice)
  else: 
    dead("Cara, aprenda a digitar um número.") 
  if how_much < 50:
    print("Legal, você não é ganancioso, você venceu!") 
    exit(0)
  else: 
    dead("Seu ganancioso!")

def bear_room():
  print("Há um urso aqui.")
  print("O urso tem um monte de mel.")
  print("O urso gordo está na frente de outra porta.")   
  print("Como você vai mover o urso?") 
  bear_moved = False
  while True: 
    choice = input("> ")
    if choice == "take honey":
      dead("O urso olha para você e depois dá um tapa na sua cara.")
    elif choice == "taunt bear" and not bear_moved: 
      print("O urso saiu da frente da porta.")
      print("Agora você pode passar por ela.") 
      bear_moved = True
    elif choice == "taunt bear" and bear_moved:
      dead("O urso fica irritado e mastiga sua perna.") 
    elif choice == "open door" and bear_moved: 
      gold_room()
    else: 
      print("Não faço ideia do que isso significa.")

def cthulhu_room(): 
  print("Aqui você vê o grande mal Cthulhu.")
  print("Ele, seja lá o que for, olha para você e você enlouquece.") 
  print("No meio da loucura você vê um corredor no fundo.")
  print("Você corre para o corredor e salva sua vida ou come sua própria cabeça?")

  choice = input("> ")
  if "corre" in choice: 
    start()
  elif "comer a cabeça" in choice: 
    dead("Bem, isso foi saboroso!")
  else:
    cthulhu_room("Essa resposta não foi válida")

def dead(why):
  print(why, "Bom trabalho!") 
  exit(0)

def start(): 
  print("Você está em uma sala escura.")
  print("Há uma porta à sua direita e outra à sua esquerda.") 
  print("Qual você escolhe?")
  choice = input("> ")
  if choice == "esquerda": 
    bear_room()
  elif choice == "direita": 
    cthulhu_room()
  else: 
    dead("Você tropeça na sala até morrer de fome.")

start()