# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from importlib import import_module
import os, sys, json, logging, argparse

try:
    import ConfigParser
except:
    import configparser as ConfigParser
import socket, fcntl, struct
from gevent import pywsgi

sys.path.append('/s')
# sys.path.append('/s/api/m_meg_line_recognition')
sys.path.append('/s/api/m_db_detection')

cmd_list = []
# cmd_list.append('cp /s/api/m_mmdet/src/cascade_rcnn.py /opt/conda/lib/python3.7/site-packages/mmdet-1.2.0+0f33c08-py3.7-linux-x86_64.egg/mmdet/models/detectors/cascade_rcnn.py')
# cmd_list.append('cp /s/api/m_mmdet/src/resnet.py /opt/conda/lib/python3.7/site-packages/mmdet-1.2.0+0f33c08-py3.7-linux-x86_64.egg/mmdet/models/backbones/resnet.py')
# cmd_list.append('cp /s/api/m_mmdet/src/__init__.py /opt/conda/lib/python3.7/site-packages/mmdet-1.2.0+0f33c08-py3.7-linux-x86_64.egg/mmdet/ops/__init__.py')
# cmd_list.append('cp /s/api/m_mmdet/src/table_projection.py /opt/conda/lib/python3.7/site-packages/mmdet-1.2.0+0f33c08-py3.7-linux-x86_64.egg/mmdet/ops/table_projection.py')
# cmd_list.append('cp /s/api/update_src/inference.py /opt/conda/lib/python3.7/site-packages/mmdet-2.10.0-py3.7.egg/mmdet/apis/inference.py')
# for cmd in cmd_list:
#     os.popen(cmd)

import api.lib.convert_output as convert_output
from api.lib.lib_debug import debug_msg

# --flask的app初始化
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

# --日志全局
logger = logging.getLogger()
logger.setLevel(logging.WARNING)

# --特定API的全局列表，根据配置文件进行初始化
G_api_list = {}
G_instance_list = {}


@app.route('/onlyou/<api_name>', methods=['POST', 'GET'])
def onlyou(api_name):
    if True:
        # --获取对应api的类，并初始化该类的全家变量（传递instance）,然后调用api的处理函数
        t_api = G_api_list[api_name]
        return t_api.api_interface(request)
    # except:
    # print ("--->err to find api name %s \n" %(api_name))
    # response={'retcode':402,'ret{}':{}}
    # response=json.dumps(response)
    # return (response)


@app.route('/api/<api_name>', methods=['POST', 'GET'])
def api(api_name):
    if True:
        # --获取对应api的类，并初始化该类的全家变量（传递instance）,然后调用api的处理函数
        t_api = G_api_list[api_name]
        return convert_output.test_convert(api_name, t_api.api_interface(request))
    # except:
    # print ("--->err to find api name %s \n" %(api_name))
    # response={'retcode':402,'ret{}':{}}
    # response=json.dumps(response)
    # return (response)


