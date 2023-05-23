# -*- coding: utf-8 -*-
#------------------------------------------------------------
import datetime,time,sys,os,random,json,re
try:
    import ConfigParser
except:
    import configparser as ConfigParser
from importlib import import_module, reload

        
def read_lipiao_conf(args):
    lipiao_conf_var={}
    try:
       cf = ConfigParser.ConfigParser()
       cf.read(args['root_directory']+args['lipiao_conf'])    
       for sec_row in cf.sections():
           lipiao_conf_var[sec_row.strip()]={}
           new_v=lipiao_conf_var[sec_row.strip()]
           for ks in cf.items(sec_row):
               new_v[ks[0].lower()]=ks[1]
               
    except:
        pass     
        
    return lipiao_conf_var    


def read_py_config(item,args):
    if True:
        sys.path.append(args['root_directory'])
        s = import_module(args['py_conf']) 
        
        return eval('s.'+item)

def read_customer_config(items,args):
    if True:
        conf_list_in_customer_conf = {}
        sys.path.append(args['root_directory'])
        
        if 'customer_conf' not in args:
            return {}
        customer_dir = args['customer_conf'].replace('.','/')
        customer_dir = os.path.join(args['root_directory'],customer_dir)
        files = os.listdir(customer_dir)
        for each in files:
            res = os.path.splitext(each)
            if res[1]=='.py':
                if res[0]=='__init__':
                    continue
                conf_list_in_customer_conf[res[0]] = {}
                s = import_module(args['customer_conf']+'.'+res[0]) 
                # 在线更新配置文件，需要reload，否则还是原来的
                s = reload(s) 
                for key in items:
                    try:
                        conf_list_in_customer_conf[res[0]][key] = eval('s.'+key)
                    except:
                        pass
        return conf_list_in_customer_conf