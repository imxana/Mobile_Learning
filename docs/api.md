## 目录

* [接口测试 ./test/api](#接口测试-testapi)
* [登录 ./signin](#登录-signin)
* [注册 ./signup](#注册-signup)
* [上传资源(七牛回调) ./qiniu/upload](#上传资源七牛回调-qiniuupload)

## 接口测试 ./test/api

methods: GET, POST

return html|str 


## 登录 ./signin

methods: POST

参数名|格式|例子
--------|--------|-------
username|str|'guest'
password|str|'456'

return

参数名|格式|例子
--------|--------|-------
code|int|0
error|str|'Invalid username'


## 注册 ./signup

methods: POST

参数名|格式|例子
--------|--------|-------
username|str|'guest'
password|str|'456'
email|str|'guest@example.com'

return

参数名|格式|例子
--------|--------|-------
code|int|0
error|str|'Invalid username'


## 上传资源(七牛回调) ./qiniu/upload

method: POST

参数名|格式|例子
--------|--------|-------
filename|str|'my-python-logo.png'

return

参数名|格式|例子
--------|--------|-------
code|int|1
url|str|'http://oi28ylyec.bkt.clouddn.com/my-python-logo.png'


