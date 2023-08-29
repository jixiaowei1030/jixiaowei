

file = [{
            "fileId": "603584879892357120",  # 地图厂房证或厂房租赁合同
            "fileName": "mmexport1689754224318.jpg",
            "subCategoryCode": "contractOfEstateOrLease"
        },
            {
                "fileId": "603585308428591104",  # 电费缴费凭证
                "fileName": "mmexport1689754227145.jpg",
                "subCategoryCode": "billsOfElectric"
            },
            {
                "fileId": "603585498497671168",  # 尽调照片
                "fileName": "mmexport1689754230008.jpg",
                "subCategoryCode": "dueDiligencePhotos"
            },
            {
                "fileId": "603585669293924352",  # 公司章程
                "fileName": "mmexport1689754235448.jpg",
                "subCategoryCode": "articlesOfAssociationLessee"
            },
            {
                "fileId": "613743243875991552",  # 增值税纳税申报表
                "fileName": "mmexport1692599787714.jpg",
                "subCategoryCode": "VAT_TaxReturn"
            },
            {
                "fileId": "609096490342146048",  # 新力租赁设备采购合同
                "fileName": "mmexport1690616408068.jpg",
                "subCategoryCode": "rentalEquipProcurementContract:9821"
            },
            {
                "fileId": "609095278494474240",  # 伊之密租赁设备采购合同
                "fileName": "mmexport1690616619857.jpg",
                "subCategoryCode": "rentalEquipProcurementContract:9822"
            },
            {
                "fileId": "609095408924745728",  # 合同公司1租赁设备采购合同
                "fileName": "mmexport1690616406693.jpg",
                "subCategoryCode": "rentalEquipProcurementContract:9820"
            },
            {
                "fileId": "609095475618373632",  # 合同公司J1租赁设备采购合同
                "fileName": "mmexport1690803025832.jpg",
                "subCategoryCode": "rentalEquipProcurementContract:9836"
            },
            {
                "fileId": "616222120510742528",  # F1租赁设备采购合同
                "fileName": "1693190688-origin-IMG_0082.JPG",
                "subCategoryCode": "rentalEquipProcurementContract:9847",
            },
            {
                "fileId": "616224607611379712",  # 合同公司J2租赁设备采购合同
                "fileName": "1693190696-origin-IMG_0084.JPG",
                "subCategoryCode": "rentalEquipProcurementContract:9841",
            },
            {
                "fileId": "616229055666577408",  # 特斯拉租赁设备采购合同
                "fileName": "Screenshot_20230828_104324_com.tencent.mm.jpg",
                "subCategoryCode": "rentalEquipProcurementContract:9852",
            }
        ]




