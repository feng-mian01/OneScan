import configparser
from utils.cmd_utils import run_cmd
from utils.log_utils import logger

#端口扫描器
class PortScanner:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./config/scan_config.ini',encoding='utf-8')
        self.nmap_path = self.config.get('port_scan','nmap_path')
        self.default_ports = self.config.get('port_scan','default_ports')
        self.scan_type = self.config.get('port_scan','scan_type')
    
    def scan(self,target,ports=None):
        if not ports:
            ports = self.default_ports
    
        #构建nmap命令
        cmd = f'"{self.nmap_path}"{self.scan_type} -p {ports} {target} -oG -'
        stdout,stderr,return_code = run_cmd(cmd)

        if return_code != 0:
            logger.error(f"端口扫描命令执行失败：{stderr}")
            return []
        result = []
        for line in stdout.split('\n'):
            if 'open' in line and target in line:
                parts = line.split()
                port = parts[1].split('/')[0]
                server = parts[2] if len(parts) > 2 else 'unknown'
                result.append({
                    'target':target,
                    'port':port,
                    'server':server,
                    'status':'open'
                })
        logger.info(f"端口扫描完成，目标:{target}发现{len(result)}个开放端口")
        return result
