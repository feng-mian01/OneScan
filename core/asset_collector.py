from utils.log_utils import logger
from utils.api_utils import get_fofa_data

#fofa资产收集
class AssetCollector:
    def collect_fofa(self,query,page=1,size=100):
        logger.info(f"开始收集fofa资产，查询:{query},页码:{page}")
        data = get_fofa_data(query,page,size)
        if data:
            logger.info(f"fofa资产收集成功，共获得{len(data)}条资产")
            assets = []
            for item in data:
                assets.append({
                    'ip':item[0] if len(item) > 0 else '',
                    'port':item[1] if len(item) > 1 else '',
                    'domain':item[2] if len(item) > 2 else '',
                    'protocol':item[3] if len(item) > 3 else '',
                })
            return assets
        else:
            logger.error(f"fofa资产收集无结果")
            return []