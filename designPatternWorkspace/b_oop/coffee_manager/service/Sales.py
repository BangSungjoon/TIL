from service.Payment import Payment

class Sales:
    def take_order(self, order):
        order.execute()
        payment = Payment(order)
        payment.execute()
        return payment