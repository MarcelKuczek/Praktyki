import platform
import psutil
import socket

def system_version():
    return platform.platform()
def processor_stats():
    return platform.processor()
class RAMInfo:
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 ** 3)
    available_memory = memory.total / (1024 ** 3)
    used_memory = memory.used / (1024 ** 3)

def host_name():
    return socket.gethostname()
def host_address():
    return socket.gethostbyname(socket.gethostname())

if __name__ == '__main__':

    print("------------------------------------------------------------------------")
    system_version = system_version()
    print("System: " + str(system_version))
    processor_stats = processor_stats()
    print("Processor: " + str(processor_stats))
    RAM_stats = RAMInfo()
    print("Total memory: " + str(round(RAM_stats.total_memory, 2) + "GB"))
    host_name = host_name()
    print("Host name: " + str(host_name))
    host_address = host_address()
    print("Host address: " + str(host_address))
    print("------------------------------------------------------------------------")
