import re
from LAC import LAC

lac = LAC(mode="lac")
tiaoxingma = '^[A-Z0-9]*$'

PATTERN = r'([\u4e00-\u9fa5]{2,5}?(?:省|自治区|市)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州)){0,1}([\u4e00-\u9fa5]{2,7}?(?:村|镇|街道)){1}'

#
# def clean_none_value(testarray):
#     temp=[]
#     for each in testarray:
#         if each not in temp:
#             temp.append(each)
#     return temp
#
# def save_detail_info_for_feimu(temp,pos,value):
#     all_info=[]
#     # for i in range(len(pos)):
#     #     for j in range(len(temp)):
#     #         # 获取每个费目的相关信息
#     #         if temp[j] in value[i]:
#     #             shr_pos = pos[i]
#     #             height = pos[i][3][1] - pos[i][0][1]
#     #             width = pos[i][1][0] - pos[i][0][0]
#     #             for i in range(len(pos)):
#     #                 if shr_pos[0][0] - width / 2 < pos[i][0][0] < shr_pos[1][0] + width * 7 and shr_pos[0][
#     #                     1] - height / 2 < pos[i][0][1] < shr_pos[3][1] + height / 2:
#     #                     all_info.append(value[i])
#     for i in range(len(pos)):
#             # 获取每个费目的相关信息
#             if temp[0] in value[i]:
#                 shr_pos = pos[i]
#                 height = pos[i][3][1] - pos[i][0][1]
#                 width = pos[i][1][0] - pos[i][0][0]
#                 for i in range(len(pos)):
#                     if shr_pos[0][0] - width / 2 < pos[i][0][0] < shr_pos[1][0] + width * 20 and shr_pos[0][
#                         1] - height / 2 < pos[i][0][1] < shr_pos[3][1] + height*4:
#                         all_info.append(value[i])
#     return all_info
#
# def to_dict(new:list):
#     feimu = []
#     jine = []
#     shuie = []
#
#     for i in range(len(new)):
#         if i % 3 == 0:
#             feimu.append(new[i])
#         elif i % 3 == 1:
#             jine.append(new[i])
#         elif i % 3 == 2:
#             shuie.append(new[i])

#     d = [{} for i in range(len(feimu))]
#     for j in range(len(feimu)):
#         d[j]['费目'] = str(feimu[j])
#         d[j]['金额'] = str(jine[j])
#         d[j]['税额'] = str(shuie[j])
#
#     return d
#
#
# # 用来删除数组中存在的空字符串
# def not_empty(s):
#     return s and s.strip()
# def is_number(s):
#     try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
#         float(s)
#         return True
#     except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
#         pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
#     try:
#         import unicodedata  # 处理ASCii码的包
#         unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
#         return True
#     except (TypeError, ValueError):
#         pass
#     return False
# def split_number_and_chinese(testarray):
#     num=0
#     new=[]
#     new_index=[]
#     time=0
#     for i in range(len(testarray)):
#         if not is_number(testarray[i]):
#             for j in range(len(testarray[i])):
#                 if testarray[i][j].isalpha():
#                     num=j
#                     new_index.append(i)
#                     number=testarray[i][:j]
#                     alpha=testarray[i][j:]
#                     # 把汉子放在new中，数字替换当前
#                     new.append(alpha)
#                     testarray[i]=number
#                     break
#     for i in range(len(new_index)):
#         testarray.insert((new_index[i]+1+time),new[i])
#         time+=1
#     result = list(filter(not_empty, testarray))
#
#     new_array = []
#     for item in result:
#         if item[0].isdigit():
#             new_array.append(item)
#     return result

def yundanhao(pos, value, save_path):
    for i in range(len(pos)):
        if '整车' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width * 5 < pos[i][0][0] < shr_pos[0][0] and shr_pos[0][1] - height * 1.4 < \
                        pos[i][3][1] < shr_pos[0][1] + height / 2:
                    return value[i]
        if '货物运单' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width / 2 < pos[i][0][0] < shr_pos[1][0] + width * 3 and shr_pos[0][1] - height < \
                        pos[i][0][1] < shr_pos[2][1] + height / 2:
                    return value[i]


def chezhong_chehao(pos, value, save_path):
    for i in range(len(pos)):
        if '车种车号' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] < pos[i][0][0] < shr_pos[1][0] + width * 3 and shr_pos[1][1] - height / 2 < pos[i][0][
                    1] < shr_pos[1][1] + height:
                    return value[i]
        elif '货位' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] < pos[i][0][0] < shr_pos[1][0] + width * 7 and shr_pos[2][1] < pos[i][0][1] < \
                        shr_pos[2][1] + height:
                    return value[i]


