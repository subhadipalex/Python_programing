import hashlib

str="subhadip"
op=hashlib.md5(str.encode())
print(op.hexdigest())