from model import llama_response, granite_response, mistral_response

def call_all_models(system_prompt, user_prompt):
    llama_result = llama_response(system_prompt, user_prompt)
    granite_result = granite_response(system_prompt, user_prompt)
    mistral_result = mistral_response(system_prompt, user_prompt)

        # Debug: show complete returned object
    print("Llama Raw Output:")
    print(llama_result)
    print("..................................")
    print("Llama Response:\n", llama_result["response"])
    print("\nGranite Response:\n", granite_result["response"])
    print("\nMistral Response:\n", mistral_result["response"])

call_all_models(
    "You are a helpful assistant who provides concise and accurate answers",
    "What is the capital of Canada? Tell me a cool fact about it as well"
)

