import time

debug = True


def debug_log(content):
    if debug:
        print content


def common_print(content):
    print  content


def color_print(content, color_offset):
    BASE = '\033[0;3%dm' % color_offset
    END = '\033[0m'
    common_print(BASE + content + END)


def time_print(content):
    common_print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()) + str(content))


def print_banner():
    banner = """
_____________      _____                         ____________                         _______              ______              _____
___  __ \__(_)_______  /____  _____________      __  ___/_  /____________ ______      ___    |____________ ___  /____  ___________(_)_______    {0.0.1#unstable}
__  /_/ /_  /_  ___/  __/  / / /_  ___/  _ \     _____ \_  __/  _ \_  __ `/  __ \     __  /| |_  __ \  __ `/_  /__  / / /_  ___/_  /__  ___/
_  ____/_  / / /__ / /_ / /_/ /_  /   /  __/     ____/ // /_ /  __/  /_/ // /_/ /     _  ___ |  / / / /_/ /_  / _  /_/ /_(__  )_  / _(__  )      author : centurio
/_/     /_/  \___/ \__/ \__,_/ /_/    \___/      /____/ \__/ \___/_\__, / \____/      /_/  |_/_/ /_/\__,_/ /_/  _\__, / /____/ /_/  /____/     License: GPLv3
                                                                  /____/                                        /____/
    """
    color_print(banner, 4)
