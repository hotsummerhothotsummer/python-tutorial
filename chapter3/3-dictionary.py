dic = {"name": "rick", "age": 22}
print(dic["name"])
dic2 = {"name": "liam", "age":8, "car": "tesla"}
print(dic2)
print(dic2["car"])
dic2["name"] = '오홍균'
print(dic2)
dic2["car"] = 'ionic'
print(dic2)
print(dic2["car"])
del dic2["name"]
print(dic2)
print(dic2.keys())
print(dic2.values())
print(dic2.get(0,"없음"))
print("오홍균" in dic2)
