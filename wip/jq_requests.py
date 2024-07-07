import requests
import subprocess
import json

def jq_get(url):
    response = requests.get(url)

    # Extract the JSON data from the response
    json_data = response.text
    try:
        # Run the jq command to pretty-print the JSON data
        result = subprocess.run(
            ['jq', '.'],  # Use jq with the . filter to pretty-print JSON
            input=json_data,  # Pass the JSON data as a string to jq
            text=True,  # Capture the output as text
            capture_output=True,  # Capture stdout and stderr
            check=True  # Raise an exception if the command fails
        )

        string_stdout = result.stdout
        json_stdout = json.loads(string_stdout)

        return {
            'string': string_stdout,
            'json': json_stdout
        }
         
    except subprocess.CalledProcessError as e:
        # Print an error message if jq fails
        print(f"An error occurred while running jq: {e}")
