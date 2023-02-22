import json


with open('sample-data.json') as f:
    data = json.load(f)


print("""Interface Status================================================================================""")
print("""DN                                               Description            MTU          Speed """)
print("------------------------------------------       --------------------  ------         ------")
for i, k in data["imdata"][0]['l1PhysIf']["attributes"].items():
    if i == 'dn':
        print(k, end="                              ")
    if i == "speed":
        print(k, end="               ")
    if i == "mtu":
        print(k, end="         ") 

