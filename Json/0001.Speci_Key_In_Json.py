#递归搜索Json串中指定field的value值

json_str="""
{"A":"Tesdt","B":[{"C":"Hello","D":"World"}]}
"""

def get_recursively(field,search_tg):
    field_values=[]
    for k,v in search_tg.items():
        if field == k:
            return search_tg[k]
        if isinstance(v,dict):
            values= get_recursively(field,v)
            field_values.append(values)
        if isinstance(v,list):
            for sub_item in v:
                if isinstance(sub_item,dict):
                    more_values = get_recursively(field,sub_item)
                    field_values.append(more_values)
    return field_values

import json

json_tg = json.loads(json_str)
print(get_recursively("B",json_tg))






