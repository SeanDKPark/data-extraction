import requests
import xml.etree.ElementTree as ET
import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None

def ResponseToDf(response):
    xml_data = response.text
    root = ET.fromstring(xml_data)

    rows = []

    for data_element in root.findall('.//data'):
        if data_element.find('.//RESULT') is not None:
            result_element = data_element.find('.//RESULT')
        elif data_element.find('.//result') is not None:
            result_element = data_element.find('.//result')
        else:
            print(xml_data)
            return 'no results in data'
        row = {}
        for child in result_element:
            row[child.tag] = child.attrib['value']
        rows.append(row)

    df = pd.DataFrame(rows)
    return df

def getStkStatInfo(key, SHOTN_ISIN, ISIN, ISSUCO_CUSTNO, STD_DT = None):
    apiID = 'getStkStatInfo'
    SHOTN_ISIN_param = 'SHOTN_ISIN:' + SHOTN_ISIN
    ISIN_param = 'ISIN:' + ISIN
    ISSUCO_CUSTNO_param = 'ISSUCO_CUSTNO:' + ISSUCO_CUSTNO

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + SHOTN_ISIN_param + ',' + ISIN_param + ',' + ISSUCO_CUSTNO_param

    if STD_DT is not None:
        url_params += ',' + 'STD_DT:' + STD_DT

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getUnlistCirclInfo(key, STD_DT, ISSUCO_CUSTNO, ISIN, SHOTN_ISIN = None):
    apiID = 'getUnlistCirclInfo'
    STD_DT_param = 'STD_DT:' + STD_DT
    ISSUCO_CUSTNO_param = 'ISSUCO_CUSTNO:' + ISSUCO_CUSTNO
    ISIN_param = 'ISIN:' + ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + STD_DT_param + ',' + ISSUCO_CUSTNO_param + ',' + ISIN_param

    if SHOTN_ISIN is not None:
        url_params += ',' + 'SHOTN_ISIN:' + SHOTN_ISIN

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getSlbDealingByIsin(key, ISIN, STD_DT):
    apiID = 'getSlbDealingByIsin'
    ISIN_param = 'ISIN:' + ISIN
    STD_DT_param = 'STD_DT:' + STD_DT

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISIN_param + ',' + STD_DT_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getShotnByMart(key, MART_TPCD):
    apiID = 'getShotnByMart'
    MART_TPCD_param = 'MART_TPCD:' + MART_TPCD

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + MART_TPCD_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getStkListInfo(key, ALT_BEGIN_DT, ALT_EXPRY_DT):
    apiID = 'getStkListInfo'
    ALT_BEGIN_DT_param = 'ALT_BEGIN_DT:' + ALT_BEGIN_DT
    ALT_EXPRY_DT_param = 'ALT_EXPRY_DT:' + ALT_EXPRY_DT

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ALT_BEGIN_DT_param + ',' + ALT_EXPRY_DT_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getXrcStkStatInfo(key, BOND_ISIN, XRC_STK_ISIN):
    apiID = 'getXrcStkStatInfo'
    BOND_ISIN_param = 'BOND_ISIN:' + BOND_ISIN
    XRC_STK_ISIN_param = 'XRC_STK_ISIN:' + XRC_STK_ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + BOND_ISIN_param + ',' + XRC_STK_ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getXrcStkOptionXrcInfo(key, RGT_STD_DT, BOND_ISIN, XRC_POSS_BEGIN_DT):
    apiID = 'getXrcStkOptionXrcInfo'
    RGT_STD_DT_param = 'RGT_STD_DT:' + RGT_STD_DT
    BOND_ISIN_param = 'BOND_ISIN:' + BOND_ISIN
    XRC_POSS_BEGIN_DT_param = 'XRC_POSS_BEGIN_DT:' + XRC_POSS_BEGIN_DT

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + RGT_STD_DT_param + ',' + BOND_ISIN_param + ',' + XRC_POSS_BEGIN_DT_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getStkIncdecDetails(key, SHOTN_ISIN, ISIN, ISSUCO_CUSTNO, ISSU_YEAR = None):
    apiID = 'getStkIncdecDetails'
    SHOTN_ISIN_param = 'SHOTN_ISIN:' + SHOTN_ISIN
    ISIN_param = 'ISIN:' + ISIN
    ISSUCO_CUSTNO_param = 'ISSUCO_CUSTNO:' + ISSUCO_CUSTNO

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + SHOTN_ISIN_param + ',' + ISIN_param + ',' + ISSUCO_CUSTNO_param

    if ISSU_YEAR is not None:
        url_params += ',' + 'ISSU_YEAR:' + ISSU_YEAR

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getSafeDpDutyDepoStatus(key, BEGIN_DT, EXPRY_DT, BIZ_TPCD, ISSUCO_CUSTNO = None, MART_TPCD = None):
    # 입력 순서에 유의
    apiID = 'getSafeDpDutyDepoStatus'
    BEGIN_DT_param = 'BEGIN_DT:' + BEGIN_DT
    EXPRY_DT_param = 'EXPRY_DT:' + EXPRY_DT
    BIZ_TPCD_param = 'BIZ_TPCD:' + BIZ_TPCD

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + BEGIN_DT_param + ',' + EXPRY_DT_param + ',' + BIZ_TPCD_param

    if ISSUCO_CUSTNO is not None:
        url_params += ',' + 'ISSUCO_CUSTNO:' + ISSUCO_CUSTNO
    if MART_TPCD is not None:
        url_params += ',' + 'MART_TPCD:' + MART_TPCD

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