def match_tiaoxingmabianhao(pos, value, save_path):
    for i in range(len(pos)):
        if '货物运单' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width < pos[i][0][0] < shr_pos[1][0] + width * 10 and shr_pos[1][1] - height < \
                        pos[i][0][1] < shr_pos[1][1] + height:
                    return value[i]
        elif re.match(tiaoxingma, value[i]):
            return value[i]


def match_tuoyunren(pos, value, save_path):
    for i in range(len(pos)):
        if '货位' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - int(4 * width) < pos[i][1][0] < shr_pos[0][0] and shr_pos[0][1] - height < pos[i][1][
                    1] < shr_pos[0][1] + height and '货位' not in value[i] and '经办人' not in value[i]:
                    return value[i]

def match_shouhuoren(pos, value, save_path):
    for i in range(len(pos)):
        if '封号' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - int(4 * width) < pos[i][1][0] < shr_pos[1][0] and shr_pos[0][1] - height/2 < pos[i][1][
                    1] < shr_pos[0][1] + height/2:
                    return value[i]

def match_daozhanren(pos, value, save_path):
    for i in range(len(pos)):
        if '施' in value[i] and '号' in value[i] and len(value[i]) == 3:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - int(4 * width) < pos[i][1][0] < shr_pos[0][0] and shr_pos[0][1] - height < pos[i][1][
                    1] < shr_pos[0][1] + height and '号' not in value[i] and '经办人' not in value[i]:
                    return value[i]


def match_dizhi(pos, value, save_path):
    for i in range(len(pos)):
        pattern = re.compile(PATTERN)
        m = pattern.search(value[i])
    return m


def match_xuqiuhao(pos, value, save_path):
    for i in range(len(pos)):
        if '需求号' in value[i] or '求号' in value[i]:
            if len(value[i].split('号')[-1]) > 5:
                if '.' in value[i]:
                    return value[i].split('号')[-1].replace('.','')
                else:
                    return value[i].split('号')[-1]
            else:
                shr_pos = pos[i]
                height = pos[i][3][1] - pos[i][0][1]  # 收货人的宽度
                width = pos[i][1][0] - pos[i][0][0]
                for i in range(len(pos)):
                    if shr_pos[1][0] - width / 2 < pos[i][0][0] < shr_pos[1][0] + width * 2 and shr_pos[1][1] - int(
                            height / 2) < pos[i][0][1] < shr_pos[1][1] + int(height / 2) and len(value[i]) > 11:
                        if '.' in value[i]:
                            return value[i].replace('.','')
                        else:
                            return value[i]

def match_fazhan(pos, value, save_path):
    for i in range(len(pos)):
        if '发站' in value[i] and '公司' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]  # 收货人的宽度
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] - width < pos[i][0][0] < shr_pos[1][0] + width and shr_pos[1][1] - int(height / 2) < \
                        pos[i][0][1] < shr_pos[1][1] + int(height / 2) and '发站' not in value[i]:
                    return value[i]


def match_tuoyunmingcheng(pos, value, save_path):
    for i in range(len(pos)):
        if '取货地址' in value[i] or '联货地址' in value[i] or '联货' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - int(width / 2) < pos[i][0][0] < shr_pos[1][0] and shr_pos[0][1] - height * 3.1 < \
                        pos[i][3][1] < shr_pos[0][1] - height / 2:
                    return value[i]


def match_shouhuomingcheng(pos, value, save_path):
    for i in range(len(pos)):
        if '送货地址' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - int(width / 3) < pos[i][0][0] < shr_pos[0][0] + width and shr_pos[0][
                    1] - height * 3.1 < pos[i][3][1] < shr_pos[0][1] + height / 2:
                    return value[i]


def match_daozhan(pos, value, save_path):
    for i in range(len(pos)):
        if '到站' in value[i] and '公司' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] < pos[i][0][0] < shr_pos[1][0] + width and shr_pos[1][1] - int(height / 2) < pos[i][0][
                    1] < shr_pos[1][1] + int(height / 2) and '发站' not in value[i] and '取货地址' not in value[i]:
                    return value[i]


