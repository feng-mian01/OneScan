import os
import configparser
from utils.cmd_utils import run_cmd
from utils.log_utils import logger

#dirsearch目录扫描
class DirScanner:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./config/scan_config.ini',encoding='utf-8')
        self.dirsearch_path = self.config.get('dir_scan','dirsearch_path')
        self.default_wordlists = self.config.get('dir_scan','default_wordlists')
        self.timeout = self.config.get('dir_scan','timeout')
    
    def scan(self,url,wordlists_path=None):
        if not wordlists:
            wordlists = self.default_wordlists
        if not os.path.exists(wordlists_path):
            logger.error(f"目录扫描词库文件{wordlists_path}不存在")
            return []
        cmd = f'python "{self.dirsearch_path}" -u {url} -w {wordlists_path} -t 10 --timeout {self.timeout} -q'
        stdout,stderr,return_code = run_cmd(cmd,cwd=os.path.dirname(self.dirsearch_path))

        if return_code != 0:
            logger.error(f"目录扫描命令执行失败：{stderr}")
            return []
        
        result = []
        for line in stdout.split('\n'):
            if '200' in line or '302' in line:
                parts = line.strip().split()
                if len(parts) >= 2:
                    status = parts[0]
                    path = parts[1]
                    result.append({
                        'url':url,
                        'path':path,
                        'status_code':status
                    })
        logger.info(f"目录扫描完成，目标:{url}发现{len(result)}个目录")
        return result