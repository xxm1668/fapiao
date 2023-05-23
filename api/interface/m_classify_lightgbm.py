# -*- coding: utf-8 -*-
import json
from api.lib.lib_debug import debug_msg
import urllib
import logging

class Interface_main(object):
    def __init__(self, instance_list=None, api_list=None, **args):
        self.f_list = instance_list
        self.api_list = api_list
        self.args = args

        self.p_interface = [
            {
                'name': 'text',
                'var_name': 'text',
                'default': '',
                'type': '',
            }
        ]

        return

    def api_interface(self, request):
        response = {}

        if request.method == 'POST':
            if True:
                p_args = {}

                for r in self.p_interface:
                    try:
                        p_args[r['var_name']] = request.form.get(r['name'])
                        if type(r['type']) == type(''):
                            assert (p_args[r['var_name']] != None)
                        p_args[r['var_name']] = type(r['type'])(p_args[r['var_name']])
                    except:
                        p_args[r['var_name']] = r['default']
                response = self.api_entry(**p_args)

                response = json.dumps(response)
                return (response)

            # except Exception:
            # print ("--->Err to docs_detection_and_recognition")
            # response={'retcode':501,'ret{}':[]}
            # response=json.dumps(response)
            # return (response)

        else:
            print("only support post method \n")
            response = {'retcode': 503, 'ret{}': []}
            response = json.dumps(response)
            return (response)

    def api_entry(self, **p_args):
        # --设置缺省值（因为api_entry可能会被其它API调用）
        for r in self.p_interface:
            if r['var_name'] not in p_args:
                p_args[r['var_name']] = r['default']

        for k in self.args:
            p_args[k] = self.args[k]

        p_args['f_list'] = self.f_list
        p_args['api_list'] = self.api_list

        P_classify = p_args['f_list']['classify_three']

        res = self.run_one(P_classify, p_args)
        # response = {'retcode': 200, 'ret{}': res}
        return res

    def run_one(self, P_classify, p_args):
        # res = []
        # print("p_args:{0}".format(p_args))
        # res_dict = P_classify.predict(p_args)
        # print("res_dict:{0}".format(res_dict))
        # res_main = res_dict['res']
        # res = res_main
        res = P_classify.predict(p_args)
        return res
