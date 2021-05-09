import hashlib, secrets
import pandas as pd

filename = 'data/Models/User.xlsx'
df = pd.read_excel(filename)

user = df['user'].tolist()
password = df['password'].tolist()

username = "admin"
test = "123456456"

flagLogin = 0

for u, p in zip(user, password):
    # print(a, "->", k)
    if username == u and hashlib.sha256(test.encode('utf-8')).hexdigest() == p:
        flagLogin = 1

if flagLogin == 1:
    print("Login Success")
    flagLogin = 0
else:
    print("Login Fail")

# print(secrets.compare_digest(hashlib.sha256(b"123456").hexdigest(), '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92')) #True
