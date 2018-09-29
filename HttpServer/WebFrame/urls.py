#所有可以被访问的ＵＲＬ列表
from views import *

urls = [
        ('/time',show_time),
        ('/hello',say_hello),
        ('/bye',say_bye)
    ]