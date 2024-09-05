import platform
import psutil
import socket
import getpass
import wmi

def system_version():
    return platform.platform()

class ProcessorInfo:

    def __init__(self):
        self.c = wmi.WMI()
        self.processor = self._get_processor()

    def _get_processor(self):
        processor_list = self.c.WIN32_Processor()
        return processor_list[0]

    def get_name(self):
        return self.processor.Name

    def get_max_clock_speed(self):
        return self.processor.MaxClockSpeed

    def get_number_of_cores(self):
        return self.processor.NumberOfCores

    def get_number_of_logical_processor(self):
        return self.processor.NumberOfLogicalProcessors

    def display_processor_info(self):
        print("Processor: ")
        print("Name: " + str(self.get_name()))
        print("Number of coress: " + str(self.get_number_of_cores()))
        print("Number of logical processor: " + str(self.get_number_of_logical_processor()))
        print("Max clock speed: " + str(self.get_max_clock_speed()) + "\n")

class RAMInfo:
    def __init__(self):
        self.memory = psutil.virtual_memory()
        self.total_memory = self.memory.total / (1024 ** 3)
        self.available_memory = self.memory.available / (1024 ** 3)
        self.used_memory = self.memory.used / (1024 ** 3)
        self.c = wmi.WMI()

    def display_ram_info(self):
        print("RAM: ")
        for memory in RAM_stats.c.Win32_PhysicalMemory():
            print("Model: " + str(memory.model))
            print("Speed: " + str(memory.speed))
            print("Capacity: " + str(round(int(memory.Capacity) / 1023 ** 3, 3)) + "GB")
        print("Total memory: " + str(round(RAM_stats.total_memory, 3)) + "GB")
        print("Total available: " + str(round(RAM_stats.available_memory, 3)) + "GB")
        print("Total used: " + str(round(RAM_stats.used_memory, 3)) + "GB \n")

class MonitorInfo:
    def __init__(self):
        self.c = wmi.WMI()
        self.monitors = self._get_monitors()

    def _get_monitors(self):
        return self.c.WIN32_DesktopMonitor()

    def get_monitor_info(self):
        info = []
        for monitor in self.monitors:
            info.append({
                "Name": monitor.Name,
                "Screen Width": monitor.ScreenWidth,
                "Screen Height": monitor.ScreenHeight,
                "Monitor Type": monitor.MonitorType
            })
        return info

    def display_monitor_info(self):
        print("Monitors: ")
        for index, monitor in enumerate(self.get_monitor_info(), start = 1):
            print("Monitor: " + str(index))
            for key, value in monitor.items():
                print(str(key) + str(value))
        print("")

def get_host_name():
    return socket.gethostname()

def get_host_address():
    return socket.gethostbyname(socket.gethostname())

def get_domain_user_name():
    return getpass.getuser()

if __name__ == '__main__':

    print("------------------------------------------------------------------------")
    system_version = system_version()
    print("System: " + str(system_version) + "\n")

    processor_stats = ProcessorInfo()
    processor_stats.display_processor_info()

    RAM_stats = RAMInfo()
    RAM_stats.display_ram_info()

    monitor_stats = MonitorInfo()
    monitor_stats.display_monitor_info()

    print("Host: ")
    print("Host name: " + str(get_host_name()))
    print("Host address: " + str(get_host_address()))
    print("Domain user name: " + str(get_domain_user_name()))

    print("------------------------------------------------------------------------")
