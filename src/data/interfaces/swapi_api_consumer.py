from abc import ABC, abstractclassmethod
from typing import Type, Tuple, Dict
from requests import Request


class SwapiApiConsumerInterface(ABC):

    @abstractclassmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        ''' Must Implement '''
        raise Exception('Must implemnt get_starships')
    
    
    @abstractclassmethod
    def get_starship_information(self, starship_id: int) -> Tuple[int, Type[Request], Dict]:
        ''' Must Implement '''
        raise Exception('Must implement get_starship_information')