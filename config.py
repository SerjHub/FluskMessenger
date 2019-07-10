import json

data = open("config.txt").read()
config = json.loads(data)
print(config['mysql_password'])
mysql_pass = config["mysql_password"]
