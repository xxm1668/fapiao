# -*- coding: utf-8 -*-
import json

G_name_other='NA'

G_map_dict={
  'kjdz0001':
      {
        'name':'fp_zzs',
        'items_map':
          {
            'PayingCorp':'buyer',
            'PayingTaxCode':'buyer_taxid',
            'DrawingCorp':'seller',
            'DrawingTaxCode':'seller_taxid',
            'SealDrawingTaxCode':'seal_seller_taxid',
            'SealText':'seal_seller',
            'IssueDate':'date',
            'TotalTax':'total_tax',
            'SubTotalAmount':'total_money_without_tax',
            'TotalAmount':'total_money',
            'TotalAmountCap':'total_money_cn',
            'InvoiceCode':'fp_code',
            'InvoiceCode2':'fp_code2',
            'InvoiceNO':'fp_id',
            'InvoiceNO2':'fp_id2',
            'ItemTaxRate':'fp_mx_taxrate',
            'ItemContent':'fp_mx_content',
            'ItemAmount':'fp_mx_amount',
            'ItemTaxAmount':'fp_mx_tax',
            'Summary':'summary',
            'VCode': 'verify_code',
            'Sheet': 'fp_lianci',
            'YesNo2': 'fp_have_seal',
            'BillTitle': 'fa_title',
          },
      },

  'zengzhishuijuan':
      {
        'name':'fp_zzsjp',
        'items_map':
          {
            'PayingCorp':'buyer',
            'PayingTaxCode':'buyer_taxid',
            'DrawingCorp':'seller',
            'DrawingTaxCode':'seller_taxid',
            'SealDrawingTaxCode':'seal_seller_taxid',
            'SealText':'seal_seller',
            'IssueDate':'date',
            'TotalTax':'total_tax',
            'SubTotalAmount':'total_money_without_tax',
            'TotalAmount':'total_money',
            'TotalAmountCap':'total_money_cn',
            'InvoiceCode':'fp_code',
            'InvoiceNO':'fp_id',
            'VCode': 'verify_code',
            'YesNo2': 'fp_have_seal',
            'Sheet': 'fp_lianci',
            'BillTitle': 'fa_title',
          },
      },

  'ershouche':
      {
        'name':'fp_zzsesc',
        'items_map':
          {
            'BillTitle': 'fa_title',
            'PayingCorp':'buyer',
            'PayingTaxCode':'buyer_taxid',
            'DrawingCorp':'seller',
            'DrawingTaxCode':'seller_taxid',
            'IssueDate':'date',
            'TotalAmount':'total_money',
            'TotalAmountCap':'total_money_cn',
            'InvoiceCode':'fp_code',
            'InvoiceNO':'fp_id',
            'VIN':'fp_vin',
            'Sheet': 'fp_lianci',
            'VCode': 'verify_code',
          },
      },


  'jidongche':
      {
        'name':'fp_zzsjdc',
        'items_map':
          {
            'BillTitle': 'fa_title',
            'PayingCorp':'buyer',
            'PayingTaxCode':'buyer_taxid',
            'PayingOragCode':'buyer_id',
            'DrawingCorp':'seller',
            'DrawingTaxCode':'seller_taxid',
            'IssueDate':'date',
            'TotalAmount':'total_money',
            'TotalAmountCap':'total_money_cn',
            'InvoiceCode':'fp_code',
            'InvoiceNO':'fp_id',
            'VIN':'fp_vin',
            'EngineNO':'fp_engine',
            'LabelNO':'fp_company',
            'VCode': 'verify_code',
            'Sheet': 'fp_lianci',
            'QualifiedNO':'hegezheng_id',
          },
      },

  'kjdz0003':
      {
        'name':'fp_fjp',
        'items_map':
          {
            'IDNo':'fp_idno',
            'SeatClass':'seat_class',
            'ItemSeatClass':'seat_class',
            'Carrier':'fp_carrier',
            'InvoiceCode':'fp_code',
            'ElectronicTicketNO':'fp_ticketno',
            'ItemTrainNO':'fp_trainno',
            'PayingCorp':'buyer',
            'IssueDate':'date',
            'CaacDevFund':'money_mhfzjj',
            'FuelSurcharge':'money_fuel',
            'Amount':'money',
            'TotalAmount':'total_money',
            'ItemOrigin':'from',
            'ItemDest':'to',
            'Origin':'from',
            'Dest':'to',
            'ItemIssueDate':'date',
            'InsurancePremium':'insurance',
          },  
      },

  'qichepiao':
      {
        'name':'fp_qcp',
        'items_map':
          {
            'SeatClass':'seat_class',
            'InvoiceCode':'fp_code',
            'TicketNO':'fp_ticketno',
            'TrainNO':'fp_trainno',
            'PayingCorp':'buyer',
            'IssueDate':'date',
            'TotalAmount':'total_money',
            'Origin':'from',
            'Dest':'to',
          },  
      },


  'kjdz0004':
      {
        'name':'fp_dinge',
        'items_map':
          {
            'IssueDate':'date',
            'TotalAmountCap':'total_money_cn',
            'TotalAmount':'total_money',
            'InvoiceCode':'fp_code',
            'InvoiceNO':'fp_id',
            'YesNo2': 'fp_have_seal',
          },
      },

  'kjdz0005':
      {
        'name':'fp_czc',
        'items_map':
          {
            'IssueDate':'date',
            'InvoiceCode':'fp_code',
            'InvoiceNO':'fp_id',
            'TotalAmount':'total_money',
            'CarNumber': 'car_license',
            'BoardingTime': 'time_start',
            'AlightingTime': 'time_end',
          },
      },

  'kjdz0006':
      {
        'name':'fp_hcp',
        'items_map':
          {
            'SeatClass':'seat_class',
            'InvoiceCode':'fp_code',
            'TicketNO':'fp_no',
            'TrainNO':'fp_trainno',
            'IDNo':'fp_idno',
            'PayingCorp':'buyer',
            'IssueDate':'date',
            'TotalAmount':'total_money',
            'Origin':'from',
            'Dest':'to',
          },  
      },


  'gaosupiao':
      {
        'name':'fp_gsglf',
        'items_map':
          {
            'IssueDate':'date',
            'Entrance':'from',
            'Exit':'to',
            'TotalAmount':'total_money',
            'TotalAmountCap':'total_money_cn',
            'InvoiceCode':'fp_code',
            'InvoiceNO':'fp_id',
          },  
      },


  'shenfenzheng':
      {
        'name':'id_sfz',
        'items_map':
          {
            'Name':'id_name',
            'National':'id_national',
            'ADD':'id_address',
            'Sex':'id_sex',
            'DateOfBirth':'id_birth',
            'IDNo':'id_no',
            'ValidTerm': 'id_valid_date',
            'IssuingAuthority': 'id_issue',
          },
      },

  'yingyezhizhao':
      {
        'name':'id_yyzz',
        'items_map':
          {
            'EstablishDate':'id_date',
            'Capital':'id_capital',
            'Address':'id_address',
            'CreditCode':'id_no',
            'LegalPerson':'id_frdb',
            'Name': 'id_name',
            'Type': 'id_type',
          },
      },

  'yinhangka':
      {
        'name':'bank_card',
        'items_map':
          {
            'BankCard':'id_cardno',
          },  
      },

  'kjdz0002':
      {
        'name':'bank_huidan',
        'items_map':
          {
            'Currency':'money_type',
            'LoanMark':'jiedai_type',
            'IssueDate':'date',
            'TotalAmount':'total_money',
            'TotalAmountCap':'total_money_cn',
            'ReceiverOrgan':'to_name',
            'ReceiverAccountName':'to_account_name',
            'ReceiverAccountNumber':'to_account_no',
            'PayerOrgan':'from_name',
            'PayerAccountName':'from_account_name',
            'PayerAccountNumber':'from_account_no',
          },  
      },

  'yunshuxukezheng':
      {
        'name':'id_ysxkz',
        'items_map':
          {
            'yehumingcheng':'yehumingcheng',
            'chelianghaopai':'chelianghaopai',
            'cheliangleixing':'cheliangleixing',
            'jingyingxukezhenghao':'jingyingxukezhenghao',
          },  
      },

  'xingshizheng':
      {
        'name':'id_xsz',
        'items_map':
          {
            'haopaihaoma':'haopaihaoma',
            'suoyouren':'suoyouren',
            'pinpaixinghao':'pinpaixinghao',
            'cheliangleixing':'cheliangleixing',
          },  
      },

  'jiashizheng':
      {
        'name':'id_jsz',
        'items_map':
          {
            'xingming':'xingming',
            'zhenghao':'zhenghao',
            'zhunjiachexing':'zhunjiachexing',
            'youxiaoqizhi':'youxiaoqizhi',
          },  
      },

    'bankline':
        {
            'name': 'bank_line',
            'items_map':
                {
                    'bno': 'no',
                    'bdate': 'date',
                    'bmoney': 'money',
                    'bname': 'name',
                    'bno_hw': 'no_hw',
                    'bdate_hw': 'date_hw',
                    'bmoney_hw': 'money_hw',
                    'bname_hw': 'name_hw',
                },
        },

    'XZSYDWSJ':
        {
            'name': 'fp_xzsj',
            'items_map':
                {
                },
        },

    'YLPJ':
        {
            'name': 'fp_hospital',
            'items_map':
                {
                    'Payer': 'buyer',
                    'IssueDate': 'date',
                    'TotalAmount': 'total_money',
                    'TotalAmountCap': 'total_money_cn',
                    'IssueDateSX': 'date',
                    'TotalAmountSX': 'total_money',
                    'TotalAmountCapSX': 'total_money_cn',
                    'InvoiceCode': 'fp_code',
                    'InvoiceNO': 'fp_id',
                },
        },

    'wuhan_hospital_mz':
        {
            'name': 'med_wh_mz',
            'items_map':
                {
                    'Name': 'name',
                    'Hospital': 'hospital_name',
                    'TotalAmountDigit': 'total_money',
                    'TotalAmountCap': 'total_money_cn',
                    'ArriveDate': 'date',
                    'InvoiceNo': 'fp_no',
                    'MedicarePay': 'money_med_pay',
                    'SelfExpense': 'money_self_expense',
                    'CashPay': 'money_case_pay',
                },
        },
    'FaPiao'.lower():
        {
            'name': 'haiguan_fapiao',
            'items_map':
                {
                },
        },
    'HeTong'.lower():
        {
            'name': 'haiguan_hetong',
            'items_map':
                {
                },
        },
    'TiYunDan'.lower():
        {
            'name': 'haiguan_tiyundan',
            'items_map':
                {
                },
        },
    'ZhuangXiangDan'.lower():
        {
            'name': 'haiguan_zhuangxiangdan',
            'items_map':
                {
                },
        },
    'YuanChanDi'.lower():
        {
            'name': 'haiguan_yuanchandi',
            'items_map':
                {
                },
        },
    'YuanChanDi_ZhongRui'.lower():
        {
            'name': 'haiguan_yuanchandi_zhongrui',
            'items_map':
                {
                },
        },
    'NO'.lower():
        {
            'name': 'haiguan_yuanchandi_zhongrui_no',
            'items_map':
                {
                },
        },
    'T1'.lower():
        {
            'name': 'haiguan_yuanchandi_zhongrui_t1',
            'items_map':
                {
                },
        },
    'R1'.lower():
        {
            'name': 'haiguan_yuanchandi_zhongrui_r1',
            'items_map':
                {
                },
        },
    'zhang'.lower():
        {
            'name': 'haiguan_yuanchandi_zhongrui_zhang',
            'items_map':
                {
                },
        },
    'qs_check_demo'.lower():
        {
            'name': 'quanshang_check_demo',
            'items_map':
                {
                    'qianming01': 'qianming01',
                    'qianming02': 'qianming02',
                    'qianming03': 'qianming03',
                    'r1_1': 'r1_1',
                    'r1_2': 'r1_2',
                    'r1_3': 'r1_3',
                    'r1_4': 'r1_4',
                    'r1_5': 'r1_5',
                    'x1_1': 'x1_1',
                    'x1_2': 'x1_2',
                    'x2_1': 'x2_1',
                    'x2_2': 'x2_2',
                    'x3_1': 'x3_1',
                    'x3_2': 'x3_2',
                    'x4_1': 'x4_1',
                    'x4_2': 'x4_2',
                    'x5_1': 'x5_1',
                    'x5_2': 'x5_2',
                },
        },
}

