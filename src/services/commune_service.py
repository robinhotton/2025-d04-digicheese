from sqlmodel import Session
from typing import Any
from ..repositories import CommuneRepository as repository
from ..models import CommuneCreate, CommunePatch
from .abstract_service import AbstractService

class CommuneService(AbstractService):
    """Service for Commune business logic, extending the AbstractService."""
    
    # Définition du repository spécifique pour ce service
    repository = repository
    
    ######################################
    # Méthodes de traitement des données #
    ######################################
    
    @classmethod
    def _process_data(cls, data: CommuneCreate | CommunePatch) -> Any:
        """Logique métier spécifique aux communes."""
        
        data_dict = cls._unpack_schema(data)
        
        # Traitement des données
        if "name" in data_dict and data_dict["name"]:
            # Normaliser le nom de la commune (première lettre en majuscule)
            data_dict["name"] = data_dict["name"].strip().title()
        
        if "postal_code" in data_dict and data_dict["postal_code"]:
            # Nettoyer et valider le code postal (5 chiffres)
            postal_code = str(data_dict["postal_code"]).strip()
            if not postal_code.isdigit() or len(postal_code) != 5:
                raise ValueError("Le code postal doit contenir exactement 5 chiffres")
            data_dict["postal_code"] = postal_code
        
        if "department_code" in data_dict and data_dict["department_code"]:
            # Normaliser le code département
            dept_code = str(data_dict["department_code"]).strip().upper()
            data_dict["department_code"] = dept_code
        
        return data_dict
    
    ################################################################
    # Fonctionnalité complémentaire pour la validation des données #
    ################################################################

    # Méthodes métier spécifiques
    @classmethod
    def get_by_postal_code(cls, postal_code: str, session: Session) -> list[dict]:
        """Récupère toutes les communes avec un code postal donné."""
        if not postal_code or len(postal_code.strip()) != 5:
            raise ValueError("Le code postal doit contenir exactement 5 chiffres")
        return cls.repository.get_by_postal_code(postal_code.strip(), session)
    
    @classmethod
    def get_by_department_code(cls, department_code: str, session: Session) -> list[dict]:
        """Récupère toutes les communes d'un département."""
        if not department_code or len(department_code.strip()) < 2:
            raise ValueError("Le code département doit contenir au moins 2 caractères")
        return cls.repository.get_by_department_code(department_code.strip().upper(), session)
    
    @classmethod
    def search_by_name(cls, name_pattern: str, session: Session) -> list[dict]:
        """Recherche des communes par nom."""
        if not name_pattern or len(name_pattern.strip()) < 2:
            raise ValueError("Le nom recherché doit contenir au moins 2 caractères")
        return cls.repository.search_by_name(name_pattern.strip(), session)
    
    @classmethod
    def validate_postal_code_department(cls, postal_code: str, department_code: str) -> bool:
        """Valide que le code postal correspond au département."""
        if not postal_code or not department_code:
            return False
        
        # Les 2 premiers chiffres du code postal correspondent généralement au département
        postal_dept = postal_code[:2]
        
        # Cas spéciaux (DOM-TOM, Corse, etc.)
        special_cases = {
            "2A": ["200", "201"],  # Corse du Sud
            "2B": ["202", "203"],  # Haute-Corse
            "971": ["971"],        # Guadeloupe
            "972": ["972"],        # Martinique
            "973": ["973"],        # Guyane
            "974": ["974"],        # Réunion
            "975": ["975"],        # Saint-Pierre-et-Miquelon
            "976": ["976"],        # Mayotte
        }
        
        dept_upper = department_code.upper()
        if dept_upper in special_cases:
            return postal_code[:3] in special_cases[dept_upper]
        
        # Cas général : département à 2 chiffres
        return postal_dept == department_code.zfill(2)