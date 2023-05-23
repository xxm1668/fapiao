# -*- coding: utf-8 -*-
import json,cv2,time,tempfile,urllib.request,random
import numpy as np
import api.lib.lib_img as lib_img
import api.lib.lib_pdf as lib_pdf


def build_args(request,p_interface):
    p_args = {}

    # --读取输入参数，没有的话要设置缺省值
    for r in p_interface:
        try:
            p_args[r['var_name']] = request.form.get(r['name'])
            if type(r['type']) == type(''):
                assert (p_args[r['var_name']] != None)
            p_args[r['var_name']] = type(r['type'])(p_args[r['var_name']])
        except:
            p_args[r['var_name']] = r['default']

    # --获取输入文件，可能是pdf（包括多个文件），也可能是单个图像
    p_args['docs'] = parse_docs_from_request(request)

    return p_args

def get_random_id():
    s=str(time.time())+'_'+str(random.randint(1,10000))
    s=s.replace('.','_')
    return s

def get_image_path(request,url_name,file_name):
    try:
        img_url = request.form.get(url_name)
        input_tempfile = tempfile.NamedTemporaryFile(delete=True)
        urllib.request.urlretrieve(img_url, input_tempfile.name)
    except:
        input_tempfile = request.files[file_name]

    return input_tempfile

def parse_docs_from_request(request,u='img_url',f='imagefile'):
    res = {}

    r_input = get_image_path(request,u,f)
    try:
        #--检测是否图像文件
        img = lib_img.read_img(r_input)
        res['input_file_type'] = 'f_img'
        res['f_img'] = img
        res['input_file'] = r_input
        res['msg'] = '[FileType:img] [Size:%s]' %(str(img.size))
    except:
        try:
            #--读取pdf文件
            pdf_raw = lib_pdf.read_pdf(r_input.name)
            res['input_file_type'] = 'f_pdf'
            res['f_pdf'] = pdf_raw
            res['input_file'] = r_input
            res['msg'] = '[FileType:pdf] [Pages:%s]' % (str(len(res['f_pdf'].pages)))
        except:
            try:
                new_tempfile = tempfile.NamedTemporaryFile(delete=True)
                r_input.seek(0)
                new_tempfile.write(r_input.read())
                new_tempfile.seek(0)
                pdf_raw = lib_pdf.read_pdf(new_tempfile.name)
                res['input_file_type'] = 'f_pdf'
                res['f_pdf'] = pdf_raw
                res['input_file'] = new_tempfile
                res['msg'] = '[FileType:pdf] [Pages:%s]' % (str(len(res['f_pdf'].pages)))
            except:
                res['input_file_type'] = 'err'
                res['msg'] = '[FileType:Err]'

    return res



