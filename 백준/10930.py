import hashlib
str=input()
print(hashlib.sha256(str.encode()).hexdigest())