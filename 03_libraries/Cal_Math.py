class Cal_Math:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b
        #print(f"Init Successful with Values {self.a} {self.b}")

    def cals_add(self, a, b):
        return str(int(a) + int(b))

    def cals_sub(self):
            return self.a - self.b

    def cals_mul(self):
            return self.a * self.b

    def cals_div(self):
        return self.a / self.b
