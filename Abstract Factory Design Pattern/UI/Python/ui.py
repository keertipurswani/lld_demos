class IButton():

    def press(self):
        pass


class ITextBox():

    def set_text(self, text):
        pass


class MacButton(IButton):

    def press(self):
        print("Mac button pressed")


class MacTextBox(ITextBox):

    def set_text(self, text):
        print("Mac textbox set to: " + text)


class WindowsButton(IButton):

    def press(self):
        print("Windows button pressed")


class WindowsTextBox(ITextBox):

    def set_text(self, text):
        print("Windows textbox set to: " + text)


class IFactory():

    def create_button(self):
        pass

    def create_textbox(self):
        pass


class MacFactory(IFactory):

    def create_button(self):
        return MacButton()

    def create_textbox(self):
        return MacTextBox()


class WindowsFactory(IFactory):

    def create_button(self):
        return WindowsButton()

    def create_textbox(self):
        return WindowsTextBox()


class GUIAbstractFactory():

    def create_factory(self, os_type: str):
        if os_type == "mac":
            return MacFactory()
        elif os_type == "windows":
            return WindowsFactory()
        return None


def main():
    os_type = input("Enter machine OS: ").lower()
    factory = GUIAbstractFactory().create_factory(os_type)
    if factory is None:
        print("Invalid OS type")
    else:
        button = factory.create_button()
        button.press()
        textbox = factory.create_textbox()
        textbox.set_text("Hello World")


if __name__ == "__main__":
    main()
