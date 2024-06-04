l = input('Digite uma frase: ').upper().strip()

print('A letra "A" aparece {} vezes na frase.'.format(l.count('A')))          
print('A primeira letra "A" aparece na posição {} da frase.'.format(l.find('A')))
print('A ultima letra "A" aparece na posição {} da frase.'.format(l.rfind('A')))