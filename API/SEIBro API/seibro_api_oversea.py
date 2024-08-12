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

def getNationFrsecCusInfo(key, STD_DT, NATION_CD):
    apiID = 'getNationFrsecCusInfo'
    STD_DT_param = 'STD_DT:' + STD_DT
    NATION_CD_param = 'NATION_CD:' + NATION_CD

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + STD_DT_param + ',' + NATION_CD_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getNationFrsecSetlInfo(key, SETL_DT, NATION_CD):
    apiID = 'getNationFrsecSetlInfo'
    SETL_DT_param = 'SETL_DT:' + SETL_DT
    NATION_CD_param = 'NATION_CD:' + NATION_CD

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + SETL_DT_param + ',' + NATION_CD_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getSecnFrsecCusInfo(key, STD_DT, ISIN):
    apiID = 'getSecnFrsecCusInfo'
    STD_DT_param = 'STD_DT:' + STD_DT
    ISIN_param = 'ISIN:' + ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + STD_DT_param + ',' + ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

def getSecnFrsecSetlInfo(key, PROC_DT, ISIN):
    apiID = 'getSecnFrsecSetlInfo'
    PROC_DT_param = 'PROC_DT:' + PROC_DT
    ISIN_param = 'ISIN:' + ISIN

    url_base = 'http://seibro.or.kr/OpenPlatform/callOpenAPI.jsp'
    url_key = '?key=' + key
    url_spec = '&apiId=' + apiID
    url_params = '&params=' + PROC_DT_param + ',' + ISIN_param

    url = url_base + url_key + url_spec + url_params

    response = requests.get(url)

    result_df = ResponseToDf(response)
    return result_df

key = '9511094f04b80fa9ad0d98e80063b7e8a1321d59cd2fc58aea9aff42ac3e8c9c'

# Sample Data
STD_DT_1 = '20180806'
NATION_CD_1 = 'US'
SETL_DT_1 = '20180806'
ISIN_1 = 'US0231351067'
PROC_DT_1 = '20180806'

#TEST
# print(getNationFrsecCusInfo(key, STD_DT_1, NATION_CD_1))
# print(getNationFrsecSetlInfo(key, SETL_DT_1, NATION_CD_1))
# print(getSecnFrsecCusInfo(key, STD_DT_1, ISIN_1))
# print(getSecnFrsecSetlInfo(key, PROC_DT_1, ISIN_1))