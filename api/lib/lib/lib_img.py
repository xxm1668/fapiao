# -*- coding: utf-8 -*-
#------------------------------------------------------------
from __future__ import print_function
import datetime,time,sys,os,random,json,re,io
import cv2,imutils
import numpy as np
from PIL import Image,ImageDraw,ImageFont
from PIL.ExifTags import TAGS
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

try:
    #--该文件会在其他环境用
    import cv2
except:
    pass

def deeper_str_now():
    this_now=datetime.datetime.now()
    return str(datetime.time(this_now.hour,this_now.minute,this_now.second))

def deeper_debug(msg,*arg):
    print ("[%s]-%s" %(deeper_str_now(),msg),end='')
    for c in arg:
        print (c,end='')
    print    

def img_from_cv_to_pil(cv_np_img):
    pil_img=Image.fromarray(cv2.cvtColor(cv_np_img,cv2.COLOR_BGR2RGB))
    return pil_img

def img_from_pil_to_cv(pil_img):
    np_img= get_np_img(pil_img)
    cv_np_img=cv2.cvtColor(np_img,cv2.COLOR_RGB2BGR)
    return cv_np_img

def convert_wand_to_pil(wand_image):
    I = Image.open(io.BytesIO(wand_image.make_blob("jpg")))
    I = I.convert('RGB')
    #I = rotate_PIL_img_exif(I)
    width, height = I.size

    return I

def read_img(fname_or_img):
    #--读文件
    try:
        I = Image.open(fname_or_img)
        I = I.convert('RGB')
        if I.format != 'JPEG':
            img_file = io.BytesIO()
            I.save(img_file, "JPEG", quality=100)
            I = Image.open(img_file)
            I = I.convert('RGB')
        #print(1111,fname_or_img)
        #I = rotate_PIL_img_exif(I)
        # only debug test
    except:
        I = fname_or_img
    
    width, height = I.size
    
    return I


def get_np_img(I,resize_width=None):
    img=np.array(I)
    if img.ndim == 2:
        img = np.reshape(img, (img.shape[0], img.shape[1], 1))
        img = np.concatenate((img, img, img), axis=2)
    #'''
    h,w,t=img.shape
    if t==4:
        img = cv2.cvtColor(img,cv2.COLOR_RGBA2RGB)  
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    #'''
    return img



def np_crop_img_from_bbox(img,bbox):
    (x1,y1,x2,y2,x3,y3,x4,y4)=get_region_by_bbox(bbox)

    #width=x2-x1
    #height=y3-y1
    #new_shape=(height,width,img.shape[2])
    #new_im = 255*np.ones(new_shape,dtype=np.uint8)
    new_im=img[y1:y3,x1:x2]

    
    return new_im

def bbox2box(bbox):
    return [int(bbox[0]),int(bbox[1]),int(bbox[2])-int(bbox[0]),int(bbox[3])-int(bbox[1])]


def strim_pos(pos,limit_size,strim_size,strim_type):
    if pos%strim_size==0:
        return pos
    if strim_type=='small':
        return (pos/strim_size)*strim_size
    return min((pos/strim_size+1)*strim_size,(limit_size/strim_size)*strim_size)


def strim_box(bbox,img_width,img_height,strim_size=16):
    x1=strim_pos(bbox[0],img_width,strim_size,strim_type='small')
    y1=strim_pos(bbox[1],img_height,strim_size,strim_type='small')
    x3=strim_pos(bbox[2],img_width,strim_size,strim_type='large')
    y3=strim_pos(bbox[3],img_height,strim_size,strim_type='large')
    return [x1,y1,x3,y3]

