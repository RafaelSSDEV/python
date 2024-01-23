print('Bem vindo a companhia de logistica de Rafael Souza da Silva')

#Entrada de dados calculo da carga
def dimensoesObjeto():
    while True:
     try:
        a = float(input('Digite o comprimento da carga (em cm):'))
        b = float(input('Digite a largura da carga (em cm):'))
        c = float(input('Digite a altura da carga (em cm):'))
        mult = float(a * b * c)
        x = mult
        print ('Volume da carga é cm³:{:.2f}'.format(x))
        if(x <= 1000):
          return 10.00
        elif(x >= 1001) and (x < 10000):
          return 20.00
        elif(x >= 10001) and (x < 30000):
          return 30.00
        elif(x >= 30001) and (x < 100000):
          return 50.00
        else:
            print('Não aceitamos objetos com dimensoes tao grandes!\nPor favor entre com dimensoes desejadas novamente')

            continue
     except ValueError:
        print('Você digitou algo não númerico! ')
        continue

#entrada com o peso da carga
def pesoObjeto():
    while True:
     try:
        peso =float(input('Digite o peso da carga em kg:'))
        p = peso
        if(p <= 0.1):
         return 1
        elif(p <= 1) and (p >= 0.11):
         return 1.5
        elif(p <= 10) and (p >= 1.10):
         return 2
        elif(p <= 30) and (p >= 10.1):
         return 3
        else:
            print('Não aceitamos cargas tao pesadas \nPor favor entre com o peso desejado novamente!')
            continue
     except ValueError:
       print('Você digitou peso do objeto com um valor não numerico!\nPor favor entre com o peso desejado novamente!')
       continue
#opç de rota com seus valores
def rotaObjeto():
    while True:
     try:
        rota = (input('Selecione a rota: \nCR - De Curitiba para Rio de Janeiro\nCS - De Curitiba para São Paulo\nCP - De Curitiba para Pará\n'))
        r = rota
        if(r == 'CR'):
         return 2
        elif(r == 'CS'):
         return 1.5
        elif(r == 'CP'):
         return 3.2
        else:
            print('Você digitou uma rota que não existe')
            continue
     except ValueError:
       print('Você digitou uma rota que não existe! \nPor favor entre com a rota desejada novamente')
       continue
#Calculo valor total
dim = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total= dim*peso*rota
print('O total a pagar ficou R$:{:.2f} (dimensões {} * peso {} * rota {})'.format(total, dim, peso, rota))

