import os
import pandas as pd
from utils.log_utils import logger

#导出数据到Excel文件
def export_to_excel(data,filename,sheet_name='scan_result'):
    try:
        os.makedirs(os.path.dirname(filename),exist_ok=True)
        df = pd.DataFrame(data)
        df.to_excel(filename,sheet_name=sheet_name,index=False)
        logger.info(f"数据已成功导出到{filename}")
        return True
    except Exception as e:
        logger.error(f"导出数据到{filename}时出错：{e}")
        return False
    
#导出数据到txt文件
def export_to_txt(data,filename):
    try:
        os.makedirs(os.path.dirname(filename),exist_ok=True)
        with open(filename,'w',encoding='utf-8') as f:
            for line in data:
                f.write(f"{line}\n")
        logger.info(f"数据已成功导出到{filename}")
        return True
    except Exception as e:
        logger.error(f"导出数据到{filename}时出错：{e}")
        return False
