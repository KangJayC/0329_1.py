import json
urls={'mary':'13612345678',"rose": "13588888888","jack":"13512312345"}
with open(r'F:\Experimental Workstation\PyCharm Workstation\class_test\sy8\addressbook.json','w') as f:
 json.dump(urls,f)
