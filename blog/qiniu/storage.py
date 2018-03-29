git#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.files.storage import FileSystemStorage
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
from django.conf import settings
class ImageStorage(FileSystemStorage):
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        super(ImageStorage, self).__init__(location, base_url)
    def _save(self, name, content):
        import os, time, random
        #文件扩展名
        ext = os.path.splitext(name)[1]
        d = os.path.dirname(name)
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0,100)
        name = os.path.join(d, fn + ext)
        localfile =  os.path.join(self.location,name)
        resultSave = super(ImageStorage, self)._save(name, content)
        self.put_qiniu(localfile,os.path.join(fn + ext))
        return resultSave


    def put_qiniu(self,localfile,filename):
        access_key  = settings.QINIU_ACCESS_KEY
        secret_key = settings.QINIU_SECRET_KEY
        bucket_name = settings.QINIU_BUCKET_NAME
        q = Auth(access_key, secret_key)
        key = filename
        token = q.upload_token(bucket_name, key, 3600)
        ret, info = put_file(token, key, localfile)
        print info
