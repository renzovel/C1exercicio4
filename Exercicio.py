#para colocar na messagen
pula="""
#######################################################
"""
#menu principal
menu="""Autor:renzo.veliz1br@gmail.com
Menu de opções:

1. Média aritmética
2. Média ponderada
3. Sair  

Digite a opção desejada:
"""
#opcao de continuar
msgCotinua="Pressione ENTER para continuar!"

#numeracoes en letras
numeracao=["primeira", "segunda", "terceira"]

#vai se repetir sempre que a opcao nao for sair
while True:
    try:
        #pedimos a opcao do usuario
        opcao=int(input(menu))
        if opcao==1:  #se for um calculamos a media aritmetica
            #salvamos a notas aqui
            notas=[]
            #repetimos enquanto nao sejam introducidas duas notas
            while True:
                try:
                    if len(notas)<2:
                        #se temos menos de 2 notas carregadas, pedimos a proxima nota
                        nota=float(input(f"Introdusca a {numeracao[len(notas)]} nota:"))
                        #se a nota for negativa exemplo -12 lancamos un error
                        if nota<0:
                            raise
                        #no caso que esteja tudo bem salvamos a nota
                        notas.append(nota);
                    else:
                        #se foram carregada as duas notas fazemos o calculo
                        print(f'{pula}Resultado da media aritmetica e : {(notas[0]+notas[1])/2}{pula}')
                        #pedimos para pressionar ENTER para sair ao menu principal
                        input(msgCotinua)
                        break
                except Exception:
                    print(f"{pula}A nota esta errada, tenta de novo.{pula}")
        elif opcao==2: #se for dois calculamos a media aritmetica
            #salvamos a notas aqui
            notas=[]
            #salvamos os pesos das notas aqui
            pesos=[]
            #repetimos enquanto nao sejam introducidas tres notas e tres pesos
            while True:
                try:
                    if len(notas)<3:
                        #se temos menos de 2 notas carregadas, pedimos a proxima nota
                        nota=float(input(f"Introdusca a {numeracao[len(notas)]} nota:"))
                        #se a nota for negativa exemplo -10 lancamos un error
                        if nota<0:
                            raise
                        #no caso que esteja tudo bem salvamos a nota
                        notas.append(nota)
                        #repetimos enquanto nao sejan introducido o peso da nota
                        while True:
                            try:
                                #pedimos o peso da nota
                                peso=float(input(f"Introdusca o peso da {numeracao[len(pesos)]} nota:"))
                                #se o peso for negativo exemplo -1 lancamos un error
                                if peso<0:
                                    raise
                                #no caso que esteja tudo bem salvamos o peso e saimos do wile
                                pesos.append(peso)
                                break
                            except Exception:
                                print(f"{pula}O peso esta errado, tenta de novo.{pula}")
                    else:
                        notaspesos=0
                        sumpesos=0
                        #passamos pelos indices do array de notas salvas pasar multiplicar e sumar
                        for i in range(0, len(notas)):
                            notaspesos+=notas[i]*pesos[i]
                            sumpesos+=pesos[i] 
                        #depois de feito o calculo mostramos o resultado
                        print(f'{pula}Resultado da media ponderada e : {notaspesos/sumpesos}{pula}')
                        #pedimos ao usuario pressionar ENTER para sair ao menu principal
                        input(msgCotinua)
                        break
                except Exception:
                    print(f"{pula}A nota esta errada, tenta de novo.{pula}")
        elif opcao==3: #se for 3 saimos do programa
            #saimos
            print("Tchau!.")
            break
        else:
            print("Opção errada, tenta de novo.")
    except Exception:
        print("Opção errada, tenta de novo.") 