def expand_bbox_with_offset(img_width,img_height,bbox,h_offset_ratio,w_offset_ratio=None,M_strim=0):
    if w_offset_ratio is None:
        w_offset_ratio=h_offset_ratio

    (x1,y1,x2,y2,x3,y3,x4,y4)=get_region_by_bbox(bbox)
    box_width=x3-x1
    box_height=y3-y1
    w_delta=int(w_offset_ratio*box_width)
    h_delta=int(h_offset_ratio*box_height)

    x1=max(x1-w_delta,0)
    y1=max(y1-h_delta,0)
    x3=min(x3+w_delta,img_width)
    y3=min(y3+h_delta,img_height)

    #--大小对齐
    if M_strim>0:
        box_width = x3 - x1
        box_height = y3 - y1
        if box_height%M_strim!=0 and (y1>=M_strim or img_height-y3>=M_strim ):
            new_h = (box_height//M_strim+1)*M_strim
            if y1>=M_strim:
                y1 = y3 - new_h
            elif img_height-y3>=M_strim:
                y3 = y1 + new_h

        if box_width%M_strim!=0 and (x1>=M_strim or img_width-x3>=M_strim ):
            new_w = (box_width//M_strim+1)*M_strim
            if x1>=M_strim:
                x1 = x3 - new_w
            elif img_width-x3>=M_strim:
                x3 = x1 + new_w

    return [x1,y1,x3,y3]


def expand_bbox_with_offset_special_for_other_type(img_width, img_height, bbox, h_offset_ratio, w_offset_ratio=None):
    if w_offset_ratio is None:
        w_offset_ratio = h_offset_ratio

    (x1, y1, x2, y2, x3, y3, x4, y4) = get_region_by_bbox(bbox)
    box_width = x3 - x1
    box_height = y3 - y1
    w_delta = int(w_offset_ratio * box_width)
    h_delta = int(h_offset_ratio * box_height)

    x1 = max(x1, 0)
    y1 = max(y1, 0)
    x3 = min(x3, img_width)
    y3 = min(y3 + h_delta, img_height)

    return [x1, y1, x3, y3]


def np_crop_line_img_from_bbox_with_offset(img,bbox,w_offset=0.0,h_offset=0.0,small_delta=0):
    height,width,t=img.shape

    (x1,y1,x2,y2,x3,y3,x4,y4)=get_region_by_bbox(bbox)
    box_width=x3-x1
    box_height=y3-y1
    w_delta=small_delta+int(w_offset*box_height)
    h_delta=small_delta+int(h_offset*box_height)

    x1=max(x1-w_delta,0)
    y1=max(y1-h_delta,0)
    x3=min(x3+w_delta,width)
    y3=min(y3+h_delta,height)

    return np_crop_img_from_bbox(img,[x1,y1,x3,y3])


def crop_line_img_from_bbox_with_offset(img,bbox,w_offset=0.0,h_offset=0.0,small_delta=0):
    width,height=img.size

    (x1,y1,x2,y2,x3,y3,x4,y4)=get_region_by_bbox(bbox)
    box_width=x3-x1
    box_height=y3-y1
    w_delta=small_delta+int(w_offset*box_height)
    h_delta=small_delta+int(h_offset*box_height)

    x1=max(x1-w_delta,0)
    y1=max(y1-h_delta,0)
    x3=min(x3+w_delta,width)
    y3=min(y3+h_delta,height)
    new_box = (x1,y1,x3,y3)
        
    cropImg = img.crop(new_box)
    
    return cropImg

def np_rotate_img_by_rotate_info(np_img,rotate_detail_angel,angle_offset=0):
    if rotate_detail_angel<=angle_offset or rotate_detail_angel>=(360-angle_offset):
        rotated_np_img = np_img
    else:
        rotated_np_img = np_rotate(np_img,rotate_detail_angel)
        #imutils.rotate_bound的旋转后的裁剪有问题
        ##rotated_np_img= imutils.rotate_bound(np_img,rotate_detail_angel)
    
    return rotated_np_img


def get_rotate_img_by_rotate_info(img_raw,rotate_detail_angel,angle_offset=0):
    if rotate_detail_angel<=angle_offset or rotate_detail_angel>=(360-angle_offset):
        rotate_img_raw = img_raw
    else:
        rotate_img_raw=img_raw.rotate(360-int(rotate_detail_angel),expand=True) 
    
    return rotate_img_raw
    


def get_region_by_bbox(bbox):
    x1=int(bbox[0])
    y1=int(bbox[1])
    x3=int(bbox[2])
    y3=int(bbox[3])
    
    
    
    x2=x3
    y2=y1
    x4=x1
    y4=y3
    
    return (x1,y1,x2,y2,x3,y3,x4,y4)


def check_box_overlap(r1,r2):
    ratio, F_flag, area_ratio = check_box_overlap_with_area(r1, r2)
    return ratio,F_flag


def check_box_overlap_with_area(r1, r2):
    [x1, y1, width1, height1] = r1
    [x2, y2, width2, height2] = r2
    x1 = int(x1)
    y1 = int(y1)
    width1 = int(width1)
    height1 = int(height1)

    x2 = int(x2)
    y2 = int(y2)
    width2 = int(width2)
    height2 = int(height2)

    endx = max(x1 + width1, x2 + width2)
    startx = min(x1, x2)
    width = width1 + width2 - (endx - startx)

    endy = max(y1 + height1, y2 + height2)
    starty = min(y1, y2)
    height = height1 + height2 - (endy - starty)

    if width <= 0 or height <= 0:
        return float(0.0), False, 1.0

    Area = float(width * height)
    Area1 = float(width1 * height1)
    Area2 = float(width2 * height2)
    ratio = Area / min(Area1, Area2)

    return ratio, Area1 < Area2, min(Area1, Area2)/max(Area1, Area2)


def check_box_same_line(r1,r2):
    [x1,y1,width1,height1]=r1
    [x2,y2,width2,height2]=r2
    x1=int(x1)
    y1=int(y1)
    width1=int(width1)
    height1=int(height1)

    x2=int(x2)
    y2=int(y2)
    width2=int(width2)
    height2=int(height2)

    if abs(height1-height2)<(0.4*max(height1,height2)):
        if abs(y2-y1)<(0.4*max(height1,height2)):
            return True

   
    return False


def check_if_camera_exif(im):
    try:
        for tag, value in im._getexif().items():
            n = TAGS.get(tag, tag)
            print(102,n,value,tag)
            if n == 'Make':
                return True
            if n == 'Camera Model Name':
                return True
            if n == 'Exposure Time':
                return True
            if n == 'ISO':
                return True
    except:
        pass

    return False


def rotate_PIL_img_exif(im):
    try:
        for tag,value in im._getexif().items():
            print(101,TAGS.get(tag,tag),value,tag)
            if TAGS.get(tag,tag)=='Orientation':
                #print '--->Read imgs have EXIF...',TAGS.get(tag,tag),value
                orientation=value
                if orientation == 2:
                    # Vertical Mirror
                    mirror = im.transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation == 3:
                    # Rotation 180°
                    mirror = im.transpose(Image.ROTATE_180)
                elif orientation == 4:
                    # Horizontal Mirror
                    mirror = im.transpose(Image.FLIP_TOP_BOTTOM)
                elif orientation == 5:
                    # Horizontal Mirror + Rotation 90° CCW
                    mirror = im.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.ROTATE_90)
                elif orientation == 6:
                    # Rotation 270°
                    mirror = im.transpose(Image.ROTATE_270)
                elif orientation == 7:
                    # Horizontal Mirror + Rotation 270°
                    mirror = im.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.ROTATE_270)
                elif orientation == 8:
                    # Rotation 90°
                    mirror = im.transpose(Image.ROTATE_90)
                else:
                    mirror = im.copy()
                
                return mirror
    except:
        pass

    return im


