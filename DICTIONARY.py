# dictionary is basically a combination of a key and a value { key: value}
# dictionary is mutable
piyush_dict = {"piyush":17342, "amit" :16951}
print(piyush_dict["amit"])
print(piyush_dict["piyush"])
print(type(piyush_dict["amit"]))
dict = {"good": 123 , 123: "ammu"}
print(dict["good"])
print(dict[123])
dict["aman"] = 1488
print(dict)

# print(dict.get(1234))
# print(dict[1234])
print(dict.values())
print(dict.keys())
print(dict.items())