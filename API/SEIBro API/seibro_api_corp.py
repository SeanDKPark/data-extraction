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

def getIssucoCustnoByIsin(key, ISIN, SHOTN_ISIN):
    apiID = 'getIssucoCustnoByIsin'
    ISIN_param = 'ISIN:' + ISIN
    SHOTN_ISIN_param = 'SHOTN_ISIN:' + SHOTN_ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISIN_param + ',' + SHOTN_ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getStddtInfo(key, ISSUCO_CUSTNO, BEGIN_STD_DT, EXPRY_STD_DT = None, RGT_RACD = None):
    apiID = 'getStddtInfo'
    ISSUCO_CUSTNO_param = 'ISSUCO_CUSTNO:' + ISSUCO_CUSTNO
    BEGIN_STD_DT_param = 'BEGIN_STD_DT:' + BEGIN_STD_DT

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISSUCO_CUSTNO_param + ',' + BEGIN_STD_DT_param

    if EXPRY_STD_DT is not None:
        url_params += ',' + 'EXPRY_STD_DT:' + EXPRY_STD_DT
    if RGT_RACD is not None:
        url_params += ',' + 'RGT_RACD:' + RGT_RACD

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getGmeetInfo(key, ISSUCO_CUSTNO, ISSUIN_NO, RGT_STD_DT):
    apiID = 'getGmeetInfo'
    ISSUCO_CUSTNO_param = 'ISSUCO_CUSTNO:' + ISSUCO_CUSTNO
    ISSUIN_NO_param = 'ISSUIN_NO:' + ISSUIN_NO
    RGT_STD_DT_param = 'RGT_STD_DT:' + RGT_STD_DT

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISSUCO_CUSTNO_param + ',' + ISSUIN_NO_param + ',' + RGT_STD_DT_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getGmeetMeasureInfo(key, ISSUCO_CUSTNO, ISSUIN_NO, RGT_STD_DT):
    apiID = 'getGmeetMeasureInfo'
    ISSUCO_CUSTNO_param = 'ISSUCO_CUSTNO:' + ISSUCO_CUSTNO
    ISSUIN_NO_param = 'ISSUIN_NO:' + ISSUIN_NO
    RGT_STD_DT_param = 'RGT_STD_DT:' + RGT_STD_DT

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISSUCO_CUSTNO_param + ',' + ISSUIN_NO_param + ',' + RGT_STD_DT_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getFmnmAltInfo(key, ISSUCO_CUSTNO, RGT_STD_DT):
    apiID = 'getFmnmAltInfo'
    ISSUCO_CUSTNO_param = 'ISSUCO_CUSTNO:' + ISSUCO_CUSTNO
    RGT_STD_DT_param = 'RGT_STD_DT:' + RGT_STD_DT

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISSUCO_CUSTNO_param + ',' + RGT_STD_DT_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getCostPaySchedul(key, TH1_PAY_TERM_BEGIN_DT, PAY_COST_TPCD):
    apiID = 'getCostPaySchedul'
    TH1_PAY_TERM_BEGIN_DT_param = 'TH1_PAY_TERM_BEGIN_DT:' + TH1_PAY_TERM_BEGIN_DT
    PAY_COST_TPCD_param = 'PAY_COST_TPCD:' + PAY_COST_TPCD

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + TH1_PAY_TERM_BEGIN_DT_param + ',' + PAY_COST_TPCD_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getDivSchedulInfo(key, BEGIN_STD_DT, ISSUCO_CUSTNO = None, EXPRY_STD_DT = None, RGT_RSN_DTAIL_SORT_CD = None):
    # 입력 순서에 유의!
    apiID = 'getDivSchedulInfo'
    BEGIN_STD_DT_param = 'BEGIN_STD_DT:' + BEGIN_STD_DT

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + BEGIN_STD_DT_param

    if ISSUCO_CUSTNO is not None:
        url_params += ',' + 'ISSUCO_CUSTNO:' + ISSUCO_CUSTNO
    if EXPRY_STD_DT is not None:
        url_params += ',' + 'EXPRY_STD_DT:' + EXPRY_STD_DT
    if RGT_RSN_DTAIL_SORT_CD is not None:
        url_params += ',' + 'RGT_RSN_DTAIL_SORT_CD:' + RGT_RSN_DTAIL_SORT_CD

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getDivInfo(key, ISSUCO_CUSTNO, BEGIN_STD_DT, EXPRY_STD_DT = None):
    apiID = 'getDivInfo'
    ISSUCO_CUSTNO_param = 'ISSUCO_CUSTNO:' + ISSUCO_CUSTNO
    BEGIN_STD_DT_param = 'BEGIN_STD_DT:' + BEGIN_STD_DT

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISSUCO_CUSTNO_param + ',' + BEGIN_STD_DT_param

    if EXPRY_STD_DT is not None:
        url_params += ',' + 'EXPRY_STD_DT:' + EXPRY_STD_DT

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getOddLotInfo(key, ISSUCO_CUSTNO, TH1_PAY_TERM_BEGIN_DT):
    apiID = 'getOddLotInfo'
    ISSUCO_CUSTNO_param = 'ISSUCO_CUSTNO:' + ISSUCO_CUSTNO
    TH1_PAY_TERM_BEGIN_DT_param = 'TH1_PAY_TERM_BEGIN_DT:' + TH1_PAY_TERM_BEGIN_DT

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISSUCO_CUSTNO_param + ',' + TH1_PAY_TERM_BEGIN_DT_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

