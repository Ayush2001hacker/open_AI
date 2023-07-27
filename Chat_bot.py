import openai
import os
from statistics import mean
import time
openai.api_key  = ""


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    try:
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,)
        
        return response.choices[0].message["content"]
        
    except openai.error.ServiceUnavailableError as e:
        
        return "ServiceError"
        
        

    except openai.error.RateLimitError as e:
        print(f"due to {e} we are shutting down the system !!")
        return "RateError"
        



    
    




