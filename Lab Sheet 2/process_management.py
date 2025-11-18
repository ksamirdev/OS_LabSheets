import logging
import multiprocessing
import time

logging.basicConfig(
    filename='process_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)


def system_process(task_name):
    logging.info(f"{task_name} started")
    time.sleep(2)  
    logging.info(f"{task_name} ended")



if __name__ == '__main__':
    print("System Starting...")

    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("System Shutdown.")