key = '' # Enter API Key

#Sample Data
SHOTN_ISIN_1 = '005930'
ISIN_1 = 'KR7005930003'
ISSUCO_CUSTNO_1 = '593'
STD_DT_1 = '20180921'
STD_DT_2 = '20180807'
ISSUCO_CUSTNO_2 = '4131'
ISIN_2 = 'KR7064400005'
SHOTN_ISIN_2 = '064400'
ISIN_3 = 'KR7068270008'
STD_DT_3 = '20180822'
MART_TPCD_1 = '13'
ALT_BEGIN_DT_1 = '20181201'
ALT_EXPRY_DT_1 = '20181231'
BOND_ISIN_1 = 'KR6002221887'
XRC_STK_ISIN = 'KR7002220002'
RGT_STD_DT_1 = '20180321'
BOND_ISIN_2 = 'KR6019591561'
XRC_POSS_BEGIN_DT_1 = '20160609'
ISSU_YEAR_1 = '2018'
BEGIN_DT_1 = '20190221'
EXPRY_DT_1 = '20190227'
BIZ_TPCD_1 = '1'
MART_TPCD_2 = '11'

#TEST
# print(getStkStatInfo(key, SHOTN_ISIN_1, ISIN_1, ISSUCO_CUSTNO_1))
# print(getUnlistCirclInfo(key, STD_DT_2, ISSUCO_CUSTNO_2, ISIN_2, SHOTN_ISIN_2))
# print(getSlbDealingByIsin(key, ISIN_3, STD_DT_3))
# print(getShotnByMart(key, MART_TPCD_1))
# print(getStkListInfo(key, ALT_BEGIN_DT_1, ALT_EXPRY_DT_1))
# print(getXrcStkStatInfo(key, BOND_ISIN_1, XRC_STK_ISIN)) ## 이거 찾아서 한번 체크
# print(getXrcStkOptionXrcInfo(key, RGT_STD_DT_1, BOND_ISIN_2, XRC_POSS_BEGIN_DT_1)) #이거도
# print(getStkIncdecDetails(key, SHOTN_ISIN_1, ISIN_1, ISSUCO_CUSTNO_1, ISSU_YEAR_1))
# print(getSafeDpDutyDepoStatus(key, BEGIN_DT_1, EXPRY_DT_1, BIZ_TPCD_1, None, MART_TPCD_2))