def np_resize_max_size(img,max_size=2560,with_strim=False,strim_size=64):
    height, width, channel = img.shape

    # magnify image size
    target_size = max(height, width, max_size)

    if target_size > max_size:
        target_size = max_size
    
    ratio = float(target_size) / float(max(height, width))

    target_h, target_w = int(height * ratio), int(width * ratio)
    #target_h = target_h if target_h%2==0 else target_h+1
    #target_w = target_w if target_w%2==0 else target_w+1

    #print(111,height, width)
    #print(222,target_h, target_w)
    #print(444,ratio,max_size)
    proc = cv2.resize(img, (target_w, target_h), interpolation = cv2.INTER_LINEAR)

    if with_strim==False:
        return proc,ratio

    # make canvas and paste image
    target_h32, target_w32 = target_h, target_w
    if target_h % 32 != 0:
        target_h32 = target_h + (32 - target_h % 32)
    if target_w % 32 != 0:
        target_w32 = target_w + (32 - target_w % 32)

    bottom_pos=target_h32-target_h
    right_pos=target_w32-target_w
    pad_img = cv2.copyMakeBorder(proc, 0, bottom_pos, 0, right_pos, cv2.BORDER_CONSTANT, value=(255, 255, 255))
    #print(111,height, width)
    #print(222,target_h, target_w)
    #print(333,target_h32, target_w32)
    #print(444,ratio,max_size)

    return pad_img,ratio

