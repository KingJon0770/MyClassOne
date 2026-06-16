import sys
import time
from datetime import datetime
from urllib.request import urlopen
import ssl

def get_real_time():
        """获取真实网络时间，防篡改本地时间"""
        try:
            with urlopen("https://www.baidu.com", timeout=6) as res:
                time_str = res.headers["Date"]
                return datetime.strptime(time_str, "%a, %d %b %Y %H:%M:%S %Z")
        except:
            # 断网才用本地时间
            return datetime.now()
def limit_box():
    # ==================== 可修改过期日期 ====================
    EXPIRE_Y = 2026
    EXPIRE_M = 5
    EXPIRE_D = 1
    # ========================================================

    # 跳过SSL校验，获取网络标准时间
    ssl._create_default_https_context = ssl._create_unverified_context

    # 初始化过期时间
    expire_date = datetime(EXPIRE_Y, EXPIRE_M, EXPIRE_D)
    now_date = get_real_time()

    # 时间判断
    if now_date >= expire_date:
        print("=" * 40)
        print(" 软件试用期限已到期")
        print(f"到期时间：{EXPIRE_Y}-{EXPIRE_M}-{EXPIRE_D}")
        print("请联系开发者授权使用")
        print("=" * 40)
        time.sleep(3)
        sys.exit()

    # 剩余天数提示
    remain = (expire_date - now_date).days
    print(f"程序正常运行，剩余试用天数：{remain} 天\n")
