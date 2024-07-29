URGENT = 1
HIGH = 2
MEDIUM = 3
LOW = 4

"""
此模块放置全局静态变量。

:author: assassing
:contact: https://github.com/hxz393
:copyright: Copyright 2024, hxz393. 保留所有权利。
"""
# 程序基本信息
MAIN_TITLE = 'BaiduPanFilesTransfers'
MAIN_VERSION = '2.8.0'
HOME_PAGE = 'https://github.com/hxz393/BaiduPanFilesTransfers'
# noinspection LongLine
# 图标使用 zlib 压缩后，再用 base64 编码的值
ICON_BASE64 = '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'
# 配置文件路径
CONFIG_PATH = 'config.ini'
# 颜色主题，可选值参见：https://ttkbootstrap.readthedocs.io/en/latest/themes/
COLOR_THEME = 'yeti'
# 作用于多个 UI 组件的左边距和上边距
MW_PADDING = (10, 0)
# 气泡提示出现位置，相对于组件右上间距
TOOLTIP_PADDING = 25
# 气泡提示显示等待延迟，毫秒
TOOLTIP_DELAY = 100
# 每次转存延时时间，单位为秒
DELAY_SECONDS = 0.1
# 转存数量限制
SAVE_LIMIT = 1000
# 百度网盘地址
BASE_URL = 'https://pan.baidu.com'
# 目录名禁用的非法字符
INVALID_CHARS = r'<>|*?\:'
# 分享下拉框选项
EXP_MAP = {"1 天": 1, "7 天": 7, "30 天": 30, "永久": 0}
# 颜色相关字典
COLOR_MAP = {
    'tooltip': 'light yellow',
    'placeholder': 'grey',
    'text': 'black',
}
# 默认请求头
HEADERS = {
    'Host': 'pan.baidu.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'navigate',
    'Referer': 'https://pan.baidu.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,en-GB;q=0.6,ru;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
# 错误代码对应错误信息字典
ERROR_CODES = {
    -1: '链接错误，链接失效或缺少提取码',
    -4: '转存失败，无效登录。请退出账号在其他地方的登录',
    -6: '转存失败，请用浏览器无痕模式获取 Cookie 后再试',
    -7: r'转存失败，转存文件夹名有非法字符，不能包含 < > | * ? \ :，请改正目录名后重试',
    -8: '转存失败，目录中已有同名文件或文件夹存在',
    -9: '链接错误，提取码错误',
    -10: '转存失败，容量不足',
    -12: '链接错误，提取码错误',
    -62: '转存失败，链接访问次数过多，请手动转存或稍后再试',
    0: '转存成功',
    2: '转存失败，目标目录不存在',
    4: '转存失败，目录中存在同名文件',
    12: '转存失败，转存文件数超过限制',
    20: '转存失败，容量不足',
    105: '链接错误，所访问的页面不存在',
    404: '转存失败，秒传无效',
}
# 标签、标题和提示信息等内容取值来源。主要是 UI 界面相关文字，不包含结果日志插入文字
LABEL_MAP = {
    'cookie': '1.请输入百度网盘主页完整 Cookies，不带引号：',
    'folder_name': '2.请输入转存目标或分享来源目录名（留空为根目录）：',
    'links': '3.请粘贴百度网盘分享链接，每行一个：',
    'links_tip': """百度网盘分享链接示例：
https://pan.baidu.com/s/1tU58ChMSPmx4e3-kDx1mLg
https://pan.baidu.com/s/1jeDvKgas8-xUss7BUFpifQ uftv 
https://pan.baidu.com/e/1X5j-baPwZHmcXioKQPxb_w rsyf
https://pan.baidu.com/s/1gFqh-WGW2LdNqKpHbwtZ9Q?pwd=1234
https://pan.baidu.com/s/1kO3Yp3Q-opIFuY7GRPtd2A 提取码：qm3h
https://pan.baidu.com/share/init?surl=7M-O0-SskRPdoZ0emZrd5w&pwd=1234
http://pan.baidu.com/s/1_evfkiTrEZvOkC2hb-NiKw ju9a
目录名 https://pan.baidu.com/s/182A8FJ02gCq1MWYyrm_emA fm9k""",
    'options': '4.选项设置',
    'logs': '5.运行日志：',
    'logs_tip': '显示运行结果或错误信息',
    'save': '批量转存',
    'share': '批量分享',
    'trust': '系统代理',
    'trust_tip': '应用系统代理访问百度网盘',
    'custom': '指定目录',
    'custom_tip': '每个链接资源保存在单独文件夹中',
    'check': '检测模式',
    'check_tip': '检查链接是否有效但不转存',
    'help': '使用帮助',
    'settings_title': '设置分享选项',
    'expiry_title': '设置分享期限：',
    'password_title': '自定义提取码：',
    'default_password': '1234',
    'ok': '确认',
    'cancel': '取消',
    'validate_title': '请重新输入',
    'validate_msg': '提取码必须是四位数字或字母的组合',
    'undo': '撤销    Ctrl+z',
    'redo': '重做    Ctrl+y',
    'cut': '剪切    Ctrl+x',
    'copy': '复制    Ctrl+c',
    'paste': '粘贴    Ctrl+v',
    'select_all': '全选    Ctrl+a',
    'clear': '删除    Delete',
}
