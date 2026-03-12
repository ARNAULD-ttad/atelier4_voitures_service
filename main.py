class Employe:

    def __init__(self, id, nom, poste):
        self.id = id
        self.nom = nom
        self.poste = poste
        self.voiture = None

    def afficher_info(self):

        print("Employé :", self.nom)
        print("Poste :", self.poste)

        if self.voiture is not None:
            print("Voiture :", self.voiture.marque, self.voiture.modele)
        else:
            print("Aucune voiture attribuée")

    def attribuer_voiture(self, voiture):

        if self.voiture is not None:
            print("Cet employé possède déjà une voiture")
            return

        if voiture.employe is not None:
            print("Cette voiture est déjà attribuée")
            return

        self.voiture = voiture
        voiture.employe = self

        print("Voiture attribuée à", self.nom)

