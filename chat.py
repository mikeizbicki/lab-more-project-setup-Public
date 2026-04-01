import os
from groq import Groq

from dotenv import load_dotenv
load_dotenv()
#in python class names are in CamelCase;
#non-class names (e.g. functions/variables) are in snake_case
class Chat:
    client = Groq()
    def __init__(self, message):
        self.messages = [        
                {
                #most important thign
                "role": "system",
                "content": "Write the output in 1-2 sentences."
            },

        ]
    def send_message(self):
        self.messages.append(
            {            {
                "role": "user",
                "content": message
        )
        chat_completion = self.client.chat.completions.create(
            messages = self.messages, 
            model="llama-3.1-8b-instant",
        )
        result = chat_completion.choices[0].message.content
        messages.append({
            "role": "assistent",
            "content": result
        })
        return result

'''
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            #most important thign
            "role": "system",
            "content": "Write the output in 1-2 sentences."
        },
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    #2nd most important thing to modify is the model; 
    #diff models are good at different tasks
    #it's tempting to alwasys use best model llama-3.1-8b-instant
    #but that is bad practice
    #use llama-3.1-8b-instant for debugging 
    #llama-3.3-70b-versatile for final
    model="llama-3.1-8b-instant",
)
print(chat_completion.choices[0].message.content)
'''