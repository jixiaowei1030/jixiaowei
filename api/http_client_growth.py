from utils.http.helper import get_daka, get_ops, post_m, get_m
from utils.http import BaseClient
import random


class HttpClientGrowth(BaseClient):


# 增长-绘本馆拉新活动

    @get_growth('/xmkp-cpb-web/front/vip/free_payment/origin_info')
    def growth_originInfo(self):
        """
        查询用户绘本馆vip权限
        """
    @post_ops("/xmkp-growth-activity/activity/get", is_json_req=True)
    def growth_cpbActivity(self, activityId):
        """
        查询绘本馆活动信息
        """
    @post_ops("/xmkp-growth-activity/goods/get", is_json_req=True)
    def growth_cpbActivityGood(self, activityId):
        """
        查询绘本馆活动赠品信息
        """

    @post_opsGrowth("/xmkp-growth-activity/auth/my/invite/get", is_json_req=True)
    def growth_ActivityInvite(self, activityId, uid):
        """
        查询绘本馆活动我的邀请人数
        """

    @post_opsGrowth("/xmkp-growth-activity/auth/my/activity/address/save",is_json_req=True)
    def growth_ActivityAddress(self, data):
        """
        填写收货地址
        """
    @post_opsGrowth("/xmkp-growth-activity/auth/my/activity/goods", is_json_req=True)
    def growth_myGoods(self,activityId):
        """
        查看用户是否有实物奖品
        """

    @post_opsGrowth("/xmkp-growth-activity/auth/my/account/detail", is_json_req=True)
    def growth_myAccount(self,activityId):
        """
        查看用户的账号金额
        """
    @post_opsGrowth("/xmkp-growth-activity/auth/my/account/withdraw", is_json_req=True)
    def growth_withdraw(self, accountId, aliAccount, amount,realName):
        """
        用户提现
        """
    @post_opsGrowth("/xmkp-growth-activity/auth/my/invite/exchange",is_json_req=True)
    def growth_exchange(self,activityId):
        """
        兑换活动邀请天数
        """
    @post_opsGrowth("/xmkp-growth-activity/top/detail", is_json_req=True)
    def growth_topDetail(self,activityId):
        """
        查询排行榜
        """

    @post_opsGrowth("/xmkp-growth-activity/auth/rights/get", is_json_req=True)
    def growth_userRight(self,rightsId):
        """
        用户权益查询
        """
    @post_opsGrowth("/xmkp-growth-activity/auth/rights/receive", is_json_req=True)
    def growth_ReceiveRight(self,accountId, rightsDetailId):
        """
        领取用户权益
        """

    #售前页接口
    @get_m("/ort/front/products/presalepage/%d"%(random.randint(179,197)))
    def growth_pageinfo(self):
        """
        查询售前页信息
        """

    @get_m("/eduOps/notcheck/group/code/campRef?campRef=971")
    def growth_groupcode(self):
        """
        获取加群码
        """

    @get_m("/ort/front/api/v1/invite/coupon/status")
    def growth_couponstatus(self, couponid):
        """
        查询售前页优惠卷status
        """

    @post_m("/ort/front/api/v1/invite/coupon")
    def growth_usecoupon(self, couponid):
        """
        使用优惠卷
        """

    @get_m("/trade/prepareorder/info")
    def growth_tradeinfo(self, domain, businessTypeId, orderItems):
        """
        查询商业化下单信息
        """

