from threading import Thread 
import time, os
def initThreads(nFatnThread):
   Thread(target=fatorar,args=[nFatnThread[0],nFatnThread[1],nFatnThread[2]]).start()

def fatorar(numeroFat, nomeFat, ordem):
  print("Início da Thread " + nomeFat )
  print("");
  count = numeroFat

  while count > 1:
    fat = count
    if count == numeroFat :
       print("")
       print('Thread '+ ordem + "- " + str(count)+ "- calculo interação: " +  str(numeroFat))
       print("")
       
    else:
      numeroFat = (count) * numeroFat
      print("")
      print('Thread '+ ordem + "- " + str(count)+ "- calculo interação: " +  str(numeroFat))
      print("");
    count = count - 1  
    time.sleep(5)
   
  print('Thread '+ ordem + " Resultado: " + str(numeroFat))
  print("");
  print("Fim da Thread " + ordem)
  print("");

  
def main():
  vetorFatorial = []
  qtdFatorial = int(input("Por favor, digite a quantidade de vezes que você deseja para calcular fatorial: "))
  for x in range(0, qtdFatorial):
    numFatorial = int(input("Digite o número que deseja calcular o fatorial: "))
    ordem = x + 1
    vetorFatorial.append([numFatorial, str(ordem)+ ' - ''Fatorial ' + 'de '  + str(numFatorial), str(ordem)])
  for y in vetorFatorial:
  
    print()
    initThreads(y)
main()
