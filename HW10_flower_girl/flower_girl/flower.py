class Flower:
    def __init__(self, freshness, color, stem_length):
        self.freshness: int = freshness  # свежесть в днях
        self.color: str = color  # цвет строка
        self.stem_length: float = stem_length  # длина стебля в сантиметрах
        self.lifetime: int = 0  # жизненный цикл в днях
        self.price: float = 0  # цена в белорусских рублях

    def set_lifetime(self, lifetime):
        self.lifetime = lifetime

    def set_price(self, price):
        self.price = price

    def get_lifetime(self):
        return self.lifetime

    def get_freshness(self):
        return self.freshness

    def get_color(self):
        return self.color

    def get_stem_length(self):
        return self.stem_length

    def get_price(self):
        return self.price

    def __repr__(self):
        return (
            f"lifetime = {self.lifetime}, freshness = {self.freshness}, color = {self.color}, "
            f"stem_length = {self.stem_length}, price = {self.price}\n")
