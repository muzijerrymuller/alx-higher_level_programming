#!/usr/bin/python3
"""
This Python script sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.The letter is sent in the variable q.
If no argument is given, q is set to an empty string.
If the response body is properly JSON formatted and not empty,
it displays the id and name in the format: [<id>] <name>.Otherwise,
it displays "Not a valid JSON" if the JSON is invalid,
and "No result" if the JSON is empty.
"""
import sys
import requests
if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
