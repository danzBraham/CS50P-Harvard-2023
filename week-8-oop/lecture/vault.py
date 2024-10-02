class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

    @property
    def galleons(self):
        return self._galleons

    @galleons.setter
    def galleons(self, galleons):
        self._galleons = galleons

    @property
    def sickles(self):
        return self._sickles

    @sickles.setter
    def sickles(self, sickles):
        self._sickles = sickles

    @property
    def knuts(self):
        return self._knuts

    @knuts.setter
    def knuts(self, knuts):
        self._knuts = knuts


def main():
    potter = Vault(100, 50, 25)
    print({"Potter": f"{potter}"})

    abra = Vault(100, 150, 200)
    print({"Abra": f"{abra}"})

    total = potter + abra
    print({"Total": f"{total}"})


if __name__ == "__main__":
    main()
