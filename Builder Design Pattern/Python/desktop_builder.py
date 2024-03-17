class Desktop:
    # _ for internal variables.
    _motherboard = None
    _processors = None
    _memory = None
    _storage = None
    _graphics_card = None

    def display(self):
        print("#################################")
        print("Desktop Specs:")
        print(f"Motherboard: {self._motherboard}")
        print(f"Processors: {self._processors}")
        print(f"Memory: {self._memory}")
        print(f"Storage: {self._storage}")
        print(f"Graphics Card: {self._graphics_card}")
        print("#################################\n")

    def get_motherboard(self):
        return self._motherboard

    def set_motherboard(self, motherboard):
        self._motherboard = motherboard

    def get_processors(self):
        return self._processors

    def set_processors(self, processors):
        self._processors = processors

    def get_memory(self):
        return self._memory

    def set_memory(self, memory):
        self._memory = memory

    def get_storage(self):
        return self._storage

    def set_storage(self, storage):
        self._storage = storage

    def get_graphics_card(self):
        return self._graphics_card

    def set_graphics_card(self, graphics_card):
        self._graphics_card = graphics_card


class DesktopBuilder():
    _desktop = None

    def __init__(self):
        self._desktop = Desktop()

    def build_motherboard(self):
        pass

    def build_processors(self):
        pass

    def build_memory(self):
        pass

    def build_storage(self):
        pass

    def build_graphics_card(self):
        pass

    def get_desktop(self):
        return self._desktop


class DellDesktopBuilder(DesktopBuilder):

    def build_motherboard(self):
        self._desktop.set_motherboard("Dell Motherboard")

    def build_processors(self):
        self._desktop.set_processors("Dell Processor - Intel i7")

    def build_memory(self):
        self._desktop.set_memory("Dell Memory - 32GB DDR3")

    def build_storage(self):
        self._desktop.set_storage("Dell Storage - 1TB HDD")

    def build_graphics_card(self):
        self._desktop.set_graphics_card(
            "Dell Graphics Card - NVIDIA GeForce GTX 1650")


class HPDesktopBuilder(DesktopBuilder):

    def build_motherboard(self):
        self._desktop.set_motherboard("HP Motherboard")

    def build_processors(self):
        self._desktop.set_processors("HP Processor - Intel i7")

    def build_memory(self):
        self._desktop.set_memory("HP Memory - 32GB DDR3")

    def build_storage(self):
        self._desktop.set_storage("HP Storage - 1TB HDD")

    def build_graphics_card(self):
        self._desktop.set_graphics_card(
            "HP Graphics Card - NVIDIA GeForce GTX 1650")


class DesktopDirector():

    def build_desktop(self, builder):
        builder.build_motherboard()
        builder.build_processors()
        builder.build_memory()
        builder.build_storage()
        builder.build_graphics_card()
        return builder.get_desktop()


def main():
    desktop_director = DesktopDirector()

    dell_builder = DellDesktopBuilder()
    dell_desktop = desktop_director.build_desktop(dell_builder)

    hp_build = HPDesktopBuilder()
    hp_desktop = desktop_director.build_desktop(hp_build)

    dell_desktop.display()
    hp_desktop.display()


if __name__ == "__main__":
    main()
