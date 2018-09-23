class Bank:
    def __init__(self, name, clients_number, credit_number):
        self.name = name
        self.clients_number = clients_number
        self.credit_number = credit_number

    def __str__(self):
        return "Bank name: " + self.name + ", " + \
               "customers amount: " + str(self.clients_number) + ", " + \
               "credits given amount: " + str(self.credit_number)
