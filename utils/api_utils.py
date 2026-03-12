import requests
import configparser
from utils.log_utils import logger

#fofa api
def fofa_data(query,page=1,size=1000):
    config = configparser.ConfigParser()
    config.read('./config/fofa_config.ini', encoding='utf-8')
    email = config.get('fofa','email')
    key = config.get('fofa','key')

    if not email or not key:
        logger.error("FOFA API配置错误：email或key为空")
        return None
    
     #构建API请求URL
    url = "https://fofa.so/api/v1/search/all"
    params = {
        'email':email,
        'key':key,
        'qbase64':query.encode('utf-8').base64encode().decode('utf-8'),
        'page':page,
        'size':size,
        'filter':'ip,port,domain,protocol'
    }

    try:
       response = requests.get(url,params=params,timeout=30)
       response.raise_for_status()
       data = response.json()
       if data.get('error'):
           logger.error(f"FOFA API请求错误：{data.get('error')}")
           return None
       return data.get('results',[])
    except Exception as e:
        logger.error(f"FOFA API请求出错：{str(e)}")
        return None
