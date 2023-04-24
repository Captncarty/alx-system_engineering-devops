#!/usr/bin/python3

"""Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userID": sys.argv[1]}).json()
    
    fix_in = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with task({})/({}):".format(
        user.get("name"), len(fix_in), len(todo)))
    [print("\t {}".format(c)) for c in fix_in]