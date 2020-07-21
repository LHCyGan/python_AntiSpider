import requests
import json

# Splash接口，编译lua脚本
render = ""

# 需要执行的命令
script = """
function main(splash, args)
    assert (splash:go(args.url))
    assert (splash:wait(0.2))
    -- 聚焦搜索框
    splash:select('input[name=q]'):foucs()
    -- 在搜索框中输入Python
    splash:send_text('Python')
    assert (splash:wait(0.2))
    return {
        png = splash:png()
    }
"""
# 设置请求头
headers = {'content-type': "application/json"}
# 按照splash规定提交命令
data = json.dumps({"lua_source": script})
# 向splash接口发出请求
resp = requests.post(render, headers=headers, data=data)

print(resp.json())