def getAuthData(projectNo,custName,guarantor):
    data = []
    list = ['jxw','fht','xzw','cm','zll']
    custNameList = {'jxw':{
        "businessName": "测试Z500公司J2",
        "businessAddress": None,
        "businessCreditCode": "91310000NRNL32PU3J",
        "businessStartDate": None,
        "businessTermEndDate": None,
        "projectNo": projectNo,
        "preAprlCode": projectNo + "202308021551111545",
        "creditCustomerType": "ENT",
        "creditCustomerName": "季晓伟",
        "creditCustomerTel": "15705101126",
        "creditCustomerNo": "320683199410302714",
        "creditCustomerIdType": None,
        "certificateValidStartDate": None,
        "certificateValidEndDate": None,
        "identityType": "法人",
        "accountManager": "jxw",
        "creditCustomerSex": None,
        "creditCustomerAddress": "上海",
        "custCenterCode": None,
        "source": None
    },
        'fht':{
        "businessName": "测试软创",
        "businessAddress": None,
        "businessCreditCode": "911101083398346103",
        "businessStartDate": None,
        "businessTermEndDate": None,
        "projectNo": projectNo,
        "preAprlCode": projectNo + "202308031008597437",
        "creditCustomerType": "ENT",
        "creditCustomerName": "范怀通",
        "creditCustomerTel": "13020117356",
        "creditCustomerNo": "412702199005284111",
        "creditCustomerIdType": None,
        "certificateValidStartDate": None,
        "certificateValidEndDate": None,
        "identityType": "法人",
        "accountManager": "fht",
        "creditCustomerSex": None,
        "creditCustomerAddress": "深圳市罗湖区深南东路5047号平安银行总行",
        "custCenterCode": None,
        "source": None
    },
        'xzw':{
        "businessName":"测试Z500公司X1",
        "businessAddress":None,
        "businessCreditCode":"92469003MA5RUJ874M",
        "businessStartDate":None,
        "businessTermEndDate":None,
        "projectNo":projectNo,
        "preAprlCode":projectNo + "202308140855134388",
        "creditCustomerType":"ENT",
        "creditCustomerName":"夏紫文",
        "creditCustomerTel":"13623859715",
        "creditCustomerNo":"410223199805229877",
        "creditCustomerIdType":None,
        "certificateValidStartDate":None,
        "certificateValidEndDate":None,
        "identityType":"法人",
        "accountManager":"xzw",
        "creditCustomerSex":None,
        "creditCustomerAddress":"贵州省金沙县岩孔镇文丰村半边街组66号",
        "custCenterCode":None,
        "source":None
        },
        'cm':{
        "businessName": "测试苏中建设500",
        "businessAddress": None,
        "businessCreditCode": "913200001385836169",
        "businessStartDate": None,
        "businessTermEndDate": None,
        "projectNo": projectNo,
        "preAprlCode": projectNo + "202308080924703954",
        "creditCustomerType": "ENT",
        "creditCustomerName": "陈鸣",
        "creditCustomerTel": "18616005900",
        "creditCustomerNo": "320621198908174349",
        "creditCustomerIdType": None,
        "certificateValidStartDate": None,
        "certificateValidEndDate": None,
        "identityType": "法人",
        "accountManager": "cm",
        "creditCustomerSex": None,
        "creditCustomerAddress": "浦东",
        "custCenterCode": None,
        "source": None
    },
        'zll':{
        "businessName": "测试Z500公司Z1",
        "businessAddress": None,
        "businessCreditCode": "91420100591083185E",
        "businessStartDate": None,
        "businessTermEndDate": None,
        "projectNo": projectNo,
        "preAprlCode": projectNo + "202308021855216022",
        "creditCustomerType": "ENT",
        "creditCustomerName": "张玲玲",
        "creditCustomerTel": "13611956978",
        "creditCustomerNo": "622425199512047628",
        "creditCustomerIdType": None,
        "certificateValidStartDate": None,
        "certificateValidEndDate": None,
        "identityType": "法人",
        "accountManager": "zll",
        "creditCustomerSex": None,
        "creditCustomerAddress": "兜兜",
        "custCenterCode": None,
        "source": None
    }
    }
    list.remove(custName)
    if guarantor == '1':
        data.append(custNameList[list[0]])
    data.append(custNameList[custName])
    return data

def getBackData(projectNo,custName,guarantor):
    data = []
    list = ['jxw','fht','xzw','cm','zll']
    custNameList = {
        'jxw':{
        "preAprlCode": projectNo + "202308021551111545",
        "backFileId": "9020716865953443840",
        "businessLicenceFileId": "6868482948483813376",
        "faceFileId": "9020792603410939904",
        "ssqContractId": "3374018567829595143"
    },
        'fht':{
        "preAprlCode": projectNo + "202308031008597437",
        "ssqContractId": "3374570986154108930",
        "businessLicenceFileId": "9015937627781681152",
        "faceFileId": "9121959342059274240",
        "backFileId": "9121869907951071232",
    },
        'xzw':{
        "backFileId":"8895024158111641600",
        "businessLicenceFileId":"8894709044938473472",
        "faceFileId":"8894959213906960384",
        "preAprlCode":projectNo + "202308140855134388",
        "ssqContractId":"3368776852512300037"
        },
        'cm':{
        "preAprlCode": projectNo + "202308080924703954",
        "ssqContractId": "3378171893697653764",
        "businessLicenceFileId": "9040042016147361792",
        "faceFileId": "9105103334712094720",
        "backFileId": "9105038145694277632"
    },
        'zll':{
        "backFileId": "9008918643317559296",
        "businessLicenceFileId": "9008703624357224448",
        "faceFileId": "9008850490768109568",
        "preAprlCode": projectNo + "202308021855216022",
        "ssqContractId": "3374112083184329736"
    }
}
    list.remove(custName)
    if guarantor == '1':
        data.append(custNameList[list[0]])
    data.append(custNameList[custName])
    return data