def convert_docu(r):
    new_r={}
    
    #--类别
    try:
        new_r['DocType'] = G_map_dict[r['recepit_category_type']]['name'].lower()
    except:
        new_r['DocType'] = G_name_other
    
    #--全文本识别结果
    new_r['FreeTexts']=[]
    for fr in r['freestyle_recog_content']:
        fr_row={}
        fr_row['Text'] = fr['text']
        fr_row['Position'] = fr['bbox']
        fr_row['Metric'] = fr['scores']
        new_r['FreeTexts'].append(fr_row)
        
    #--结构化识别结果
    new_r['StructTexts']=[]

    s_row_dict={
        'fp_code':None,
        'fp_id': None,
        'fp_code2': None,
        'fp_id2': None,
    }

    if int(r['judge_good_or_not']) ==200 and len(r['content'])>=1:
        for fr in r['content']:
            try :
                fr_row={}
                fr_row['ItemText'] = fr['text']
                fr_row['ItemMetric'] = fr['scores']
                fr_row['ItemPosition'] = fr['locations']
                if len(G_map_dict[r['recepit_category_type']]['items_map'])>0:
                    fr_row['ItemName'] = G_map_dict[r['recepit_category_type']]['items_map'][fr['text_category']]
                else:
                    fr_row['ItemName'] = fr['text_category']
                new_r['StructTexts'].append(fr_row)
                if fr_row['ItemName'] in s_row_dict:
                    s_row_dict[fr_row['ItemName']] = fp_row
            except Exception:
                pass

    if s_row_dict['fp_code2'] is not None and s_row_dict['fp_code'] is None:
        s_row_dict['fp_code2']['ItemName'] = 'fp_code'

    if s_row_dict['fp_id2'] is not None and s_row_dict['fp_id'] is None:
        s_row_dict['fp_id2']['ItemName'] = 'fp_id'


    #--位置
    new_r['Locations']=r['locations']
    new_r['RotateAngel']=r['rotate_detail_angel']
    
    return new_r




