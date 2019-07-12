# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

import re
import json
'''
<link type="text/css" rel="stylesheet" href="
<a href="
<script src="
'''
def findLinks(htmlString):
    resultlist = []
    #links = re.compile(r"target=\"_blank\" href =\"(.+?)\"")
    links = re.compile(r"<a href=\"(.+?)\"")
    Scriptlinks = re.compile(r"<script src=\"(.+?)\"")
    CSSlinks = re.compile(r"<link.*href=\"(.+?)\"")

    scripturls = Scriptlinks.findall(htmlString.decode("utf8"))
    cssurls =  CSSlinks.findall(htmlString.decode("utf8"))
    hrefurls =  links.findall(htmlString.decode("utf8"))

    resultlist.extend(scripturls)
    resultlist.extend(cssurls)
    resultlist.extend(hrefurls)

    resultlist = list(set(resultlist))
    tmp =[]
    for item in resultlist:
        item = item.strip().strip("/")
        if item.startswith("#"):
            continue
        tmp.append(item)
        print(item)

    return list(set(tmp))


def findLinks111(htmlString):
    resultlist = []
    #links = re.compile(r"target=\"_blank\" href =\"(.+?)\"")
    links = re.compile(r"\'(.+?)\'\: {")
    Scriptlinks = re.compile(r"resolve\, \'(.+?)\')\;")
    CSSlinks = re.compile(r"<link.*href=\"(.+?)\"")

    scripturls = Scriptlinks.findall(htmlString.decode("utf8"))
    cssurls =  CSSlinks.findall(htmlString.decode("utf8"))
    hrefurls =  links.findall(htmlString.decode("utf8"))

    resultlist.extend(scripturls)
    resultlist.extend(cssurls)
    resultlist.extend(hrefurls)

    resultlist = list(set(resultlist))
    tmp =[]
    for item in resultlist:
        item = item.strip().strip("/")
        if item.startswith("#"):
            continue
        tmp.append(item)
        print(item)

    return list(set(tmp))

def findJsonValue(string,keytofind):
    result = []
    jsondict = {}
    try:
        jsondict = json.loads(string)#解析出来的也不一定是json格式，也可能是字符串
    except Exception as e:
        print("not a json string")
        return

    if isinstance(jsondict, dict):
        for key in jsondict:
            value = jsondict[key]
            if key == keytofind:
                print(value)
                result.append(value)
            else:
                if isinstance(value, dict):
                    tmpresult = findJsonValue(json.dumps(value), keytofind)
                    result.extend(tmpresult)
                elif isinstance(value, list):
                    for listitem in value:
                        tmpresult = findJsonValue(json.dumps(listitem), keytofind)
                        result.extend(tmpresult)
                else:
                    pass
    else:
        pass
    return  result




if __name__ == "__main__":
    html = open("D:\user\01374214\Downloads\dom (3).html","r").read()
    result = findJsonValue(html,"reportUrl")
    for item in result:
        print("http://erpcampus.jd.com/"+item)