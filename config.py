from dotenv import load_dotenv
import os
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

load_dotenv()

PARAMETERS = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 100,
}

WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
WATSONX_URL = os.getenv("WATSONX_URL")

# Models supported by your account
LLAMA_MODEL_ID = "meta-llama/llama-4-maverick-17b-128e-instruct-fp8"

# Your account doesn't support Granite
GRANITE_MODEL_ID = "mistralai/mistral-small-3-1-24b-instruct-2503"

MISTRAL_MODEL_ID = "mistralai/mistral-small-3-1-24b-instruct-2503"