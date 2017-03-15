# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

from setting import access_key, secret_key, bucket_name

# access_key = 'Access_Key'
# secret_key = 'Secret_Key'

q = Auth(access_key, secret_key)

# bucket_name = 'Bucket_Name'

key = 'my-python-logo3.png';

#上传文件到七牛后， 七牛将文件名和文件大小回调给业务服务器。
policy={
    # 'callbackUrl':'http://139.129.24.151:5000/image/upload',
    'callbackUrl':'http://220.184.60.200:5000/qiniu/upload',
    # 'callbackUrl':'http://your.domain.com/callback.php',
    # 'callbackBody':'filename=$(fname)&filesize=$(fsize)'
    'callbackBody':'filename=$(key)&filesize=$(fsize)'
}
print('policy',policy)

token = q.upload_token(bucket_name, key, 3600, policy)

localfile = './sync/bbb.jpg'

ret, info = put_file(token, key, localfile)
print('ret',ret)
print('info', info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)

