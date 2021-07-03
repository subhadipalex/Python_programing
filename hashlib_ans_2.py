import hashlib

str="subhadip"
op=hashlib.md5(str.encode())
op1=hashlib.sha1(str.encode())
op2=hashlib.sha224(str.encode())
op3=hashlib.sha256(str.encode())
print(op.hexdigest())
print(op1.hexdigest())
print(op2.hexdigest())
print(op3.hexdigest())