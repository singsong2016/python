import re

def reg(str,pattern):
    s=re.search(pattern,str)
    p='>.*<'
    result=re.search(p,str[s.start():s.end()])
    return result.group()[1:-1]

#for instance
# str='<a href="www.baidu.com" class="data">hello</a><a href="www.baidu.com" class="data">hello</a>'
# pattern='class="data">.*?</a>'