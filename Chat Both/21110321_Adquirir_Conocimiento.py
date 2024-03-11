class KnowledgeBase:
    def __init__(self):
        self.knowledge = {
            "Hola": "Hola, ¿cómo estás?",
            "¿Cómo estas?": "Estoy bien, gracias por preguntar.",
            "¿De que te gustaría hablar?": "Podemos hablar de cualquier cosa. ¿Tienes algo en mente?"
        }

    def add_knowledge(self, question, answer):
        self.knowledge[question] = answer

    def get_response(self, question):
        return self.knowledge.get(question, "Lo siento, no entiendo. ¿Podrías enseñarme algo nuevo?")


def main():
    knowledge_base = KnowledgeBase()

    while True:
        user_input = input("Tú: ")
        response = knowledge_base.get_response(user_input)

        if response == "Lo siento, no entiendo. ¿Podrías enseñarme algo nuevo?":
            new_question = input("Bot: " + response + "\n" + "Por favor ingresa una pregunta nueva: ")
            new_answer = input("Bot: " + "Por favor ingresa la respuesta para '" + new_question + "': ")
            knowledge_base.add_knowledge(new_question, new_answer)
            print("Bot: ¡Gracias por enseñarme!")
        else:
            print("Bot:", response)


if __name__ == "__main__":
    main()
