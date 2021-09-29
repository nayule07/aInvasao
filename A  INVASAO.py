numero_m = int(input('m: '))
while not(0 < numero_m < 6):
    numero_m = int(input('m: '))
 

numero_n = int(input('n: '))
while not(0 < numero_n < 11):
    numero_n = int(input('n: '))

m=[]
n=[]
 

i = 0
while i < numero_m:
    z = int(input('m[%d]: ' % i))
    if 0 < z < 500:
        m.append(z)
        i += 1
    else:
        print('Número inválido!')
 
i = 0
while i < numero_n:
    n.append(int(input('n[%d]: ' % i)))
    i += 1


sm = 0
for T in m:
    sm += T
soma = 0
while (sm != 0):
    resto = sm % 10
    sm = (sm - resto)//10
    soma = soma + resto

som = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56]

sd = soma
mult = [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]

if (sd%2) == 0:
    print('Método A')
    
    
    def troca(n, a, b):
        temp = n[a]
        n[a] = n[b]
        n[b] = temp

    def indice_maior_item(n, x):
        y = 0

        for a in range(1, x):
            if n[a] > n[y]:
                y = a
        return y

    def selection_sort(n, x):
        for tamanho in range(x, 1, -1):
            maior = indice_maior_item(n, tamanho)
            troca(n, maior, tamanho-1)

    selection_sort(n, len(n))
   
    ab = [n[i]*mult[i] for i in range(len(n))]

    sn = 0
    for nota in ab:
        sn += nota
    
else:
    print('Método B')

    soma_sequencia = [n[y] + som[y] for y in range(len(n))]
    sn = 0
    resto = 0
    soma = 0
    for numero in soma_sequencia:
        while numero != 0:
            resto = numero % 10
            numero = numero // 10
            sn = sn + resto

if sn < 369:
    print('Código corrompido!')
else:
    dia = sn % 31
    if dia == 0:
        dia = 31
    else:
        dia == dia

    num_mes = sn % 12
    if num_mes == 0:
        num_mes = 12
    else:
        num_mes == num_mes


        
    mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    if dia > 28 and mes[num_mes == 1]:
        print('Código corrompido!')

    else:
        print ('Invasão:',dia , 'de', mes[num_mes - 1])



        
