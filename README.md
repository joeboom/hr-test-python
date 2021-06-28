# hr-test-python

This is the interview questions for python dev skills.

---
### 1. How do you setup local python dev environment?  
- What IDE do you use?
- How do you setup python PRD environment in Linux?
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
- Using Nginx as the front (reverse proxy)
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
bad input
```
# Test command:
curl 127.0.0.1/noexist

# Expected outcome:  (standard nginx 404 output)
... 
404 Not Found 
...
```


What to submit:
- Nginx server config
- Python cod
