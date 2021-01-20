class Fish:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def status(self):
        print(str(self.name) + " weight: " + str(self.weight) + ", color: " + str(self.color))

    def feed(self):
        self.weight += 1


class Clownfish(Fish):
    def __init__(self, name, weight, color, stripe_color):
        super().__init__(name, weight, color)
        self.stripe_color = stripe_color

    def status(self):
        print(str(self.name) + ", weight: " + str(self.weight) + ", color: " + str(self.color) +
              ", second color: " + str(self.stripe_color))

    def feed(self):
        self.weight += 1


class Tang(Fish):
    def __init__(self, name, weight, color, short_term_memory_loss=False):
        super().__init__(name, weight, color)
        self.short_term_memory_loss = short_term_memory_loss

    def status(self):
        print(str(self.name) + ", weight: " + str(self.weight) + ", color: " + str(self.color)
              + ", short term memory loss: " + str(self.short_term_memory_loss))

    def feed(self):
        self.weight += 1


class Kong(Fish):
    def __init__(self, name, weight, color):
        super().__init__(name, weight, color)

    def status(self):
        print(str(self.name) + ", weight: " + str(self.weight) + ", color: " + str(self.color))

    def feed(self):
        self.weight += 2



