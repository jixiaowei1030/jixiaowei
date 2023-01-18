from utils.http import BaseClient
from utils.http.helper import get_xxm, post_xxm

class HttpClientXxm(BaseClient):
    '''
    喜马拉雅儿童
    '''

    # 新手活动入口
    @get_xxm("/xxm-activity-mobile/userTask/queryUserTask?taskScene=1")
    def query_user_task(self, mobile, password):
        '''
        @param taskScene
        '''


    # 获取任务活跃度
    @post_xxm("/xxm-activity-mobile/userTask/taskReceiveReward",is_json_req = True)
    def task_receive_reward(self, mobile, password, **kwargs):
        '''
        @param taskId : 任务id
        @param type
        '''

    # 获取vip奖励
    @post_xxm("/xxm-activity-mobile/userTask/receiveReward",is_json_req = True)
    def reveive_reward(self, mobile, password, **kwargs):
        '''
        @param rewardType：奖励类型
        '''

    # 频道页
    @post_xxm("/xxm-album-mobile/home/v2/loadPageContent",is_json_req = True)
    def load_page_content(self, mobile, password, **kwargs):
       '''
       @param:pageTitle
       @param:ageGroupId
       @param:babyId
       @param:currentPage
       @param:pageId
       @param:version
       '''


