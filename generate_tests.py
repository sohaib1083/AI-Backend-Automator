import os
import re
import requests
import json

# Load environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "meta-llama/llama-4-maverick-17b-128e-instruct"
ROUTES_FILE = "app/routes.py"
TEST_FILE = "test_routes.py"

# Extract all Flask routes and their corresponding function code
def extract_routes():
    with open(ROUTES_FILE, "r") as f:
        content = f.read()
    
    # Regex to match both route and function name, considering line breaks
    route_pattern = re.findall(r'@app\.route\(["\'](.*?)["\'](?:,\s*methods=\[.*?\])?\)\s*def\s+(\w+)\s*\((.*?)\):\s*(.*?)\n', content, re.DOTALL)
    
    # Return list of tuples (route, function_code)
    return [(route, code) for route, _, _, code in route_pattern]

# Extract all routes already tested from test_routes.py using # TEST_FOR: markers
def extract_tested_routes():
    if not os.path.exists(TEST_FILE):
        return []
    with open(TEST_FILE, "r") as f:
        content = f.read()
    return re.findall(r'# TEST_FOR:\s*(.*)', content)

# Use Groq API to generate test code with both path and function logic
def generate_test_code(route, code):
    prompt = f"""
You are a Python developer. Write two pytest tests (1 positive, 1 negative) for this Flask endpoint:

Route: {route}

Function:
{code}

Tests should use the 'client' fixture from pytest-flask.
Only return Python code in this format:

# TEST_FOR: {route}
def test_<something>_positive(client):
    ...

def test_<something>_negative(client):
    ...

Do not include markdown, explanation, or extra comments. Only output valid Python code.
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        data=json.dumps(data)
    )

    if response.status_code != 200:
        raise Exception(f"Groq API Error: {response.status_code} - {response.text}")

    return response.json()["choices"][0]["message"]["content"].strip()

# Append the generated test to the test_routes.py file
def append_test(code):
    with open(TEST_FILE, "a") as f:
        f.write("\n\n" + code + "\n")

# Main function
def main():
    all_routes = extract_routes()  # List of (route, function_code) tuples
    tested_routes = extract_tested_routes()  # List of tested routes
    new_routes = [r for r in all_routes if r[0] not in tested_routes]

    if not new_routes:
        print("🎉 All routes are already tested.")
        return

    for route, code in new_routes:
        print(f"✏️ Generating test for: {route}")
        try:
            test_code = generate_test_code(route, code)  # Pass both route and code
            append_test(test_code)
            print(f"✅ Test added for: {route}")
        except Exception as e:
            print(f"❌ Failed for {route}: {e}")

if __name__ == "__main__":
    main()
