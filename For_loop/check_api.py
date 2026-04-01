import requests

def check_gemini_key(api_key: str):
    url = "https://generativelanguage.googleapis.com/v1beta/models"

    headers = {
        "x-goog-api-key": api_key
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            return "VALID API KEY ✅"

        elif response.status_code in (401, 403):
            return f"INVALID / EXPIRED API KEY ❌ (status {response.status_code})"

        else:
            return f"UNKNOWN RESPONSE ⚠️ {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        return f"NETWORK ERROR: {e}"


# Example usage
key = "AIzaSyA9Z5bYFxaBAfTyHCnjZCAaH9RaC7yTTbY"
print(check_gemini_key(key))
