
"""
@Time ： 2021/4/13 19:55
@Auth ： liulian
@File ：test_audioRecordR_audio_record.py
@IDE ：PyCharm
"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestAudioRecordRAudioRecord(BaseTestCase):
    def test_audioRecordR_audio_record_1(self, cpb_api_scope, setupdata, data):
        """
        desc:读环节，上发录音
        steps：
        1.获取用户的response
        2.assert1接口是否请求成功'
        3.assert2绘本等级是否正确
        4.assert3绘本数量是否正确
        """
        # 第1步：请求接口，断言响应
        actual_res = cpb_api_scope[0].audioRecordR_audio_record(setupdata.mobile, setupdata.password,data.bookId, data.pageId, data.audioRef, data.text, data.duration, data.audioId, data.audioUrl, data.score, data.detail)
        print(actual_res)
        # 第2步：准备测试数据，获取用户的user_id
        # user_id = re.search("=(.*?)&", services.m_token["Cookie"]).group(1)
        user_id = cpb_api_scope[3]
        print(user_id)
        # 第3步：接口响应成功
        self.assert_equal(0, actual_res.code, "接口调用失败")
        # 第4步：查询mysql该录音信息并做断言
        expect_res = cpb_api_scope[1].query(
                "SELECT*FROM xmkp_child_picture_book.CPB_AUDIO_RECORD_R WHERE  book_id='2867'and page_id=2438 and audio_ref =244 and audio_id= 10484133020 and user_id={} ORDER BY create_time desc LIMIT 1".format(user_id), True)
        bookId = int(data.bookId)
        duration = float(data.duration)
        self.assert_equal(expect_res[0].audio_url, data.audioUrl, "上报的录音文件地址错误")
        self.assert_equal(expect_res[0]['book_id'], bookId, "上传录音对应绘本id错误")
        self.assert_equal(expect_res[0].page_id, data.pageId, "绘本页面错误")
        self.assert_equal(expect_res[0].audio_ref, data.audioRef, "文件错误")
        self.assert_equal(expect_res[0].text, data.text, "绘本名称错误")
        self.assert_equal(expect_res[0].duration, duration, "录音文件错误")
        self.assert_equal(expect_res[0].audio_id, data.audioId, "录音id错误")