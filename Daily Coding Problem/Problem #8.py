# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
# - record(order_id): adds the order_id to the log
# - get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.


class ecommerce:
    def __init__(self):
        self.orderid = None
        self.last = None
        self.log = [1,2,3,4]

    def record(self, orderid):
        new_entry = orderid
        self.log.append(new_entry)
        print(f"New log added: {new_entry}")
        # print(self.log[-1])

    def get_last(self, last):
        index = last

        if index == 1:
            print(f"The last element in the log is {self.log[-1]}")
        else:
            print(f"The last {index} elements in the log are {self.log[-index:]}")

ecom = ecommerce()
ecom.record(5)
ecom.record(6)
ecom.record(7)
print(f"Current log: {ecom.log}")
ecom.get_last(2)
ecom.record(8)
ecom.record(9)
ecom.get_last(2)
