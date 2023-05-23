# -*- coding: utf-8 -*-
#------------------------------------------------------------
import datetime,time,sys,os,random,json,re,math


DEBUG_Flags={
  'init':True,
  'warning':True,
  'err':True,
  'info':True,
  'time':True,
  'single_box_debug':True,
  'g_timeflag':True, 
}

G_flags_debug={}


def deeper_str_now():
    return datetime.datetime.now().strftime('%H:%M:%S.%f')


def set_debug_flags(flags):
    for k in flags:
        if flags[k]==True:
            G_flags_debug[str(k).lower()]=1
    G_flags_debug['g_timeflag']=float(time.time())

def debug_msg(msg,flag='info',indent=0,indent_str='>'): 
    if flag.lower() in G_flags_debug:
        if flag.lower()=='time':
            delta_time=float(time.time())-G_flags_debug['g_timeflag']
            G_flags_debug['g_timeflag']=float(time.time())
            if len(msg.strip())==0:   
                s=''     
            else:
                indent_str='*'
                s='[%s]-[%s]-[%.2f]: %s %s' %(deeper_str_now(),flag.upper(),delta_time,indent_str*indent,msg)
        elif len(msg.strip())==0:
            s=''
        else:
            if flag.lower()=='err' or flag.lower()=='warning':
                indent_str='+'
            s='[%s]-[%s]: %s %s' %(deeper_str_now(),flag.upper(),indent_str*indent,msg)
        print(s)
    

set_debug_flags(DEBUG_Flags)
