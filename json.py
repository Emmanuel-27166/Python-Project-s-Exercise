import json

x = '{"name" : "John", "age" : "30", "city" : "Freetown"}'


y = json.loads(x)

print(y["age"])