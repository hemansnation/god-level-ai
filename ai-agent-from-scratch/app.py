from flask import Flask, request, render_template_string
from agents.rule_based import RuleBasedAgent
from agents.memory import MemoryAgent
from agents.chat import ChatAgent
from agents.llm import LLMAgent
from utils.api_keys import WEATHER_API_KEY
import time

app = Flask(__name__)

rule_agent = RuleBasedAgent()
memory_agent = MemoryAgent()
chat_agent = ChatAgent(WEATHER_API_KEY)
llm_agent = LLMAgent()
cache = {}

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.form["message"]
        start_time = time.time()

        if user_input in cache:
            response = cache[user_input]
        elif user_input.startswith("weather in "):
            response = chat_agent.respond(user_input)
            cache[user_input] = response
        elif user_input.startswith("my name is ") or user_input == "what’s my name":
            response = memory_agent.respond(user_input)
            cache[user_input] = response
        elif user_input in rule_agent.rules:
            response = rule_agent.respond(user_input)
            cache[user_input] = response
        else:
            response = llm_agent.respond(user_input)
            cache[user_input] = response

        latency = time.time() - start_time
        return render_template_string("""
            <form method="post">
                <input type="text" name="message" placeholder="Type here..." />
                <input type="submit" value="Send" />
            </form>
            <p><b>You:</b> {{ user_input }}</p>
            <p><b>Agent:</b> {{ response }}</p>
            <p><i>Latency: {{ latency }}s</i></p>
        """, user_input=user_input, response=response, latency=f"{latency:.2f}")
    return render_template_string("""
        <form method="post">
            <input type="text" name="message" placeholder="Type here..." />
            <input type="submit" value="Send" />
        </form>
    """)

if __name__ == "__main__":
    app.run(debug=True)