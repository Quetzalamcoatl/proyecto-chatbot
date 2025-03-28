from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from menu_cafe import info 

template = """
You are a owner of a coffee shop and you need to answer information about our shop.

Answer the question below always in Spanish in a friendly way.

For example: If an user ask for a price, you need to anwer in a friendly way the costn and invite him to taste it.


Here is the conversation history: {datos_negocio}

Question: {question}

Answer: 
"""
model = OllamaLLM(model="Gemma3:latest")
prompt = ChatPromptTemplate.from_template(template)
chain =prompt | model 

def chat():
    context = ""
    print("=================¡Bienvenid@! Soy Icniuh, el asistente de la UAM A. Escribe 'exit' para quitar=================")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = chain.invoke({"datos_negocio":info, "context":context, "question":user_input})
        print("Bot:", result)
        context += f"\nUser: {user_input}\nAI: {result}"


if __name__ == "__main__":
    chat()
