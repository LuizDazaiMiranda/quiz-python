print('Seja muito bem vindo ao quiz do luiz!')
usuario_responder = input('Quer começar? (S/N): ')

if usuario_responder != 'S':
    quit()

score = 0

print('Começando...')
print('(1) Quem desenvolveu a linguagem de programação Python? \n (A) Guido van Rossum \n (B) Anders Hejlsberg \n (C) Brendan Eich \n (D) James Gosling \n')
responder1 = input('Resposta: ')

if responder1 == 'A':
    print('Parabens você acertou :) \n')
    score+=1
    
else:
    print('Resposta incorreta você errou! :( ')
    
print('(2) Qual é a função usada para ler a entrada do usuário a partir do teclado em Python \n (A) keyboard_input() \n (B) read() \n (C) get_input() \n (D) input() \n')

responder2 = input('Resposta: ')

if responder2 == 'D':
    print('Parabens você acertou :) \n')
    score+=1
    
else: 
    print('Resposta incorreta você errou! :( ')
    
print('(3) Qual é o operador de atribuição em Python? \n (A) == \n (B) != \n (C) = \n (D) == \n')

responder3 = input('Resposta: ')

if responder3 == 'C':
    print('Parabens você acertou :) \n')
    score+=1
    
else: 
    print('Resposta incorreta você errou! :( ')
    
print('(4) Qual é o método utilizado para adicionar um elemento ao final de uma lista em Python? \n (A) append() \n (B) add() \n (C) extend() \n (D) insert() \n')

responder4 = input('Resposta: ')

if responder4 == 'A':
    print('Parabens você acertou :) \n')
    score+=1
    
else:
    print('Resposta incorreta você errou! :( ')
    
print('(5) Como você verifica o número de itens em uma lista em Python? \n (A)  count() \n (B) items() \n (C) size() \n (D) len() \n')

responder5 = input('Resposta: ')

if responder5 == "D":
    print('Parabens você acertou :) \n')
    score+=1
    
else:
    print('Resposta incorreta você errou! :( ')
    
print('(6) Qual é o resultado da expressão 2 ** 3 em Python? \n (A) 6 \n (B) 8 \n (C) 12 \n (D) 16 \n')

responder6 = input('Resposta: ')

if responder6 == 'B':
     print('Parabens você acertou :) \n')
     score+=1
     
else:
    print('Resposta incorreta você errou! :( ')
    
print('(7) Qual é a função usada para verificar se um objeto é de um determinado tipo em Python? \n (A) print() \n (B) typeof() \n (C) type() \n (D) isinstance() \n ')

responder7 = input('Resposta: ')

if responder7 == 'D':
    print('Parabens você acertou :) \n')
    score+=1
    
else:
    print('Resposta incorreta você errou! :( ')
    

print(f'Quiz acabou... Prontuação: {score}')