import redis
import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))
HOST_NAME = env("HOST_NAME")
ACCESS_KEY = env("ACCESS_KEY")

r = redis.Redis(host=HOST_NAME,
    port=6380, db=0, password=ACCESS_KEY, ssl=True)

result = r.ping()
print("Ping returned : " + str(result))

# 文字列型データ
result = r.set("Message", "Hello!, The cache is working with Python!")
print("SET Message returned : " + str(result))

result = r.exists('Message')
print("Num of Message's Keys is :" + str(result))

result = r.keys()
print("List of Keys is :", result)

result = r.get("Message")
print("GET Message returned : " + result.decode("utf-8"))

result = r.client_list()
print("CLIENT LIST returned : ")
for c in result:
    print("id : " + c['id'] + ", addr : " + c['addr'])

# リスト
result = r.rpush('name', 'Tom') # 末尾に追加
print("RPush", result)

result = r.rpush('name', 'Alex', 'John')
print("RPush", result)

result = r.lpush('name', 'Taro') # 先頭に追加
print("LPush", result)

result = r.lpush('name', 'Tetuo', "Suzuki") # 先頭に追加
print("LPush", result)

result = r.lpop('name') # 先頭から値を取り出して削除
print("LPop", result)

result = r.rpop('name')  # 末尾から値を取り出して削除
print("RPop", result)

result = r.keys()
print("List of Keys is :", result)

result = r.lrange('name', 0, -1)
print("GET name returned : " , result)

result = r.delete('name') # name を削除
print("Delete", result)

result = r.keys()
print("List of Keys is :", result)
