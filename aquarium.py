class Aquarium:

    def __init__(self):
        self.fish_list = []

    def add_fish(self, fish):
        self.fish_list.append(fish)

    def feed(self):
        for fish in self.fish_list:
            fish.feed()

    def get_status(self):
        for fish in self.fish_list:
            fish.status()

    def remove_fish(self):
        for fish in self.fish_list:
            if fish.weight >= 11:
                self.fish_list.remove(fish)
            else:
                pass
