import json


class BotValidator:
    """
    A class to validate request bodies for different bot message formats.
    Each bot type has a specific validation method.

    Methods
    -------
    validate_telegram(request_body):
        Validates if the request body matches the Telegram bot message structure.
    validate_other_bot(request_body):
        Placeholder for validation logic of other bots.
    identify_bot(request_body):
        Identifies the bot type based on the request body structure.
    """

    @staticmethod
    def validate_telegram(request_body):
        """
        Validates if the request body matches the Telegram bot message structure.

        Parameters
        ----------
        request_body : bytes
            The raw body of the request, typically in JSON format.

        Returns
        -------
        bool
            True if the structure matches Telegram's message format, otherwise False.
        """
        try:
            data = json.loads(request_body.decode("utf-8"))

            required_keys = ["update_id", "message"]
            message_keys = ["message_id", "from", "chat", "date", "text"]
            from_keys = ["id", "is_bot", "first_name", "language_code"]
            chat_keys = ["id", "first_name", "type"]

            if not isinstance(data, dict):
                return False
            if not all(key in data for key in required_keys):
                return False
            if not all(key in data["message"] for key in message_keys):
                return False
            if not all(key in data["message"]["from"] for key in from_keys):
                return False
            if not all(key in data["message"]["chat"] for key in chat_keys):
                return False

            return True
        except (json.JSONDecodeError, KeyError, AttributeError):
            return False

    @staticmethod
    def validate_discord(request_body):
        return False

    def identify_bot(self, request_body):
        if self.validate_telegram(request_body):
            return "telegram"
        if self.validate_discord(request_body):
            return "discord"
        return "unknown"