key = '9511094f04b80fa9ad0d98e80063b7e8a1321d59cd2fc58aea9aff42ac3e8c9c'

#Sample Data
ISIN_1 = 'KR7005930003'
SHOTN_ISIN_1 = '005930'
ISSUCO_CUSTNO_1 = '593'
BEGIN_STD_DT_1 = '20161231'
EXPRY_STD_DT_1 = '20181231'
RGT_RACD_1 = '001'
ISSUIN_NO_1 = '00593'
RGT_STD_DT_1 = '20171231'
ISSUCO_CUSTNO_2 = '3572'
RGT_STD_DT_1 = '20151001'
TH1_PAY_TERM_BEGIN_DT_1 = '20180720'
PAY_COST_TPCD_1 = '3'
RGT_RSN_DTAIL_SORT_CD_1 = '02'
ISSUCO_CUSTNO_3 = '10364'
TH1_PAY_TERM_BEGIN_DT_2 = '20180709'

#Test
# print(getIssucoCustnoByIsin(key, ISIN_1, SHOTN_ISIN_1))
# print(getStddtInfo(key, ISSUCO_CUSTNO_1, BEGIN_STD_DT_1))
# print(getStddtInfo(key, ISSUCO_CUSTNO_1, BEGIN_STD_DT_1, EXPRY_STD_DT_1, RGT_RACD_1))
# print(getGmeetInfo(key, ISSUCO_CUSTNO_1, ISSUIN_NO_1, RGT_STD_DT_1))
# print(getGmeetMeasureInfo(key, ISSUCO_CUSTNO_1, ISSUIN_NO_1, RGT_STD_DT_1))
# print(getFmnmAltInfo(key, ISSUCO_CUSTNO_2, RGT_STD_DT_1))
# print(getCostPaySchedul(key, TH1_PAY_TERM_BEGIN_DT_1, PAY_COST_TPCD_1))
# print(getDivSchedulInfo(key, BEGIN_STD_DT_1))
# print(getDivSchedulInfo(key, BEGIN_STD_DT_1, ISSUCO_CUSTNO_1, EXPRY_STD_DT_1, RGT_RSN_DTAIL_SORT_CD_1))
print(getDivInfo(key, ISSUCO_CUSTNO_1, BEGIN_STD_DT_1, EXPRY_STD_DT_1))
# print(getOddLotInfo(key, ISSUCO_CUSTNO_3, TH1_PAY_TERM_BEGIN_DT_2))