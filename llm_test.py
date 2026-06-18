from model import llama_response, granite_response, mistral_response

def call_all_models(system_prompt, user_prompt):
    llama_result = llama_response(system_prompt, user_prompt)
    granite_result = granite_response(system_prompt, user_prompt)
    mistral_result = mistral_response(system_prompt, user_prompt)

        # Debug: show complete returned object

    print("Llama Result:")
    print("Summary:", llama_result["summary"])
    print("Sentiment:", llama_result["sentiment"])
    print("Category:", llama_result["category"])
    print("Action:", llama_result["action"])

    print("Granite Result:")
    print("Summary:", granite_result["summary"])
    print("Sentiment:", granite_result["sentiment"])
    print("Category:", granite_result["category"])
    print("Action:", granite_result["action"])

    print("Mistral Result:")
    print("Summary:", mistral_result["summary"])
    print("Sentiment:", mistral_result["sentiment"])
    print("Category:", mistral_result["category"])
    print("Action:", mistral_result["action"])

system_prompt = """
You are a customer support assistant.

Analyze the customer's message and return:
- summary
- sentiment
- category
- action

The action should be a clear recommendation for the support representative to resolve the issue.
"""

user_prompt = "I was charged 20usd extra for my subscription this month."

call_all_models(system_prompt, user_prompt) 

