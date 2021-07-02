# hr-test-python

This is the interview questions for python dev skills.

---
### 1. How do you setup local python dev environment?  
- What IDE do you use?
- How do you setup python production environment in Linux?
  - List the cli commands if possible.

---
### 2. Are you familiar using any linux distro?
- crontab
- ssh
- nfs
- nginx

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

---
### 3.1 Nginx (Optional)
- Using Nginx as the front web server (reverse proxy)
- deploy python program on port 8000

#### What to submit:
- Nginx server config
