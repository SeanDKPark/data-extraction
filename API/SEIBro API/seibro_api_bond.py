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

def getBondIssuInfo(key, ISSU_DT = '', ISSUCO_CUSTNO = ''):
    apiID = 'getBondIssuInfo'
    ISSU_DT_param = 'ISSU_DT:' + ISSU_DT
    ISSUCO_CUSTNO_param = 'ISSUCO_CUSTNO:' + ISSUCO_CUSTNO

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISSU_DT_param + ',' + ISSUCO_CUSTNO_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getBondStatInfo(key, ISIN):
    apiID = 'getBondStatInfo'
    ISIN_param = 'ISIN:' + ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getIntPayInfo(key, ISIN):
    apiID = 'getIntPayInfo'
    ISIN_param = 'ISIN:' + ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getBondOptionXrcInfo(key, ISIN = '', ERLY_RED_DT = ''):
    apiID = 'getBondOptionXrcInfo'
    ISIN_param = 'ISIN:' + ISIN
    ERLY_RED_DT_param = 'ERLY_RED_DT:' + ERLY_RED_DT

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISIN_param + ',' + ERLY_RED_DT_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getShortmIssuInfo(key, ISIN, ERLY_RED_DT):
    apiID = 'getShortmIssuInfo'
    ISSU_DT_param = 'ISSU_DT:' + ISIN
    SECN_TPCD_param = 'SECN_TPCD:' + ERLY_RED_DT

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISSU_DT_param + ',' + SECN_TPCD_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getCDInfo(key, ISIN):
    apiID = 'getCDInfo'
    ISIN_param = 'ISIN:' + ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getCPInfo(key, ISIN):
    apiID = 'getCPInfo'
    ISIN_param = 'ISIN:' + ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getESTBInfo(key, ISIN):
    apiID = 'getESTBInfo'
    ISIN_param = 'ISIN:' + ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

key = '' # Enter API Key

#Sample Data
issu_dt1 = '20180803'
issuco_custno1 = '29998'
isin1 = 'KR6268761881'
isin2 = 'KR6032641E64'
isin3 = 'KR6225693573'
erly_red_dt1 = '20180824'
issu_dt2 = '20180801'
secn_tpcd1 = '12'
isin4 = 'KRZE00701E3V'
isin5 = 'KRZF30300A87'
isin6 = 'KRZS24449010'

#TEST
# print(getBondIssuInfo(key, issu_dt1, issuco_custno1))
# print(getBondStatInfo(key, isin1))
# print(getIntPayInfo(key, isin2))
# print(getBondOptionXrcInfo(key, isin3, erly_red_dt1))
# print(getShortmIssuInfo(key, issu_dt2, secn_tpcd1))
# print(getCDInfo(key, isin4))
# print(getCPInfo(key, isin5))
# print(getESTBInfo(key, isin6))