def match_phone_tuoyun(pos, value, save_path):
    for i in range(len(pos)):
        if '车种车号' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width < pos[i][1][0] < shr_pos[0][0] and value[i].isdigit() and shr_pos[0][
                    1] - height < pos[i][1][1] < shr_pos[0][1] + height and value[i].isdigit() and len(value[i])>8:
                    return value[i]


def match_phone_shouhuo(pos, value, save_path):
    for i in range(len(pos)):
        if '布号' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - int(3 * width) < pos[i][1][0] < shr_pos[1][0] and shr_pos[0][1] - height / 2 < \
                        pos[i][1][1] < shr_pos[0][1] + height / 2 and value[i].isdigit() and len(value[i])>8:
                    return value[i]

    else:
        return 'None'


def match_huowumingcheng(pos, value, save_path):
    huowu = []
    for i in range(len(pos)):
        if '货物名称' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width * 1.5 < pos[i][0][0] < shr_pos[0][0] + width and shr_pos[3][1] - height / 2 < \
                        pos[i][0][1] < shr_pos[3][1] + (height * 3.5):
                    huowu.append(value[i])
            return huowu
    else:
        return huowu


def match_jianshu_all(pos, value, save_path):
    for i in range(len(pos)):
        if '合计' in value[i] and len(value[i]) == 2:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width < pos[i][0][0] < shr_pos[1][0] + int(width * 4) and value[i].isdigit() and \
                        shr_pos[0][1] - height < pos[i][1][1] < shr_pos[0][1] + height and '合计' not in value[i]:
                    return value[i] + '件'
        elif '包装' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width / 2 < pos[i][0][0] < shr_pos[0][0] + width and shr_pos[3][1] + height * 4.5 < \
                        pos[i][0][1] < shr_pos[3][1] + (height * 5.5):
                    return value[i]
    else:
        return 'None'


def match_jianshu_split(pos, value, save_path):
    huowu = []
    for i in range(len(pos)):
        if '件数' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width * 1.5 < pos[i][0][0] < shr_pos[0][0] + width and shr_pos[3][1] - height / 2 < \
                        pos[i][0][1] < shr_pos[3][1] + (height * 3.5):
                    huowu.append(value[i])
            if len(huowu) > 0:
                return huowu
    return huowu


def match_baozhuang_all(pos, value, save_path):
    for i in range(len(pos)):
        if '包装' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width / 2 < pos[i][0][0] < shr_pos[0][0] + width and shr_pos[3][1] + height * 3.5 < \
                        pos[i][0][1] < shr_pos[3][1] + (height * 4.5):
                    return value[i]
        elif '合计' in value[i] and len(value[i]) == 2:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width * 4 < pos[i][0][0] < shr_pos[1][0] + int(width * 5) and value[i].isdigit() and \
                        shr_pos[0][1] - height < pos[i][1][1] < shr_pos[0][1] + height:
                    return value[i]
    else:
        return 'None'

def match_huowujiage_all(pos, value, save_path):
    for i in range(len(pos)):
        if '货物价格' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width / 2 < pos[i][0][0] < shr_pos[0][0] + width and shr_pos[3][1] + height * 3.5 < \
                        pos[i][0][1] < shr_pos[3][1] + (height * 4.5):
                    return value[i]
        elif '合计' in value[i] and len(value[i]) == 2:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width * 5 < pos[i][0][0] < shr_pos[1][0] + int(width * 8) and value[i].isdigit() and \
                        shr_pos[0][1] - height < pos[i][1][1] < shr_pos[0][1] + height:
                    return value[i]
    else:
        return 'None'

def match_zhongliang_all(pos, value, save_path):
    for i in range(len(pos)):
        if '重量' in value[i] and 'kg' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width / 2 < pos[i][0][0] < shr_pos[0][0] + width and shr_pos[3][1] + height * 3.5 < \
                        pos[i][0][1] < shr_pos[3][1] + (height * 4.5):
                    if '|' in value[i]:
                        return value[i].split('|')[0]
                    else:
                        return value[i]
        elif '合计' in value[i] and len(value[i]) == 2:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width * 8 < pos[i][0][0] < shr_pos[1][0] + int(width * 11) and value[i].isdigit() and \
                        shr_pos[0][1] - height < pos[i][1][1] < shr_pos[0][1] + height:
                    if '|' in value[i]:
                        return value[i].split('|')[0]
                    else:
                        return value[i]
    else:
        return 'None'

