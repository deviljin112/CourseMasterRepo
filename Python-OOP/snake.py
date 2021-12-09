from reptile import Reptile


class Snake(Reptile):
    def __init__(self, venom):
        super().__init__(True, False, True)
        self.forked_tongue = True
        self.venom = venom
        self.limbs = False

    def use_tongue_to_smell(self):
        return "Smells like teen spirit..."