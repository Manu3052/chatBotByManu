from abc import ABC, abstractmethod


class AbstractProviderConfig(ABC):
    """
    An abstract base class that defines the configuration and behavior 
    for a communication chat. This class serves as a template for 
    implementing specific chat configurations.

    Methods
    -------
    verify_commands():
        Abstract method to validate and interpret commands received 
        in the communication chat. Subclasses must define the logic for 
        command verification.

    reply():
        Abstract method to define the logic for sending a reply 
        through the communication chat. Subclasses must implement this.
    """

    @abstractmethod
    def verify_existing_message(self, message: str) -> bool:
        pass

    @abstractmethod
    def verify_commands(self):
        """
        Validate and interpret commands received in the chat.

        This method must be implemented by subclasses to handle specific 
        command verification logic, such as recognizing predefined 
        commands or parsing message content.

        Parameters
        ----------
        None

        Returns
        -------
        dict or None
            A dictionary with parsed command details if a valid command 
            is detected, or None if no valid command is found.
        """
        pass

    @abstractmethod
    def reply(self):
        """
        Send a reply through the communication chat.

        This method must be implemented by subclasses to define the 
        specific behavior for replying to messages in the chat.

        Parameters
        ----------
        message : dict
            A dictionary containing message details such as sender, 
            message content, and metadata.

        Returns
        -------
        None
        """
        pass
