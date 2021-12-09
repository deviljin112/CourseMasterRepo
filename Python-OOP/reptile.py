# Import a file and class in the file
from animal import Animal


class Reptile(Animal):
    def __init__(self, cold_blooded, tetrapod, amniotic_eggs):
        # Pre-define a variable in the parent
        super().__init__(True)
        self.cold_blooded = cold_blooded
        self.tetrapod = tetrapod
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = amniotic_eggs

    def seek_heat(self):
        return "I'm too cold!"

    def hunt(self):
        return "I'm hungry"

    def use_venom(self):
        return "Kill'em!"

    def attract_mate_through_scent(self):
        return "Tssss..."