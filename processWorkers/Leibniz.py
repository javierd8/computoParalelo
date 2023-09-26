#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing

def function_square(data):
    result = data*data
    return result

def pit(sumatoria):
    signo=-1
    #print(sumatoria)
    for i in range(3, 1000000, 2):
        sumatoria+=(1/i)*signo
        signo *=- 1
    #print(sumatoria)
    return sumatoria*4
    

if __name__ == '__main__':
    sumatoria = 1
    inp = list(range(1,2))
    pool = multiprocessing.Pool(processes=8)
    res = pool.map(pit,inp)

    pool.close() 
    pool.join() 

    print ('Pool    :', res)
