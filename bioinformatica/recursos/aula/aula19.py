seq = '     aCCCCTGACTGACCACTG      '

seq = seq.upper()

#seq = seq.replace(' ', '')
lista_seq = seq.split()

seq = ''.join(str(e) for e in lista_seq)

print(seq)
print('Quantidade de adenina: %d' % seq.count('A'))