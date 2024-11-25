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
        Validates if the request body matches the Telegram bot message structure for both 
        `callback_query` and `message` formats.

        Parameters
        ----------
        request_body : bytes
            The raw body of the request, typically in JSON format.

        Returns
        -------
        bool
            True if the structure matches either the `callback_query` or `message` format, otherwise False.
        """
        try:
            data = json.loads(request_body.decode("utf-8"))

            if 'callback_query' in data:
                required_keys = ["update_id", "callback_query"]
                callback_query_keys = ["id", "from", "message", "data"]
                from_keys = ["id", "is_bot", "first_name", "language_code"]
                message_keys = ["message_id", "from", "chat", "date", "text"]
                chat_keys = ["id", "first_name", "type"]

                if not all(key in data for key in required_keys):
                    return False
                callback_query = data['callback_query']
                if not all(key in callback_query for key in callback_query_keys):
                    return False
                if not all(key in callback_query["from"] for key in from_keys):
                    return False
                if not all(key in callback_query["message"] for key in message_keys):
                    return False
                if not all(key in callback_query["message"]["chat"] for key in chat_keys):
                    return False

            elif 'message' in data:
                required_keys = ["update_id", "message"]
                message_keys = ["message_id", "from", "chat", "date", "text"]
                from_keys = ["id", "is_bot", "first_name", "language_code"]
                chat_keys = ["id", "first_name", "type"]

                if not all(key in data for key in required_keys):
                    return False
                message = data['message']
                if not all(key in message for key in message_keys):
                    return False
                if not all(key in message["from"] for key in from_keys):
                    return False
                if not all(key in message["chat"] for key in chat_keys):
                    return False
            else:
                return False

            return True

        except (json.JSONDecodeError, KeyError, AttributeError):
            return False

    def identify_bot(self, request_body):
        if self.validate_telegram(request_body):
            return "telegram"
        return "unknown"
