from abc import ABC, abstractmethod


class NetworkDevice:

    @abstractmethod
    def clone():
        pass

    @abstractmethod
    def display():
        pass

    @abstractmethod
    def update(new_name):
        pass


class Router(NetworkDevice):

    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address

    def clone(self):
        return Router(self.name, self.ip_address)

    def update(self, new_name):
        self.name = new_name

    def display(self):
        print(f"Router: {self.name} - {self.ip_address}")


class Switch(NetworkDevice):

    def __init__(self, name, protocol):
        self.name = name
        self.protocol = protocol

    def clone(self):
        return Switch(self.name, self.protocol)

    def update(self, new_name):
        self.name = new_name

    def display(self):
        print(f"Switch: {self.name} - {self.protocol}")


def main():
    router = Router("Router1", "192.168.1.1")
    switch = Switch("Switch1", "TCP")

    router.display()
    switch.display()

    router_clone = router.clone()
    switch_clone = switch.clone()

    router_clone.update("Router2")
    switch_clone.update("Swicth2")

    router_clone.display()
    switch_clone.display()


if __name__ == "__main__":
    main()