def match_xinaglei_all(pos, value, save_path):
    for i in range(len(pos)):
        if '箱型箱类' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width / 2 < pos[i][0][0] < shr_pos[0][0] + width and shr_pos[3][1] + height * 3.5 < \
                        pos[i][0][1] < shr_pos[3][1] + (height * 4.5):
                    if '|' in value[i]:
                        return value[i].split('|')[-1]
                    else:
                        return value[i]
        elif '合计' in value[i] and len(value[i]) == 2:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width * 11 < pos[i][0][0] < shr_pos[1][0] + int(width * 14) and value[
                    i].isdigit() and shr_pos[0][1] - height < pos[i][1][1] < shr_pos[0][1] + height:
                    if '|' in value[i]:
                        return value[i].split('|')[-1]
                    else:
                        return value[i]
    else:
        return 'None'

def match_xinaghap_all(pos, value, save_path):
    for i in range(len(pos)):
        if '箱号' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width / 2 < pos[i][0][0] < shr_pos[0][0] + width and shr_pos[3][1] + height * 3.5 < \
                        pos[i][0][1] < shr_pos[3][1] + (height * 4.5):
                    return value[i]
        elif '合计' in value[i] and len(value[i]) == 2:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width * 14 < pos[i][0][0] < shr_pos[1][0] + int(width * 17) and value[
                    i].isdigit() and shr_pos[0][1] - height < pos[i][1][1] < shr_pos[0][1] + height:
                    return value[i]
    else:
        return 'None'

def match_shifeng_all(pos, value, save_path):
    for i in range(len(pos)):
        if '箱号' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] < pos[i][0][0] < shr_pos[1][0] and shr_pos[3][1] + height * 3.5 < pos[i][0][1] < \
                        shr_pos[3][1] + (height * 4.5):
                    return value[i]
        elif '合计' in value[i] and len(value[i]) == 2:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width * 17 < pos[i][0][0] < shr_pos[1][0] + int(width * 20) and value[
                    i].isdigit() and shr_pos[0][1] - height < pos[i][1][1] < shr_pos[0][1] + height:
                    return value[i]
    else:
        return 'None'

def match_quedingzl_all(pos, value, save_path):
    for i in range(len(pos)):
        if '人确定' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] < pos[i][0][0] < shr_pos[1][0] and shr_pos[3][1] + height * 5 < pos[i][0][1] < \
                        shr_pos[3][1] + (height * 6) and value[i][0].isdigit():
                    return value[i]
        elif '合计' in value[i] and len(value[i]) == 2:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width * 20 < pos[i][0][0] < shr_pos[1][0] + int(width * 23) and value[
                    i].isdigit() and shr_pos[0][1] - height < pos[i][1][1] < shr_pos[0][1] + height:
                    return value[i]
    else:
        return 'None'

def match_tiji_all(pos, value, save_path):
    for i in range(len(pos)):
        if '体积' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] < pos[i][0][0] < shr_pos[1][0] and shr_pos[3][1] + height * 4.5 < pos[i][0][1] < \
                        shr_pos[3][1] + (height * 6):
                    return value[i]
        elif '合计' in value[i] and len(value[i]) == 2:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width * 24 < pos[i][0][0] < shr_pos[1][0] + int(width * 25) and value[
                    i].isdigit() and shr_pos[0][1] - height < pos[i][1][1] < shr_pos[0][1] + height:
                    return value[i]
    else:
        return 'None'

def match_yunjia_all(pos, value, save_path):
    for i in range(len(pos)):
        if '运价号' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] < pos[i][0][0] < shr_pos[1][0] and shr_pos[3][1] - height / 2 < pos[i][0][1] < \
                        shr_pos[3][1] + (height * 6) and value[i].isdigit():
                    return value[i]
    else:
        return 'None'

def match_jifeizl_all(pos, value, save_path):
    for i in range(len(pos)):
        if '计费重量' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0]-width/2 < pos[i][1][0] < shr_pos[1][0]+width and shr_pos[3][1] + height * 4 < pos[i][0][1] < \
                        shr_pos[3][1] + (height * 6) and value[i][0].isdigit():
                    return value[i]
        elif '运价号' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width/2  < pos[i][0][0] < shr_pos[1][0] + width*2.5 and value[
                    i].isdigit() and shr_pos[3][1] + height*4 < pos[i][1][1] < shr_pos[3][1] + height*6 and value[i][0].isdigit():
                    return value[i]

    else:
        return 'None'

