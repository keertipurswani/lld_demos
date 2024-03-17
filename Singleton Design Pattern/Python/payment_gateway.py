class PaymentGatewayManager():

    __instance = None
    __config = None

    def __init__(self):
        if not self.__instance:
            print("Initializing Payment gateway instance")
            self.__config = {"payment_gateway_name": "Stripe"}
        else:
            raise RuntimeError("Attempt to instantiate a second instance")

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = PaymentGatewayManager()
        return cls.__instance

    def get_config(self):
        return self.__config


def main():
    pg_manager = PaymentGatewayManager.get_instance()
    new_pg_manager = PaymentGatewayManager.get_instance()

    print(pg_manager.get_config())
    print(new_pg_manager.get_config())

    if id(pg_manager) == id(new_pg_manager):
        print("Both instances are the same. Singleton pattern is working.")
    else:
        print("Singleton pattern is not working correctly.")

    # PaymentGatewayManager()  # uncomment this to see a error being thrown by class.


if __name__ == "__main__":
    main()
