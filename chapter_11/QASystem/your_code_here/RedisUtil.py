import redis
import json
from util.utils import login_expire


class RedisUtil(object):
    def __init__(self):
        self.client = redis.Redis()
        self.user_duplicate_key = 'qa_system:user:duplicate'
        self.session_key = 'qa_system:session'
        self.answer_key = 'qa_system:answer'

    def check_user_registered(self, user: str) -> bool:
        """
        使用Redis的集合判断用户是否已经注册，Key名字为 self.user_duplicate_key对应的字符串
        :param user: 用户名
        :return: True or False
        """
        return True

    def save_session(self, session_id: str, session_info: dict) -> None:
        """
        把Session信息保存到Redis的哈希表中。Key为self.session_key对应的字符串
        :param session_id: 字符串
        :param session_info: 字典
        :return:
        """
        pass

    def delete_session(self, session_id: str):
        """
        从Redis中删除用户对应的Session，哈希表的Key为self.session_key对应的字符串
        :param session_id: 字符串
        :return:
        """
        pass

    def fetch_session(self, session_id: str) -> dict:
        """
        使用session_id从Redis中获取Session。要注意以下3种情况：
        1. 在self.session_key对应的哈希表中，找不到session_id这个field
        2. Session获取下来是一个JSON字符串，解析为字典以后，里面有一个Key叫做`expire_time`，
           它的值是一个时间戳，表示这个Session的过期时间，如果这个时间戳小于time.time()，那么
           就需要让用户重新登录。判断的逻辑已经提前写好，直接调用`login_expire(session_data=session_data)`
           即可。返回True表示已经过期，返回False表示还没有过期
        3. 无论如何都要返回一个字典，如果Session存在而且没有过期，就返回Session，如果Session不存在或者已经
           过期，就返回一个空字典

        Redis Key为 self.session_key对应的字符串
        :param session_id: 字符串
        :return: dict
        """

        return {}

    def check_user_answer_question(self, user: str, question_id: str) -> bool:
        """
        判断用户是不是已经回答过这个问题了。
        Redis Key为self.answer_key对应的字符串
        :param user: 用户名
        :param question_id: 问题id
        :return: True 或者 False
        """
        return True

    def set_answer_flag(self, question_id: str, user: str) -> None:
        """
        回答问题以后，就需要标记这个用户已经回答了这个问题，从而防止他多次回复同一个问题。
        对应的Redis Key为self.answer_key的字符串
        :param question_id:  问题id
        :param user: 用户名
        :return:
        """
        pass