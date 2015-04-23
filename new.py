import urllib
import urllib.request
import json

zabbix_url = "http://192.168.1.218:81/zabbix/api_jsonrpc.php"
zabbix_header = {"Content-Type":"application/json"}
zabbix_user = "admin"
zabbix_pass = "zabbix"
auth_code = ""
auth_data = json.dumps(
    {
        "jsonrpc":"2.0",
        "method":"user.login",
        "params":
            {
                "user":zabbix_user,
                "password":zabbix_pass
            },
        "id":1
    }
)
auth_data = auth_data.encode("UTF-8")
request = urllib.request.Request(zabbix_url,auth_data)
request.add_header("Content-Type","application/json")
result = urllib.request.urlopen(request)
result = json.loads(result.readall().decode('utf-8'))
auth_token = result['result']
app_url = "http://192.168.1.218:3000/debug/vars"
data = urllib.request.urlopen(app_url)
data = data.readall().decode('UTF-8')
data = json.loads(data)
send_out = json.dumps({
    "data":[
    {
        "{#MEMNAME}":"\HeapAlloc",
        "{#MEMALLOC}":"1500"},
    {
        "{#MEMNAME}":"\HeapMem",
        "{#MEMALLOC}":"2000"},

   ]})


