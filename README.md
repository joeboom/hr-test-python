# hr-test-python

This is the interview questions for python dev skills.

---
### 1. How do you setup local python dev environment?  
- What IDE do you use?
  - VS Code is the IDE I use. 
- How do you setup python production environment in Linux?
  - List the cli commands if possible.

For setup of a python production environment I would:
- Install Homebrew (brew):
    ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```
- Install Python: 
    ```brew install python3```
- Create a Production virtual environment:
    ```python3 -m venv .prod```
- Activate .prod:
    ```. .prod/bin/activate```
- Install modules that are required in the production environment. For example to install Flask:
    ```pip3 install flask```


---
### 2. Are you familiar using any linux distro?
- crontab
- ssh
- nfs
- nginx

I have not used a linux distro for work but I have used cron and am familiar with nginx.

---
### 3. Setup a RESTful API with python & nginx.
- Using localhost
- Free to choose any python web component
- All outputs in JSON

API definition: /timestamp
> return current UNIX timestamp
```
# Test command:
curl 127.0.0.1/timestamp

# Expected outcome:
{"timestamp":1624900201}
```

API definition: /readdata
> read POST JSON input and send it back
```
# Test command:
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"abc","password":"xyz"}' \
  http://127.0.0.1/readdata

# Expected outcome:
{"username":"abc","password":"xyz"}
```

bad input
```
# Test command:
curl 127.0.0.1/noexist

# Expected outcome:  (404)
... 
404 Not Found 
...
```

#### What to submit:
- Python code

Please see 'main.py'.


