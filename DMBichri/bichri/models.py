## into your database.
from __future__ import unicode_literals

from django.db import models

class Appartenance(models.Model):
    codemembre = models.ForeignKey('Membre', db_column='codeMembre')  # Field name made lowercase.
    identite = models.ForeignKey('Entite', db_column='idEntite')  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=45, blank=True)  # Field name made lowercase.
    codeexercice = models.ForeignKey('Exercice', db_column='codeExercice')  # Field name made lowercase.
    dateadhesion = models.DateField(db_column='dateAdhesion', blank=True, null=True)  # Field name made lowercase.
    typeadhesion = models.CharField(db_column='typeAdhesion', max_length=45, blank=True)  # Field name made lowercase.
    niveau = models.CharField(max_length=45, blank=True)
    fonction = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'appartenance'


class Appartetab(models.Model):
    idappartetab = models.IntegerField(db_column='idAppartEtab')  # Field name made lowercase.
    dateappart = models.DateField(db_column='dateAppart', blank=True, null=True)  # Field name made lowercase.
    datefin = models.DateField(db_column='dateFin', blank=True, null=True)  # Field name made lowercase.
    idetablissement = models.ForeignKey('Etablissement', db_column='idEtablissement')  # Field name made lowercase.
    codemembre = models.ForeignKey('Membre', db_column='codeMembre')  # Field name made lowercase.
    iddomaine = models.ForeignKey('Domaine', db_column='idDomaine')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appartetab'


