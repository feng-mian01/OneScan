import subprocess
import os
from utils.log_utils import logger

#调用外部命令
def run_cmd(cmd,cwd=None,timeout=300):
    try:
        logger.info(f"执行命令：{cmd}")
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8',
            timeout=timeout
        )
        return result.stdout,result.stderr,result.returncode
    except subprocess.TimeoutExpired:
        logger.error(f"命令执行超时：{cmd}")
        return "","Timeout",-1
    except Exception as e:
        logger.error(f"命令执行出错：{cmd},错误信息：{str(e)}")
        return "",str(e),-1
