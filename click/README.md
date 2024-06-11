
# 一个简易的使用selenium的刷目标访问量的小程序
## 实现效果:
    能够实现定点访问目标网页,刷量,并且后台运行,防止机器人检测
## 文件结构：  
    environment.json  : 环境变量配置文件
    program.py   ：主要程序
## 环境变量解释：
### enviroment.json:
        "search_engine_name":　//浏览器设置
        [
        {
            "liulanqi": "https://cn.bing.com/?mkt=zh-CN",  //bing浏览器
            "id": "sb_form_q",                             //定位搜索框html元素
            "buttom": "sb_form_go",                        //定位按钮搜索框
            "filter": "b_tpcn"                            //定位超链接
        },
        {
            "liulanqi": "https://www.baidu.com/",
            "id": "kw",
            "buttom": "su",
            "filter": "c-title t t tts-title"
        }
        ]
        "search_words": [                //搜索关键词配置
            {
                "kw": "自主IEC61131-1",    //搜索词
                "target":
                    {
                    "type": "word",        //匹配原则,字符串字串匹配原则,标题含有这个词被认为是目标值
                    "value": ["上海翌控科技-您的IEC61131-3解决方案专家","攻克工业软件“卡脖子”技术"]
                    }
            }
        ],
        "time": 3,       //中间停顿时间
        "skip_time": 300,   //每次循环跳过时间
        "num_repete": 5,    //每次运行几次
        "target_see_time": 10   //目标页面浏览时间


