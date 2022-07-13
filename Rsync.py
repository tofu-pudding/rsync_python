import subprocess
from multiprocessing import Pool
from Loguru import my_logger

def rsync_pool(list):
    pool = Pool()
    pool.map_async(rsync, list)
    pool.close()
    pool.join()

def rsync(turple):
    cmd = ['rsync','-avP']
    if turple[2]:
        cmd.append('--delete')
    cmd.append(turple[0])
    cmd.append(turple[1])
    my_logger.info(cmd)
    subprocess.call(cmd)