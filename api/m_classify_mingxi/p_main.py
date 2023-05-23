import os
import json
import base64

import importlib, sys
import traceback

importlib.reload(sys)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from model.classify_mingxi.predict import predict


class p_main(object):
    """
    """

    def __init__(self, **args):
        def get_default_args(**s):
            return s

        p_args = get_default_args(
            root_directory='./'
        )
        p_args.update(args)
        print(p_args)

    def predict(self, params):
        output = {}
        text = str(params["text"].encode(), encoding='utf-8')
        try:
            # 变量初始化
            label = predict(text)
            output['text'] = text
            output['label'] = label
            output['message'] = '成功运行'
            output['code'] = 200

        except Exception as e:
            print(e)
            print(sys.exc_info())
            print(traceback.format_exc())
            output['text'] = text
            output['label'] = ''
            output['message'] = '成功出错'
            output['code'] = 201

        finally:
            print(output)
            output = json.dumps(output, ensure_ascii=False, indent=1)  # 防止中文报错
            return base64.b64encode(output.encode("UTF-8")).decode("utf-8")


if __name__ == '__main__':
    pass
