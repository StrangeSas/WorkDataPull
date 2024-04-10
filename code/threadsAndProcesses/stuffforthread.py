import concurrent.futures
import time
import threading
import multiprocessing

start = time.perf_counter()

def do_smt(a):
    print(f'sleep for {a} seconds')
    time.sleep(a)
    return"done"

#Threads
"""
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs= [5,4,3,2,1]
    results = executor.map(do_smt, secs)
    #results = [executor.submit(do_smt, 1) for _ in range(10)]
    #print([i.result() for i in results])
"""
#Processes
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs= [5,4,3,2,1]
    results = executor.map(do_smt, secs)
    #results = [executor.submit(do_smt, 1.5) for _ in range(20)]
    #print([i.result() for i in results])


finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)}second(s)')

"""
А ведь по сути, для ускорения обработки всех приколов из дата аналитики - я могу
мульти треадинг, чтобы не занимать столько времени просто ожидая что какая-то функция
закончит обрабатываться и продолжить делать то, что не требует этой функции.
И не ждать по пол часа на простую обработку различных приколов, которые только можно найти
Ну и мультипроцессы спокойно можно использовать для деления крупных датасетов, для спокойной и 
быстрой обработки данных внутри огромных массивов, для уменьшения времени ожидания и ускорения
общей работы.

"""