def match_huowujiage_split(pos, value, save_path):
    huowu = []
    for i in range(len(pos)):
        if '包装' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width / 2 < pos[i][0][0] < shr_pos[0][0] + width and shr_pos[3][1] - height / 2 < \
                        pos[i][0][1] < shr_pos[3][1] + (height * 3.5):
                    huowu.append(value[i])
            if len(huowu) > 0:
                return huowu
    else:
        return huowu


def match_zhongliang(pos, value, save_path):
    for i in range(len(pos)):
        if '合计' in value[i] and len(value[i]) == 2:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + int(5 * width) < pos[i][0][0] < shr_pos[1][0] + int(width * 15) and shr_pos[0][
                    1] - height / 2 < pos[i][1][1] < shr_pos[0][1] + height / 2 and '合计' not in value[i]:
                    return value[i] + 'KG'


def match_xianghao(pos, value, save_path):
    xianghao = []
    for i in range(len(pos)):
        if '箱号' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] < pos[i][1][0] < shr_pos[1][0] + width and shr_pos[3][1] < pos[i][0][1] < shr_pos[3][
                    1] + (height * 3) and '箱号' not in value[i]:
                    xianghao.append(value[i])
            return xianghao


def match_shifenghao(pos, value, save_path):
    sf = []
    for i in range(len(pos)):
        if '箱号' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] + width < pos[i][0][0] < shr_pos[1][0] + width * 3 and shr_pos[3][1] + height * 0.4 < \
                        pos[i][0][1] < shr_pos[3][1] + int(height * 3) and '施封' not in value[i]:
                    sf.append(value[i])
            return sf
    else:
        return sf


def match_feimu(pos, value, save_path):
    feimu = []
    origin_feimu=[]
    for i in range(len(pos)):
        if '费目' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width*2 < pos[i][0][0] < shr_pos[0][0] and shr_pos[3][1] < pos[i][0][
                    1] < shr_pos[3][1] + int(height * 5):
                    if len(value[i]) != 0:
                        feimu.append(value[i])
                    origin_feimu.append(value[i])
        elif '税额' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] - width / 2 < pos[i][0][0] < shr_pos[1][0] + width and shr_pos[3][1] < pos[i][0][1] < \
                        shr_pos[3][1] + int(height * 5):
                    pattern = re.compile("[\u4e00-\u9fa5]")
                    s = "".join(pattern.findall(value[i]))
                    if len(s) != 0:
                        feimu.append(s)
                    origin_feimu.append(value[i])
    if len(feimu) == 0:
        return 'None'
    else:
        return feimu,origin_feimu



def match_feiyongheji(pos, value, save_path):
    for i in range(len(pos)):
        if '大写' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width * 2.4 < pos[i][1][0] < shr_pos[0][0] and shr_pos[1][1] - height < pos[i][0][
                    1] < shr_pos[1][1] + height and '￥' in value[i]:
                    return value[i]

        elif '￥' in value[i]:
            return value[i]
        elif '费用合计' in value[i] or '用合计' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0] < pos[i][0][0] < shr_pos[1][0] + width * 2 and shr_pos[1][1] - height < pos[i][0][1] < \
                        shr_pos[1][1] + height:
                    return value[i]




def match_shuie(pos,value,save_path,jine_list):
    shuie=[]
    for j in range(len(jine_list)):
        for i in range(len(pos)):
            if jine_list[j] in value[i]:
                shr_pos = pos[i]
                height = pos[i][3][1] - pos[i][0][1]
                width = pos[i][1][0] - pos[i][0][0]
                for i in range(len(pos)):
                    if shr_pos[1][0] < pos[i][0][0] < shr_pos[1][0] + width*4 and shr_pos[0][1] - height / 2 < pos[i][0][1] < shr_pos[0][1]+height/2:
                        s = "".join(filter(lambda s: s in '0123456789.', value[i]))
                        shuie.append(s)
                        break
                break
    return shuie



def match_feimu_detail(feimu,jine,shuie):
    print('费目是',feimu)
    print('金额是',jine)
    print('税额是',shuie)
    feimu_detail=[]
    if len(feimu) == len(jine) == len(shuie):
        for i in range(len(feimu)):
            list = {
                "费目": feimu[i], "金额": jine[i], "税额": shuie[i]
            }
            feimu_detail.append(list)
    return  feimu_detail



