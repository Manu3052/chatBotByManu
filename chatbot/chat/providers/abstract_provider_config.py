from abc import ABC, abstractmethod 


class AbstractProviderConfig(ABC):
    """
    An abstract base class that defines the configuration and behavior 
    for a communication chat. This class serves as a template for 
    implementing specific chat configurations.

    Methods
    -------
    reply():
        Abstract method that must be implemented to define the logic for 
        sending a reply through the communication chat.
    """

    @abstractmethod
    def reply(self):
        """
        Send a reply through the communication chat.
        
        This method must be implemented by subclasses to define 
        the behavior of replying in the specific chat.
        """
        pass
    