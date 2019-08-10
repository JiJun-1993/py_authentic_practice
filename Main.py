from wxpy import *
import word_states as ws
import os
# def test():
bot = Bot(cache_path=True)
@bot.register([Friend])
def print_others(msg):
    try:
        if msg.type == "Sharing":
            # 存储处理
            # ws.savemsg(msg)
            # 获取链接中文章的正文
            context = ws.get_web_article(msg.url)
            # 获取前20个关键字
            statis = ws.stats_text_cn(context,20)
            # 生成并保存图片
            image = ws.text_graph(statis)
            # 返回图片给发信息的人
            msg.reply_image(image)
    except Exception as e:
        logging.exception(e)    

if __name__ == "__main__":
    bot.join()


