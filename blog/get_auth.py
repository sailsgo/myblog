#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------
# Filename:    get_auth.py
# Revision:    1.0
# CreateDate:  2017/6/23
# Author:      mingjianyong
# Email        mingjianyong@aspirecn.com
# Description: 
# ------------------------------------------------------------
# Version 1.0
# ------------------------------------------------------------


from qiniu import auth
au = auth.Auth("eo8KrWCHq3gJe53OhK1Zv33iHF_FVYDe6TymSCyZ","LhJAkfoEJcbd7-m7m5lMliTO1gg7aCFIA5eTmBmg")
print au.upload_token("images")
