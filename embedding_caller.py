import os
import requests

EMBEDDING_API_URL = "https://api.ai.prod.eu-central-1.aws.ml.hana.ondemand.com/v2/inference/deployments/d39c204ced795aac/embeddings/?api-version=2023-05-15"
AUTH_URL = os.environ["SAP_AUTH_URL"]
CLIENT_ID = os.environ["SAP_CLIENT_ID"]
CLIENT_SECRET = os.environ["SAP_CLIENT_SECRET"]

def get_sap_token():
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    headers = { "Content-Type": "application/x-www-form-urlencoded" }
    response = requests.post(AUTH_URL, data=data, headers=headers)
    response.raise_for_status()
    return response.json()["access_token"]

def get_embedding(text):
    token = get_sap_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
	"AI-Resource-Group": "default"
    }
    print("✅ Headers:", headers)
    payload = { "input": text }
    response = requests.post(EMBEDDING_API_URL, json=payload, headers=headers)
    response.raise_for_status()
    embedding = response.json()["embeddings"][0]
    print("✅ Embedding:", embedding)
    return embedding

# Example usage
if __name__ == "__main__":
    get_embedding("SAP AI Core makes enterprise AI scalable.")