def match_jine(pos, value, save_path):
    jine = []
    for i in range(len(pos)):
        if '箱号' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0]  < pos[i][0][0] < shr_pos[1][0] + width and shr_pos[3][1]+height*6 < pos[i][0][
                    1] < shr_pos[3][1] + int(height * 10):
                    if len(value[i]) != 0 and value[i][0].isdigit():
                        jine.append(value[i])
            for i in range(len(pos)):
                if '运价' in value[i]:
                    shr_pos = pos[i]
                    height = pos[i][3][1] - pos[i][0][1]
                    width = pos[i][1][0] - pos[i][0][0]
                    for i in range(len(pos)):
                        if shr_pos[0][0] - width < pos[i][0][0] < shr_pos[1][0] and shr_pos[3][1] + height * 6 < \
                                pos[i][0][
                                    1] < shr_pos[3][1] + int(height * 10):
                            if len(value[i]) != 0 and value[i][0].isdigit():
                                jine.append(value[i])

    if len(jine) == 0:
        return 'None'
    else:
        return jine




def baozhuang_split(pos, value, save_path):
    huowu = []
    for i in range(len(pos)):
        if '包装' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width / 2 < pos[i][0][0] < shr_pos[1][0] + width / 2 and shr_pos[3][1] - height / 2 < \
                        pos[i][0][1] < shr_pos[3][1] + (height * 3.5):
                    huowu.append(value[i])
            return huowu
    else:
        return huowu


def huowujiage_split(pos, value, save_path):
    huowu = []
    for i in range(len(pos)):
        if '货物价格' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] < pos[i][0][0] < shr_pos[1][0] and shr_pos[3][1] + height < pos[i][0][1] < shr_pos[3][
                    1] + (height * 4.5):
                    huowu.append(value[i])
            return huowu
    else:
        return huowu


def zhongliang_split(pos, value, save_path):
    huowu = []
    for i in range(len(pos)):
        if '重量' in value[i] and 'kg' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] < pos[i][0][0] < shr_pos[1][0] and shr_pos[3][1] < pos[i][0][1] < shr_pos[3][1] + (
                        height * 3.5):
                    huowu.append(value[i])
            return huowu
    else:
        return huowu


def xianglei_split(pos, value, save_path):
    huowu = []
    for i in range(len(pos)):
        if '箱型箱类' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] < pos[i][1][0] < shr_pos[1][0] + width / 2 and shr_pos[3][1] < pos[i][0][1] < \
                        shr_pos[3][1] + (height * 3.5):
                    huowu.append(value[i])
            return huowu
    else:
        return huowu


def quedingzhongliang_split(pos, value, save_path):
    huowu = []
    for i in range(len(pos)):
        if '人确定' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] - width / 2 < pos[i][0][0] < shr_pos[1][0] + width and shr_pos[3][1] + height * 1.1 < \
                        pos[i][0][1] < shr_pos[3][1] + (height * 4.5):
                    huowu.append(value[i])
            return huowu
    else:
        return huowu


def tiji_split(pos, value, save_path):
    huowu = []
    for i in range(len(pos)):
        if '体积' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] < pos[i][0][0] < shr_pos[1][0] + width and shr_pos[3][1] + height * 1.1 < pos[i][0][
                    1] < shr_pos[3][1] + (height * 4.5):
                    huowu.append(value[i])
            return huowu
    else:
        return huowu


def yunjia_split(pos, value, save_path):
    huowu = []
    for i in range(len(pos)):
        if '运价号' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[0][0] < pos[i][0][0] < shr_pos[1][0] + width / 4 and shr_pos[0][1]+width/2 < pos[i][0][1] < \
                        shr_pos[3][1] + (height * 6) and '号' not in value[i] and value[i].isdigit():
                    huowu.append(value[i])
            if len(huowu)!=0:
                return huowu
            else:
                return "None"


def jifeizhongliang_split(pos, value, save_path):
    huowu = []
    for i in range(len(pos)):
        if '计费重量' in value[i]:
            shr_pos = pos[i]
            height = pos[i][3][1] - pos[i][0][1]
            width = pos[i][1][0] - pos[i][0][0]
            for i in range(len(pos)):
                if shr_pos[1][0]-width/2 < pos[i][1][0] < shr_pos[1][0]+width and shr_pos[3][1] + height < pos[i][0][1] < shr_pos[3][
                    1] + (height * 4.5) and value[i][0].isdigit():
                    huowu.append(value[i])
            return huowu
    else:
        return huowu
