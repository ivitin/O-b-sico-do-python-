from random import randrange
import matplotlib.pyplot as plt

eixo_x = list (range(1,9))
eixo_y = []

#print (eixo_x)
for nota in range (8):
    eixo_y.append(randrange(0,11))
#    print(eixo_y)

plt.plot(eixo_x,eixo_y,marker = 'o')

plt.title('Notas do aluno VICTOR MOISÉS')
plt.xlabel('PROVAS')
plt.ylabel ('NOTAS')
plt.show()