def convert_pdf_table(r):
    new_r = {}

    # --类别
    try:
        new_r['DocType'] = G_map_dict[r['recepit_category_type']]['name'].lower()
    except:
        new_r['DocType'] = 'Table'

    # --结构化识别结果
    new_r['TableTexts'] = []
    if len(r['content']) >= 1:
        for fr in r['content']:
            try:
                fr_row = {}
                fr_row['ItemText'] = fr['text']
                fr_row['ItemMetric'] = fr['scores']
                fr_row['ItemRowIDX'] = fr['row_idx']
                fr_row['ItemColDX'] = fr['col_idx']
                fr_row['ItemRowIDXEnd'] = fr['row_idx_end']
                fr_row['ItemColDXEnd'] = fr['col_idx_end']
                new_r['TableTexts'].append(fr_row)
            except Exception:
                pass

    new_r['FreeTexts']=[]
    if 'freestyle_recog_content' in r:
        for fr in r['freestyle_recog_content']:
            fr_row={}
            fr_row['Text'] = fr['text']
            fr_row['Position'] = fr['bbox']
            fr_row['Metric'] = fr['scores']
            fr_row['RowIdx'] = fr['row_idx']
            new_r['FreeTexts'].append(fr_row)


    # --位置
    new_r['PageNumber'] = r['page_number']
    new_r['PageNumberEnd'] = r['page_number_end']
    new_r['TableName'] = r['table_name']

    return new_r


