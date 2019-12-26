from instabot import Bot
import re


def is_user_exist(current_user):
    return bot.get_user_id_from_username(current_user) is not None


def get_mentions(current_comment):
    # как искать регулярное выражение для инстаграмм описано в ссылке
    #     https://blog.jstassen.com/2016/03/code-regex-for-instagram-username-and-hashtags/
    reg_expr_for_user_instagram = r"(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)"

    mentions = re.findall(reg_expr_for_user_instagram, current_comment)
    filtered_mentions = [mention for mention in mentions if is_user_exist(mention)]
    return filtered_mentions

#ссылка из урока
url_name_user = 'beautybar.rus'
url_post_istagram = 'https://www.instagram.com/p/BtON034lPhu/'


instagram_login = ''
instagram_passwd = ''


bot = Bot()
bot.login(username=instagram_login, password=instagram_passwd)

media_id = bot.get_media_id_from_link(url_post_istagram)

comment_users = set()
for comment_full in bot.get_media_comments_all(media_id, False):
    comment = comment_full["text"]
    current_user_and_usercomment = get_mentions(comment)
    if current_user_and_usercomment:
        comment_author = comment_full["user"]["username"]
        print(comment_author)
        comment_users.add(comment_author)
print(comment_users)
