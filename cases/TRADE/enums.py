from enum import Enum


class CardType(Enum):
    ID_CARD = 1  # 二代身份证
    PASSPORT = 2  # 护照
    MTPHKMK = 3  # 港澳xxx
    TRTP = 4  # 台湾xxx


class PayType(Enum):  # 返现出款渠道
    XI_DIAN = 3  # 喜点
    ALI_PAY = 4  # 支付宝
    WECHAT_PAY = 5  # 微信


class StatusCode(Enum):
    OK = "200"
    OrderNotExist = "96604404"
    SystemError = "9999"
    EmptyReqSource = "96603001"
    EmptyReqId = "96603001"
    EmptyBusinessType = "96603001"
    EmptyBusinessId = "96603001"
    EmptyRealName = "96603001"
    EmptyCardType = "96603001"
    EmptyCardCode = "96603001"
    EmptyAmount = "96603001"
    WrongCardType = "96603001"
    EmptyPayType = "96603001"
    WrongPayType = "96603001"
    EmptyALiIdentityTypeId = "96603001"
    EmptyALiPayAccount = "96603001"
    EmptyALiPayRealName = "96603001"
    EmptyRemark = "96603001"


class OrderError(Enum):
    OrderNotExist = "订单不存在"
    SubOrderNotExist = "子订单不存在"
    ParentOrderNotExist = "父订单不存在"
    EmptyCancelTime = "取消时间不能为空"
    OnlyCancelToBePayedOrder = "只有待支付状态才可以取消"


class OrderStatus(Enum):
    ALL = -1  # 全部
    TOBE_PAY = 0  # 待支付
    PAY = 1  # 已支付
    CANCEL = 2  # 已取消
    TOBE_DELIVERED = 3  # 待发货
    DELIVERED = 4  # 已发货
    TOBE_REFUNDED = 5  # 待退款
    REFUNDING = 6  # 退款中
    REFUNDED = 7  # 已退款
    FINISHED = 8  # 已收货完成
    CLOSED = 9  # 关闭


class CashBackError(Enum):
    EmptyReqSource = "请求来源不能为空"
    EmptyReqId = "请求序号不能为空"
    EmptyBusinessType = "业务类型不能为空"
    EmptyBusinessId = "业务ID不能为空"
    EmptyRealName = "真实姓名不能为空"
    EmptyCardType = "证件类型不能为空"
    EmptyCardCode = "证件号码不能为空"
    EmptyRechargeAmount = "充值金额不能为空"
    EmptyCashBackAmount = "返现金额不能为空"
    WrongCardType = "目前仅支持二代身份证"
    EmptyPayType = "出款渠道不能为空"
    WrongPayType = "暂不支持除支付宝之外的返现渠道"
    EmptyALiIdentityTypeId = "支付宝返现-支付宝支付类型不能为空"
    EmptyALiPayAccount = "支付宝返现-支付宝账号不能为空"
    EmptyALiPayRealName = "支付宝返现-真实姓名不能为空"
    EmptyRemark = "账单描述不能为空"


class Common(Enum):
    ReqSource = "ShiShuaiGangTest"