def convert_table(r):
    new_r={}

    #--类别
    try:
        new_r['DocType'] = G_map_dict[r['recepit_category_type']]['name'].lower()
    except:
        new_r['DocType'] = 'Table'
    
    #--结构化识别结果
    new_r['TableTexts']=[]
    if len(r['content'])>=1:
        for fr in r['content']:
            try :
                fr_row={}
                fr_row['ItemText'] = fr['text']
                fr_row['ItemPosition'] = fr['locations']
                fr_row['ItemMetric'] = fr['scores']
                fr_row['ItemRowIDX'] = fr['row_idx']
                fr_row['ItemColDX'] = fr['col_idx']
                new_r['TableTexts'].append(fr_row)
            except Exception:
                pass
    new_r['FreeTexts']=[]
    for fr in r['freestyle_recog_content']:
        fr_row={}
        fr_row['Text'] = fr['text']
        fr_row['Position'] = fr['bbox']
        fr_row['Metric'] = fr['scores']
        fr_row['RowIdx'] = fr['row_idx']
        new_r['FreeTexts'].append(fr_row)
    
    #--位置
    new_r['Locations']=r['locations']
    new_r['RotateAngel']=int(r['rotate_detail_angel'])

    return new_r


def convert_chepai(r):
    new_r = {'chepai':[]}


    # --结构化识别结果
    if len(r['content']) >= 1:
        for fr in r['content']:
            try:
                fr_row = {}
                fr_row['ItemText'] = fr['text']
                fr_row['ItemPosition'] = fr['locations']
                fr_row['ItemMetric'] = fr['scores']
                fr_row['ItemLocationMetric'] = fr['locations_scores']
                new_r['chepai'].append(fr_row)
            except Exception:
                pass

    return new_r


