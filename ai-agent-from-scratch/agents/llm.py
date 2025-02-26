from transformers import pipeline

class LLMAgent:
    def __init__(self):
        self.chatbot = pipeline("text-generation", model="distilgpt2")

    def respond(self, user_input):
        response = self.chatbot(user_input, max_length=50, num_return_sequences=1)
        return response[0]["generated_text"]