class Observer():

    def update(order):
        pass


class Order():
    _id = None
    _status = None
    _observers = []
    ORDER_PLACED = "Order Placed"
    ORDER_SHIPPED = "Order Shipped"
    ORDER_DELIVERED = "Order Delivered"

    def __init__(self, id):
        self._id = id
        self._status = self.ORDER_PLACED

    def get_order_id(self):
        return str(self._id)

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status
        self.notify()

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Customer(Observer):
    _name = None

    def __init__(self, name):
        self._name = name

    def update(self, order: Order):
        print(f"Customer " + self._name +
              " has received order status update for order " +
              order.get_order_id() + " with status " + order.get_status())


class Restaurant(Observer):
    _restaurant_name = None

    def __init__(self, restaurant_name):
        self._restaurant_name = restaurant_name

    def update(self, order: Order):
        print(f"Restaurant " + self._restaurant_name +
              " has received order status update for order " +
              order.get_order_id() + " with status " + order.get_status())


class DeliveryDriver(Observer):
    _driver_name = None

    def __init__(self, driver_name):
        self._driver_name = driver_name

    def update(self, order: Order):
        print(f"Delivery driver " + self._driver_name +
              " has received order status update for order " +
              order.get_order_id() + " with status " + order.get_status())


class CallCenter(Observer):

    def update(self, order: Order):
        print(f"Call center has received order status update for order " +
              order.get_order_id() + " with status " + order.get_status())


def main():
    order = Order(1)
    customer = Customer("John")
    restaurant = Restaurant("Pizza Hut")
    delivery_driver = DeliveryDriver("Tom")
    call_center = CallCenter()

    order.attach(customer)
    order.attach(restaurant)
    order.attach(delivery_driver)
    order.attach(call_center)
    
    order.set_status(Order.ORDER_PLACED)

    order.set_status(Order.ORDER_SHIPPED)

    order.detach(call_center)

    order.set_status(Order.ORDER_DELIVERED)


if __name__ == "__main__":
    main()
