from snake import Snake


class Python(Snake):
    def __init__(self):
        super().__init__(False)
        self.large = True
        self.two_lungs = True

    def digest_large_pray(self):
        return "Big Nom Noms"

    def constrict(self):
        return "Chokeeeeee Time!"

    def climb(self):
        return "Slimy business"

    def shed_skin(self):
        return "Woopty Doopty Fresh Skin!"


# print(f"This is the imported name of the file '{__name__}'")  # => python
