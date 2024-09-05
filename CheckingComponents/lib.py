import platform
import psutil
import socket
import wmi

def system_version():
    return platform.platform()
def processor_stats():
    return platform.processor()

class RAMInfo:
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 ** 3)
    available_memory = memory.available / (1024 ** 3)
    used_memory = memory.used / (1024 ** 3)
    c = wmi.WMI()

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
    print("RAM: ")
    for memory in RAM_stats.c.Win32_PhysicalMemory():
        print("Model: " + str(memory.model))
        print("Speed: " + str(memory.speed))
        print("Capacity: " + str(round(int(memory.Capacity) / 1023 ** 3, 3)) + "GB")
    print("Total memory: " + str(round(RAM_stats.total_memory, 3)) + "GB")
    print("Total available: " + str(round(RAM_stats.available_memory, 3)) + "GB")
    print("Total used: " + str(round(RAM_stats.used_memory, 3)) + "GB \n")
    host_name = host_name()
    print("Host name: " + str(host_name))
    host_address = host_address()
    print("Host address: " + str(host_address))
    print("------------------------------------------------------------------------")
