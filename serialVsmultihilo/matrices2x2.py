import numpy as np #Aveces da un falso positivo pero si jala la lib
import threading
import time

def multiMatriz(mat1,mat2,matR):
    #print(threading.current_thread().name, 'Starting')
    matR.extend(np.dot(mat1,mat2))
    #for r in matR:
    #    print(r)
    #print(threading.current_thread().name, 'Exiting')

def transMatriz(mat,mat_T):
    #print(threading.current_thread().name, 'Starting')
    mat_T.extend(np.transpose(mat))
    #for r in mat_T:
    #    print(r)    
    #print(threading.current_thread().name, 'Exiting')

if __name__ == "__main__":
    matA = [[2,3],[4,1]] #Ni idea si sera [[][]] o [][] idk nunca use python y [][] si jala
    matB = [[5,1],[8,7]]
    matC = [[3,1],[9,2]]
    matD = [[1,0],[2,3]]
    size=100000
    acumHilo=0
    acumSerial=0
    
    #MultiHilo
    for i in range(0,size):
        #time.sleep(0.2)
        start_time = time.time()
        jobs = []
        matR1 = list()
        matR2 = list()
        matR3 = list()
        matR3_T = list()
        
        thread = threading.Thread(name='hilo1', target=multiMatriz, args=(matA,matB,matR1)) #matA punto matB = matR1
        jobs.append(thread) #Mete los hilos en una lista para manejarlos mas facil
        
        thread2 = threading.Thread(name='hilo2', target=multiMatriz, args=(matC,matD,matR2)) #matC punto matD = matR2
        jobs.append(thread2) #Mete los hilos en una lista para manejarlos mas facil

        for j in jobs:
            j.start() #Arranca(Empieza) los hilos

        for j in jobs:
            j.join() #Los "syncroniza" con el main (Checa si ya acabaron los hilos antes de realizar la sig linea)
        
        #Pasos 3 y 4
        thread3 = threading.Thread(name='hilo3', target=multiMatriz, args=(matR1,matR2,matR3)) #matR1 punto matR2 = matR3
        thread3.start() #Inicia el hilo
        thread3.join() #Lo sincroniza con el main
        
        thread4 = threading.Thread(name='hilo4', target=transMatriz, args=(matR3,matR3_T)) #Inversa de matR3
        thread4.start() #Inicia el hilo
        thread4.join() #Lo sincroniza con el main
        
        #print ("List processing complete.")
        end_time = time.time()
        #print("multithreading time=", end_time - start_time, i)
        acumHilo+= end_time - start_time
    print("Multithreading tiempo promedio=", acumHilo/size)

    #Serial
    for i in range(0,size):
        #time.sleep(0.2)
        start_time = time.time()
        matR1 = list()
        matR2 = list()
        matR3 = list()
        matR3_T = list()
        multiMatriz(matA,matB,matR1)
        multiMatriz(matC,matD,matR2)
        multiMatriz(matR1,matR2,matR3)
        transMatriz(matR3,matR3_T)
        #print ("List processing complete.")
        end_time = time.time()
        #print("serial time=", end_time - start_time, i)
        acumSerial+= end_time - start_time

    print("Serial tiempo promedio=", acumSerial/size)
