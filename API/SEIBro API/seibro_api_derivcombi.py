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

def getDerivCombiIssuInfo(key, ISSU_DT, SECN_KACD):
    apiID = 'getDerivCombiIssuInfo'
    ISSU_DT_param = 'ISSU_DT:' + ISSU_DT
    SECN_KACD_param = 'SECN_KACD:' + SECN_KACD

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISSU_DT_param + ',' + SECN_KACD_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getBassetUnredScale(key, STD_DT, STND_BASSET_CD, SECN_TPCD):
    apiID = 'getBassetUnredScale'
    STD_DT_param = 'STD_DT:' + STD_DT
    STND_BASSET_CD_param = 'STND_BASSET_CD:' + STND_BASSET_CD
    SECN_TPCD_param = 'SECN_TPCD:' + SECN_TPCD

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + STD_DT_param + ',' + STND_BASSET_CD_param + ',' + SECN_TPCD_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getDerivCombiIsinInfo(key, ISIN):
    apiID = 'getDerivCombiIsinInfo'
    ISIN_param = 'ISIN:' + ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getAssetInfo(key, ISIN):
    apiID = 'getAssetInfo'
    ISIN_param = 'ISIN:' + ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getAssetXrcInfo(key, ISIN):
    apiID = 'getAssetXrcInfo'
    ISIN_param = 'ISIN:' + ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getRedCondiInfo(key, ISIN):
    apiID = 'getRedCondiInfo'
    ISIN_param = 'ISIN:' + ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getRedIsinInfo(key, RED_DT, SECN_KACD, DERISEC_EXER_TPCD = None):
    apiID = 'getRedIsinInfo'
    RED_DT_param = 'RED_DT:' + RED_DT
    SECN_KACD_param = 'SECN_KACD:' + SECN_KACD

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + RED_DT_param + ',' + SECN_KACD_param

    if DERISEC_EXER_TPCD is not None:
        url_params += ',' + 'DERISEC_EXER_TPCD:' + DERISEC_EXER_TPCD

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

key = '9511094f04b80fa9ad0d98e80063b7e8a1321d59cd2fc58aea9aff42ac3e8c9c'

#Sample Data
issu_dt1 = '20180702'
secn_kacd1 = '4101'
std_dt1 = '20180731'
stnd_basset_cd1 = 'KSD020000101'
secn_tpcd1 = '41'
isin1 = 'KR6539335879'
isin2 = 'KR6673301885'
red_dt1 = '20180806'
derisec_exer_tpcd1 = '3'

#TEST
print(getDerivCombiIssuInfo(key, issu_dt1, secn_kacd1))
print(getBassetUnredScale(key, std_dt1, stnd_basset_cd1, secn_tpcd1))
print(getDerivCombiIsinInfo(key, isin1))
print(getAssetInfo(key, isin1))
print(getAssetXrcInfo(key, isin2))
print(getRedCondiInfo(key, isin2))
print(getRedIsinInfo(key, red_dt1, secn_kacd1, derisec_exer_tpcd1))