class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def time_of_withering(self):
        tmp = 0
        for flower in self.flowers:
            tmp += flower.get_lifetime()
        return tmp / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers = sorted(self.flowers, key=lambda flower: flower.get_freshness())

    def sort_by_color(self):
        self.flowers = sorted(self.flowers, key=lambda flower: flower.get_color())

    def sort_by_stem_length(self):
        self.flowers = sorted(self.flowers, key=lambda flower: flower.get_stem_length())

    def sort_by_price(self):
        self.flowers = sorted(self.flowers, key=lambda flower: flower.get_price())

    def print_bouquet(self):
        print("Bouquet consist of:")
        for flower in self.flowers:
            print(flower)

    def find_flowers_by_color(self, color):
        flowers_with_given_color = []
        for flower in self.flowers:
            if flower.get_color() == color:
                flowers_with_given_color.append(flower)
        if len(flowers_with_given_color) > 0:
            return flowers_with_given_color
        else:
            return None

    def find_flowers_by_freshness(self, freshness):
        flowers_with_given_freshness = []
        for flower in self.flowers:
            if flower.get_freshness() == freshness:
                flowers_with_given_freshness.append(flower)
        if len(flowers_with_given_freshness) > 0:
            return flowers_with_given_freshness
        else:
            return None

    def find_flowers_by_stem_length(self, stem_length):
        flowers_with_given_length = []
        for flower in self.flowers:
            if flower.get_stem_length() == stem_length:
                flowers_with_given_length.append(flower)
        if len(flowers_with_given_length) > 0:
            return flowers_with_given_length
        else:
            return None

    def find_flowers_cheaper_than_given_price(self, price):
        flowers_cheaper_than_given_price = []
        for flower in self.flowers:
            if flower.get_price() < price:
                flowers_cheaper_than_given_price.append(flower)
        if len(flowers_cheaper_than_given_price) > 0:
            return flowers_cheaper_than_given_price
        else:
            return None

    def find_flowers_by_lifetime(self, lifetime):
        flowers_by_lifetime = []
        for flower in self.flowers:
            if flower.get_lifetime() == lifetime:
                flowers_by_lifetime.append(flower)
        if len(flowers_by_lifetime) > 0:
            return flowers_by_lifetime
        else:
            return None

    def is_bouquet_contain_flower(self, flower_type):
        for flower in self.flowers:
            if type(flower) is flower_type:
                return True
        return False
