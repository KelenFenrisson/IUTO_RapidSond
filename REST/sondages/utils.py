########################################################################################################################
# UTILS MODULE : fonctions utilitaires
########################################################################################################################
import os


def mkpath(p):
    """
    Fonction mkpath : retourne le chemin absolu d'un fichier en fonction de son chemin relatif
    :param p: String, chemin relatif du fichier
    :return: String, chemin absolu du fichier
    """
    return os.path.normpath(os.path.join(os.path.dirname(__file__),	p))