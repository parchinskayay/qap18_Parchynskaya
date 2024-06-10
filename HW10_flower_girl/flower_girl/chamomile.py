from flower_girl.flower import Flower


class Chamomile(Flower):
    def __init__(self, freshness, color, stem_length):
        super().__init__(freshness, color, stem_length)
        super().set_lifetime(5)
        super().set_price(25)

    def __repr__(self):
        return f"Chamomile:\n" + super().__repr__()
