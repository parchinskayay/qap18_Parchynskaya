from flower_girl.flower import Flower


class Peon(Flower):
    def __init__(self, freshness, color, stem_length):
        super().__init__(freshness, color, stem_length)
        super().set_lifetime(7)
        super().set_price(38)

    def __repr__(self):
        return f"Peon:\n" + super().__repr__()