def convert_haiguan(r):
    new_r = {}

    # --类别
    try:
        new_r['DocType'] = G_map_dict[r['recepit_category_type'].lower()]['name'].lower()
    except:
        new_r['DocType'] = G_name_other

    # --全文本识别结果
    new_r['FreeTexts'] = []

    # --结构化识别结果
    new_r['StructTexts'] = []

    # --位置
    new_r['Locations'] = r['locations']
    new_r['RotateAngel'] = int(r['rotate_detail_angel'])

    return new_r


def convert_general(r, only_freestyle=False):
    new_r = {}
    name_map_dict={
        'kjdz0001': 'fp_zzs',
        'jidongche': 'fp_jdc',
        'ershouche': 'fp_esc',
        'xhqd': 'fp_xhqd',
        'XZSYDWSJ'.lower(): 'fa_xzsj',
        'kjdz0003': 'fa_fjp',
        'kjdz0004': 'fp_de',
        'kjdz0006': 'fp_hcp',
        'gaosupiao': 'fp_gsp',
        'qichepiao': 'fp_qcp',
        'zengzhishuijuan': 'fp_juan',
        'kjdz0005': 'fp_czc',
    }

    if only_freestyle==True:
        new_r['DocType'] = 'NA'
        new_r['FreeTexts'] = []
        for fr in r['freestyle_recog_content']:
            fr_row = {}
            fr_row['Text'] = fr['text']
            fr_row['Position'] = fr['bbox']
            fr_row['Metric'] = fr['scores']
            fr_row['RowIdx'] = fr['row_idx']
            new_r['FreeTexts'].append(fr_row)


    else:
        # --类别
        try:
            new_r['DocType'] = name_map_dict[r['recepit_category_type'].lower()].lower()
        except:
            new_r['DocType'] = r['recepit_category_type']


        # --全文本识别结果
        if new_r['DocType'][:2] !='fp':
            new_r['FreeTexts'] = []
            for fr in r['freestyle_recog_content']:
                fr_row = {}
                fr_row['Text'] = fr['text']
                fr_row['Position'] = fr['bbox']
                fr_row['Metric'] = fr['scores']
                fr_row['RowIdx'] = fr['row_idx']
                new_r['FreeTexts'].append(fr_row)

        # --结构化识别结果
        new_r['StructTexts'] = []

        if int(r['judge_good_or_not']) == 200 and len(r['content']) >= 1:
            for fr in r['content']:
                try:
                    fr_row = {}
                    fr_row['ItemText'] = fr['text']
                    fr_row['ItemMetric'] = fr['scores']
                    fr_row['ItemPosition'] = fr['locations']
                    fr_row['ItemName'] = fr['text_category']
                    new_r['StructTexts'].append(fr_row)
                except Exception:
                    pass

    # --位置
    new_r['Locations'] = r['locations']
    new_r['RotateAngel'] = int(r['rotate_detail_angel'])

    return new_r


def test_convert(api_name,s):
    res = json.loads(s)
    
    new_res={}
    #--结果代码
    new_res['ResultCode'] = res['retcode']
    new_res['Results'] = []
    
    for r in res['ret{}']:
        if api_name=='test_recog_docu' or api_name=='test_detect_docu' or api_name=='test_recog_docu_without_detect' or api_name=='m_recog_bankline':
            new_r=convert_docu(r)
        elif api_name=='test_recog_table':
            new_r=convert_table(r)
        elif api_name=='test_recog_pdf_table' or api_name == 'tables_detection_and_recognition':
            new_r=convert_pdf_table(r)
        elif api_name == 'test_demo_haiguan':
            new_r = convert_haiguan(r)
        elif api_name == 'm_recog_chepai':
            new_r = convert_chepai(r)
        elif api_name == 'm_freestyle_recognition':
            new_r = convert_general(r, only_freestyle=True)
        else:
            new_r = convert_general(r)
        new_res['Results'].append(new_r)
    
    response=json.dumps(new_res)  
    return response