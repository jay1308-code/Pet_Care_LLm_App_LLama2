import boto3
import json 
from constant import *



def load_llm(payload):

    client = boto3.client('sagemaker-runtime', region_name='ap-south-1')

    response = client.invoke_endpoint(EndpointName=ENDPOINT_NAME, ContentType="application/json",
                                    Body=json.dumps(payload))

    return response

prompt = "what is Blockchain?"

payload = {
    "inputs": prompt,
    "parameters": {
        "do_sample": True,
        "top_p": 0.6,
        "temperature": 0.8,
        "top_k": 50,
        "max_new_tokens": 512,
        "repetition_penalty": 1.03,
        "stop": ["</s>"]
    }
}

result = load_llm(payload)

final_result = result['Body']

print(final_result.read())
