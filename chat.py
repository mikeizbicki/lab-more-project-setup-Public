import os, pprint
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
#in python class names are in CamelCase;
#non-class names (e.g. functions/variables) are in snake_case
class Chat:
    '''
    >>> chat = Chat()
    >>> chat.send_message('my name is bob', temperature=0.0)
    '''
    client = Groq()
    def __init__(self):
        self.messages = [        
                {
                #most important thign
                "role": "system",
                "content": "Write the output in 1-2 sentences. Talk like a pirate."
            },

        ]
    def send_message(self, message):
        self.messages.append(
            {    
                #system: never change; user: changes a lot;
                # the message that you are sending to the AI      
                "role": "user",
                "content": message
            }
        )
        #in order to make non-deterministic code deterministic;
        #n general very hard CS problem;
        # in this case, has a "temperature" param that controls randomness;
        # the higher the value, the more randomness;
        # higher temperature => more creativity
        chat_completion = self.client.chat.completions.create(
            messages = self.messages, 
            model="llama-3.1-8b-instant",
            temperature = 0.0, 
            #only one, the same, determanisti now above
        )
        result = chat_completion.choices[0].message.content
        self.messages.append({
            "role": "assistant",
            "content": result
        })
        return result

if __name__ == '__main__':
    chat = Chat()
    try:
        while True: 
                user_input = input('chat>')
                response = chat.send_message(user_input)
                print(response)
    except KeyboardInterrupt:
        print("hat has ended")