#月课接口
    @get_m("/ort/front/api/v1/invite/growth/monthLadderReward")
    def growth_monthRewardConfig(self):
        """
        获取月课实物奖励配置
        """

    @get_m("/ort/front/api/v1/monthlyClassActivityPresale")
    def growth_monthRole(self):
        """
        月课身份判断
        """

    @get_m("/ort/front/api/v1/monthlyClassActivityPresale")
    def growth_not_monthRole(self):
        """
        非月课身份判断
        """

    @get_m("/ort/front/api/v1/userCashAccount")
    def growth_getUserCash(self):
        """
        获取月课用户账户金额
        """

    @get_m("/ort/front/api/v1/invite/growth/monthLadderRewardConfig")
    def growth_monthRewardConfig(self):
        """
        获取月课实物奖励配置
        """
    @get_m("/ort/front/api/v1/userInvitationRecord")
    def growrh_userInvitation(self):
        """
        用户邀请记录
        """
    @post_m("/ort/front/api/v1/operationNewUserAward")
    def growth_NewUserAward(self):
        """
        用户是否领取2元奖励
        """
    @get_m("/ort/front/api/v1/userWithdrawingRecord")
    def growth_Not_WithdrawingRecord(self):
        """
        用户无提现记录
        """

    @get_m("/ort/front/api/v1/userWithdrawingRecord")
    def growth_WithdrawingRecor(self):
        """
        用户有提现记录
        """
    @post_m("/ort/front/api/v1/withdrawingAmount",is_json_req=True)
    def growth_withdrawingAmount(self,uid,realName,cashAmount,aliAccount):
        """
        用户提现申请
        """
    @post_m("/ort/front/api/v1/exchangeReward",is_json_req=True)
    def growth_exchangeReward(self,address,realName,moblieNumber,prizeName,giftId):
        """
        填写用户地址
        """

    @get_growth("/xmkp-growth/front/poster?activityId=3&source=yueke")
    def growth_posters(self):
        """
        获取月课海报配置信息
        """

    #1元分销

    @get_m("/xmkp-growth/front/distribution/userId")
    def growth_userid(self, time):
        """
        获取用户id
        """

    @get_m("/xmkp-growth/front/distribution/config")
    def growth_config(self, time):
        """
        获取1元分销阶梯奖项配置信息
        """

    @get_m("/xmkp-growth/front/distribution/UserDistributionDetail")
    def growth_userdistribution(self, time, activityId):
        """
        获取用户阶梯奖励信息
        """

    @get_daka("/xmkp-growth/front/distribution/userGrowthRoleUrl")
    def growth_usergrowthroleurl1(self, time):
        """
        1元分销--获取分流跳转地址,跳转到0元售前页
        """

    @get_m("/xmkp-growth/front/distribution/userGrowthRoleUrl")
    def growth_usergrowthroleurl2(self, time):
        """
        月课分销--获取分流跳转地址，跳转到月课分销活动页
        """

    @get_m("/ort/front/api/v1/invite/poster")
    def growth_poster(self, presalePageId):
        """
        获取原版1元海报信息
        """

    @get_ops("/eduOps/api/v1/camp/482/presale/1072")
    def ops_presale(self, timeStamp):
        """
        获取售前页信息
        """

    @post_m("/ort/front/poster/identify?presalePageId=1072", is_json_req=True)
    def growth_identify(self, source, pictureCreatedTime, activityId):
        """
        生成海报的id
        """

    @post_m("/xmkp-growth/front/distribution/generatePost", is_json_req=True)
    def growth_generate_post(self, time, activityId):
        """
        新用户第一次生成海报
        """

    @get_m("/xmkp-growth/front/distribution/userGrowthRole")
    def growth_user_role1(self):
        """
        获取用户标签(月课用户)
        """

    @get_daka("/xmkp-growth/front/distribution/userGrowthRole")
    def growth_user_role2(self):
        """
        获取用户标签(无课用户)
        """

    @get_m("/xmkp-growth/front/cashAccount/userCashAccount")
    def growth_notcash_account(self, time):
        """
        用户一元分销账户信息(无邀请用户)
        """

    @get_m("/xmkp-growth/front/distribution/userInvitationRecord")
    def growth_notinvitation_record(self, time):
        """
        用户邀请记录(无邀请记录)
        """

    @get_m("/xmkp-growth/front/cashAccount/userWithdrawingRecord")
    def growth_notwithdrawing_record(self, time):
        """
        用户提现记录(无提现记录)
        """


    @get_m("/xmkp-growth/front/cashAccount/userCashAccount")
    def growth_cash_account(self, time):
        """
        用户一元分销账户信息(有邀请用户)
        """

    @get_m("/xmkp-growth/front/distribution/userInvitationRecord")
    def growth_invitation_record(self, time):
        """
        用户邀请记录(有邀请记录)
        """

    @get_m("/xmkp-growth/front/cashAccount/userWithdrawingRecord")
    def growth_withdrawing_record(self, time):
        """
        用户提现记录(有提现记录)
        """

    @post_m("/xmkp-growth/front/cashAccount/withdrawingAmount?time=1614499780003", is_json_req=True)
    def growth_withdrawing(self, uid, realName, cashAmount, aliAccount):
        """
        用户发起提现
        """