# --根据配置文件初始化实例及API
def init_api_config(cf, args):
    def init_instance(sec_row, item_rows, args):
        info = {}

        # --basic_info是type,name,model_name
        info['basic_info'] = {}

        # --P_list是实例的输入参数
        info['P_list'] = {}
        info['P_list']['f_gpu_or_cpu'] = args.f_gpu_or_cpu
        info['P_list']['instance_list'] = {}
        info['P_list']['internel_host_ip'] = args.internel_host_ip
        info['P_list']['root_directory'] = args.root_directory

        # --根据配置文件初始化
        for ks in item_rows:
            if ks[0] in ['type', 'name', 'model_name']:
                info['basic_info'][ks[0]] = ks[1]
            elif ks[0][:len('instance_')] == 'instance_':
                if ks[1] in G_instance_list:
                    k = ks[0][len('instance_'):].lower()
                    info['P_list']['instance_list'][k] = G_instance_list[ks[1]]
            else:
                info['P_list'][ks[0]] = ks[1]

        # --assert
        assert (info['basic_info']['type'] == 'instance')

        # --调用类初始化
        debug_msg('', indent=2, flag='init')
        debug_msg('', indent=2, flag='init')
        debug_msg('Initing instance:%s' % (info['basic_info']['name']), indent=2, flag='init')

        s = import_module(info['basic_info']['model_name'] + '.p_main')
        t_model = s.p_main(**info['P_list'])
        G_instance_list[info['basic_info']['name']] = t_model
        debug_msg('P:%s' % (str(info['P_list'])), indent=4, flag='init')
        debug_msg('', indent=2, flag='init')

        return

    def init_api(sec_row, item_rows, args):
        info = {}

        # --basic_info是type,name,model_name
        info['basic_info'] = {}

        # --P_list是实例的输入参数
        # --instance_list是实例列表
        info['P_list'] = {}
        info['P_list']['instance_list'] = {}
        info['P_list']['api_list'] = {}
        info['P_list']['root_directory'] = args.root_directory

        # --根据配置文件初始化
        for ks in item_rows:
            if ks[0] in ['type', 'name']:
                info['basic_info'][ks[0]] = ks[1]
            elif ks[0][0:len('api_')] == 'api_':
                k = ks[0][len('api_'):].lower()
                info['P_list']['api_list'][k] = G_api_list[ks[1]]
            elif ks[0][0:len('instance_')] == 'instance_':
                k = ks[0][len('instance_'):].lower()
                info['P_list']['instance_list'][k] = G_instance_list[ks[1]]
            else:
                info['P_list'][ks[0]] = ks[1]

        # --assert
        assert (info['basic_info']['type'] == 'api')

        # --调用类初始化
        debug_msg('', indent=2, flag='init')
        debug_msg('Initing api:%s' % (info['basic_info']['name']), indent=2, flag='init')
        s = import_module('interface.' + info['basic_info']['name'])
        t_api = s.Interface_main(**info['P_list'])
        G_api_list[info['basic_info']['name']] = t_api
        debug_msg('P:%s' % (str(info['P_list'])), indent=4, flag='init')
        debug_msg('', indent=2, flag='init')

        return

    for sec_row in cf.sections():
        # --先初始化实例instance
        for ks in cf.items(sec_row):
            if ks[0] == 'type' and ks[1] == 'instance':
                init_instance(sec_row, cf.items(sec_row), args)

    for sec_row in cf.sections():
        # -再初始化接口
        for ks in cf.items(sec_row):
            if ks[0] == 'type' and ks[1] == 'api':
                init_api(sec_row, cf.items(sec_row), args)

    return


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        a = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24]
    except:
        a = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15], 'utf-8')))[20:24]
    return socket.inet_ntoa(a)


def start_app():
    # --read config
    parser = argparse.ArgumentParser(description='API Main...')
    parser.add_argument('--root_directory', default='/s/api/')
    parser.add_argument('--f_gpu_or_cpu', default='GPU0')
    parser.add_argument('--config_file')
    parser.add_argument('--internel_host_ip', default='10.10.10.1')
    parser.add_argument('--port', default='8000')
    args = parser.parse_args()
    logging.info(args)

    debug_msg('', indent=2, flag='init')
    debug_msg('', indent=2, flag='init')
    debug_msg('', indent=2, flag='init')
    os.environ['PYTHONUNBUFFERED'] = '1'

    cf = ConfigParser.ConfigParser()
    cf.read(args.config_file)
    port = int(args.port)
    ver = 'SAE Ver20220615-RC1'
    debug_msg('Starting API Service(%s)-->%s:%s' % (ver, str(get_ip_address('eth0')), str(port)), indent=4, flag='init')

    # --初始化全局参数
    init_api_config(cf, args)

    # --start listen api request
    signal = True
    debug_msg('', indent=2, flag='init')
    debug_msg('', indent=2, flag='init')
    debug_msg('', indent=2, flag='init')
    debug_msg('OK to start API Service(%s)-->%s:%s' % (ver, str(get_ip_address('eth0')), str(port)), indent=4,
              flag='init')
    app.run(host='0.0.0.0', port=port, threaded=False, processes=1)
    # server = pywsgi.WSGIServer(('0.0.0.0', port), app)
    # server.serve_forever()


# --main函数入口
if __name__ == '__main__':
    start_app()
