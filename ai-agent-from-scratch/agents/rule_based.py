class RuleBasedAgent:
    def __init__(self):
        self.rules = {
            "hello": "Hi there!",
            "how are you": "I'm doing great, thanks!",
            "bye": "Goodbye!",
            "default": "Sorry, I don’t understand that."
        }

    def respond(self, user_input):
        user_input = user_input.lower().strip()
        return self.rules.get(user_input, self.rules["default"])