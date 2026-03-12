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

    def retirer_voiture(self):

        if self.voiture is None:
            print("Cet employé n'a pas de voiture")
            return

        self.voiture.employe = None
        self.voiture = None

        print("Voiture retirée")
class Voiture:

    def __init__(self, marque, modele, matricule):
        self.marque = marque
        self.modele = modele
        self.matricule = matricule
        self.employe = None
