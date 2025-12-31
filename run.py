import os
from src.load_data import load_people
from src.generate_text import generate_personalized_message

os.makedirs("outputs", exist_ok=True)


people = load_people("data/sample.csv")

with open("outputs/messages.txt", "w", encoding="utf-8") as f:
    for person in people:
        message = generate_personalized_message(
            person["name"],
            person["age"],
            person["city"]
        )
        f.write(message + "\n\n")
