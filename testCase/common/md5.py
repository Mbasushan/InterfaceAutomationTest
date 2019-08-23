#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import hashlib

def my_md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    print(m.hexdigest())
    return m.hexdigest()