def np_rotate(img,ang):
    (h, w) = img.shape[:2]
    (cX, cY) = (w/2, h/2)
    M = cv2.getRotationMatrix2D((cX, cY), ang, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # 计算旋转后的图像大小（避免图像裁剪）
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # 调整旋转矩阵（避免图像裁剪）
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    return cv2.warpAffine(img, M, (nW, nH))

def np_rotate_bad(img,ang):
    (h, w) = img.shape[:2]
    center = (w/2, h/2)

    M = cv2.getRotationMatrix2D(center, ang, 1.0)
    return cv2.warpAffine(img, M, (w, h))

def code_text(t):
    if sys.version_info < (3, 0):
        t=unicode(t,'utf-8','ignore').replace(u'\x1a', '')
    return t


def judge_two_seg_same_line(left_location,right_location):
    h1 = left_location[3] - left_location[1]
    h2 = right_location[3] - right_location[1]
    total_h=max(right_location[3],left_location[3])-min(right_location[1],left_location[1])

    return total_h<=max(h1,h2)+min(h1,h2)*0.2

def judge_box_is_vertical(row):
    if int(row[0][1])==int(row[1][1]) and int(row[2][1])==int(row[3][1]) \
        and int(row[0][0])==int(row[3][0]) and int(row[1][0])==int(row[2][0]):
        return True
    else:
        return False

def do_visual_freestyle_detetection(fname,np_one_img,freestyle_res_detection_and_recog):
    im = img_from_cv_to_pil(np_one_img)
    draw = ImageDraw.Draw(im)

    for r in freestyle_res_detection_and_recog:
        x1, y1 = r['bbox'][0], r['bbox'][1]
        x2, y2 = r['bbox'][2], r['bbox'][3]
        for line_w in range(0, 3):
            x = (x1 + line_w, y1 + line_w, x2 - line_w, y2 - line_w)
            draw.rectangle(x, outline="blue")

    im.save(fname, 'jpeg')
    return

def rotate_cv_with_offset(img_cv, angel,angel_offset=0):
    img_raw = img_from_cv_to_pil(img_cv)
    rotate_img,f_rotate = rotate_pil_with_offset(img_raw, angel,angel_offset)
    return get_np_img(rotate_img),f_rotate

def rotate_pil_with_offset(img_raw, rotate_detail_angel,angle_offset):
    #--旋转，如果在angel_offset区间就不必旋转（太小了就算了）
    #--返回，旋转后的pil_img
    if rotate_detail_angel < 0:
        rotate_detail_angel = 360 + rotate_detail_angel

    # -最后旋转角度旋转一下
    if rotate_detail_angel <= angle_offset or rotate_detail_angel >= (360 - angle_offset):
        rotate_img = img_raw
        f_rotate = False
    else:
        rotate_img = img_raw.rotate(360 - float(rotate_detail_angel), expand=True)
        f_rotate = True

    return rotate_img,f_rotate
