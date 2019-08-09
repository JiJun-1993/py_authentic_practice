from wxpy import *
import word_states as ws
import os
def main_test():
    bot = Bot(True)
    friends = bot.friends()
    # [<Friend: 游否>]
    # 确保搜索结果是唯一的，并取出唯一结果
    
    @bot.register()
    def print_others(msg):
        try:
            if msg.type == "Sharing":
                # 存储处理
                ws.savemsg(msg)
                # 获取链接中文章的正文
                context = ws.get_web_article(msg.url)
                # 获取前20个关键字
                statis = ws.stats_text_cn(context,20)
                # 生成并保存图片
                image = ws.text_graph(statis)
                # 返回图片给发信息的人
                msg.reply_image(image)
                
                print(msg)
        except Exception as e:
            logging.exception(e)    
    embed()

def test(url):
    context = ws.get_web_article(url)
    # 获取前20个关键字
    statis = ws.stats_text_cn(context,100)
    image_path = "1.png"
    # 生成并保存图片
    ws.text_graph(statis,image_path)
    # 返回图片给发信息的人
    # msg.reply_image(image_path)

if __name__ == "__main__":
    # url = "https://mp.weixin.qq.com/s?__biz=MjM5NjAxOTU4MA==&mid=3009227944&idx=1&sn=e49abe70e3f40dc48dde676f58a6866f&chksm=904620bba731a9ad7fef0e9da20a9a505dbbfc802300bc01f25826611682f6ae4c10091a3866&mpshare=1&scene=1&srcid=&sharer_sharetime=1565316989130&sharer_shareid=a650fe44233d15768e07550857984e6f#rd"
    # test(url)
    main_test()


