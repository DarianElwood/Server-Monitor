from monitor.monitor import Monitor
from monitor.address import Address


def main():
    a1 = Address("vps-8f5796f3.vps.ovh.net", 2303)
    a2 = Address("24.77.118.84", 2303)
    myMonitor = Monitor([a1, a2])
    print(myMonitor.fetch())

if __name__ == "__main__":
    main()