class Cotisation(models.Model):
    idcotisation = models.IntegerField(db_column='idCotisation', primary_key=True)  # Field name made lowercase.
    codemembre = models.ForeignKey('Membre', db_column='codeMembre')  # Field name made lowercase.
    datecotisation = models.DateField(db_column='dateCotisation', blank=True, null=True)  # Field name made lowercase.
    montant = models.IntegerField(blank=True, null=True)
    idtypecotisation = models.ForeignKey('Typecotisation', db_column='idTypeCotisation')  # Field name made lowercase.
    idevenement = models.ForeignKey('Evenement', db_column='idEvenement', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cotisation'


class Domaine(models.Model):
    iddomaine = models.IntegerField(db_column='idDomaine', primary_key=True)  # Field name made lowercase.
    codedomaine = models.CharField(db_column='codeDomaine', max_length=45, blank=True)  # Field name made lowercase.
    libelledomaine = models.CharField(db_column='libelleDomaine', max_length=45, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'domaine'


class Entite(models.Model):
    identite = models.CharField(db_column='idEntite', primary_key=True, max_length=45)  # Field name made lowercase.
    identiteparent = models.ForeignKey('self', db_column='idEntiteParent', blank=True, null=True)  # Field name made lowercase.
    libelleentite = models.CharField(db_column='libelleEntite', max_length=45, blank=True)  # Field name made lowercase.
    idtypeentite = models.ForeignKey('Typeentite', db_column='idTypeEntite')  # Field name made lowercase.
    coderegion = models.ForeignKey('Region', db_column='codeRegion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entite'


class Etablissement(models.Model):
    idetablissement = models.IntegerField(db_column='idEtablissement')  # Field name made lowercase.
    nometablissement = models.CharField(db_column='nomEtablissement', max_length=45, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=45, blank=True)
    idtypeetab = models.ForeignKey('Typeetab', db_column='idTypeEtab')  # Field name made lowercase.
    idetablissementparent = models.ForeignKey('self', db_column='idEtablissementParent')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'etablissement'


class Evenement(models.Model):
    idevenement = models.IntegerField(db_column='idEvenement', primary_key=True)  # Field name made lowercase.
    libelleevenement = models.CharField(db_column='libelleEvenement', max_length=45, blank=True)  # Field name made lowercase.
    dateevenement = models.DateField(db_column='dateEvenement', blank=True, null=True)  # Field name made lowercase.
    lieuevenement = models.CharField(db_column='lieuEvenement', max_length=45, blank=True)  # Field name made lowercase.
    identite = models.ForeignKey(Entite, db_column='idEntite')  # Field name made lowercase.
    codeexercice = models.ForeignKey('Exercice', db_column='codeExercice')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evenement'


class Exercice(models.Model):
    codeexercice = models.IntegerField(db_column='codeExercice', primary_key=True)  # Field name made lowercase.
    libelleexercice = models.CharField(db_column='libelleExercice', max_length=45, blank=True)  # Field name made lowercase.
    encours = models.IntegerField(db_column='enCours', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exercice'


class Membre(models.Model):
    codemembre = models.CharField(db_column='codeMembre', primary_key=True, max_length=50)  # Field name made lowercase.
    nommembre = models.CharField(db_column='nomMembre', max_length=45, blank=True)  # Field name made lowercase.
    prenommembre = models.CharField(db_column='prenomMembre', max_length=45, blank=True)  # Field name made lowercase.
    datenaiss = models.DateField(db_column='dateNaiss', blank=True, null=True)  # Field name made lowercase.
    lieunaiss = models.CharField(db_column='lieuNaiss', max_length=45, blank=True)  # Field name made lowercase.
    coderegion = models.ForeignKey('Region', db_column='codeRegion')  # Field name made lowercase.
    email = models.CharField(max_length=45, blank=True)
    adress1 = models.CharField(max_length=45, blank=True)
    adress2 = models.CharField(max_length=45, blank=True)
    numtel1 = models.CharField(db_column='numTel1', max_length=45, blank=True)  # Field name made lowercase.
    numtel2 = models.CharField(db_column='numTel2', max_length=45, blank=True)  # Field name made lowercase.
    etatcompte = models.CharField(db_column='etatCompte', max_length=45, blank=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userId', max_length=45, blank=True)  # Field name made lowercase.
    mdp = models.CharField(max_length=45, blank=True)
    idtypemembre = models.ForeignKey('Typemembre', db_column='idTypeMembre')  # Field name made lowercase.
    etat = models.CharField(max_length=45, blank=True)
    anneebac = models.IntegerField(db_column='anneeBac', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'membre'


class Region(models.Model):
    coderegion = models.CharField(db_column='codeRegion', primary_key=True, max_length=10)  # Field name made lowercase.
    region = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'region'


class Responsabilite(models.Model):
    idresponsabilite = models.IntegerField(db_column='idResponsabilite', primary_key=True)  # Field name made lowercase.
    codemembre = models.ForeignKey(Membre, db_column='codeMembre')  # Field name made lowercase.
    identite = models.ForeignKey(Entite, db_column='idEntite')  # Field name made lowercase.
    codeexercice = models.ForeignKey(Exercice, db_column='codeExercice')  # Field name made lowercase.
    titreresponsabilite = models.CharField(db_column='TitreResponsabilite', max_length=45)  # Field name made lowercase.
    datedeb = models.DateField(db_column='dateDeb')  # Field name made lowercase.
    datefin = models.DateField(db_column='dateFin', blank=True, null=True)  # Field name made lowercase.
    observation = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'responsabilite'


class Typecotisation(models.Model):
    idtypecotisation = models.IntegerField(db_column='idTypeCotisation', primary_key=True)  # Field name made lowercase.
    libelletypecotisation = models.CharField(db_column='libelleTypeCotisation', max_length=45, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typecotisation'


class Typeentite(models.Model):
    idtypeentite = models.IntegerField(db_column='idTypeEntite', primary_key=True)  # Field name made lowercase.
    libelletypeentite = models.CharField(db_column='libelleTypeEntite', max_length=45, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'typeentite'


class Typeetab(models.Model):
    idtypeetab = models.IntegerField(db_column='idTypeEtab', primary_key=True)  # Field name made lowercase.
    typeetab = models.CharField(db_column='typeEtab', max_length=45, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'typeetab'


class Typemembre(models.Model):
    idtypemembre = models.IntegerField(db_column='idTypeMembre', primary_key=True)  # Field name made lowercase.
    libelletypemembre = models.CharField(db_column='libelleTypeMembre', max_length=45, blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'typemembre'