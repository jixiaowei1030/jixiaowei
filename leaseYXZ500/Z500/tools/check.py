import PyPDF2

def checkFinanceLease(pay_main_no):
    '''融资租赁合同'''
    pdf_text = getPdfText('直租_融资租赁合同.pdf')

    print(pdf_text)
    # print(pdf_text.split("\n")[4][3:])
    # print(pdf_text.split("\n")[-14][6:32])
    # print(pdf_text.split("\n")[13][3:])
    # print(pdf_text.split("\n")[14][-10:])
    # print(pdf_text.split("\n")[15][3:])
    # print(pdf_text.split("\n")[16][6:])
    # print(pdf_text.split("\n")[17][3:])
    # print(pdf_text.split("\n")[18][3:])
    # print(pdf_text.split("\n")[20][-32:-3])
    # print(pdf_text.split("\n")[22][25:35])
    # print(pdf_text.split("\n")[23][3:13])
    # print(pdf_text.split("\n")[23][18:28])
    # print(pdf_text.split("\n")[25][21:23])
    # print(pdf_text.split("\n")[26][12:14])
    # print(pdf_text.split("\n")[27][11:15])
    # print(pdf_text.split("\n")[30][17:26])
    # print(pdf_text.split("\n")[30][31:42])
    # print(pdf_text.split("\n")[32][:1])
    # print(pdf_text.split("\n")[39][4:19])
    # print(pdf_text.split("\n")[41][6:15])
    # print(pdf_text.split("\n")[43][10:16])
    # print(pdf_text.split("\n")[43][21:25])
    # print(pdf_text.split("\n")[44][11:21])
    # print(pdf_text.split("\n")[44][26:36])
    # print(pdf_text.split("\n")[47][9:13])
    # print(pdf_text.split("\n")[47][18:19])
    # print(pdf_text.split("\n")[55][:7])
    # print(pdf_text.split("\n")[56][:6])
    # print(pdf_text.split("\n")[57][:4])
    # print(pdf_text.split("\n")[58][3:14])
    # print(pdf_text.split("\n")[58][14:43])
    # print(pdf_text.split("\n")[58][44:])

    # print(pdf_text.split("\n")[59][:])
    # print(pdf_text.split("\n")[65][11:14])
    # print(pdf_text.split("\n").index("1第一个租"))
    # print(pdf_text.split("\n")[399]+pdf_text.split("\n")[400]+pdf_text.split("\n")[401]+pdf_text.split("\n")[402]+pdf_text.split("\n")[403]+pdf_text.split("\n")[404]+pdf_text.split("\n")[405])
    # print(pdf_text.split("\n")[406]+pdf_text.split("\n")[407]+pdf_text.split("\n")[408]+pdf_text.split("\n")[409]+pdf_text.split("\n")[410]+pdf_text.split("\n")[411]+pdf_text.split("\n")[412])
    # print(pdf_text.split("\n")[413]+pdf_text.split("\n")[414]+pdf_text.split("\n")[415]+pdf_text.split("\n")[416]+pdf_text.split("\n")[417]+pdf_text.split("\n")[418]+pdf_text.split("\n")[419])
    # print(pdf_text.split("\n")[420][3:].strip())
    # print(pdf_text.split("\n")[426].strip())
    # print(pdf_text.split("\n")[427].strip())
    # print(pdf_text.split("\n")[428].strip())
    # print(pdf_text.split("\n")[429].strip())
    # print(pdf_text.split("\n")[430].strip())
    # print(pdf_text.split("\n")[431].strip())
    # print(pdf_text.split("\n")[432].strip())
    # print(pdf_text.split("\n")[433].strip())
    # print(pdf_text.split("\n")[434].strip())
    # print(pdf_text.split("\n")[435].strip())
    # print(pdf_text.split("\n")[436].strip())
    # print(pdf_text.split("\n")[437].strip())
    # print(pdf_text.split("\n")[439][13:24])
    # print(pdf_text.split("\n")[443][24:32])

    assert pdf_text.split("\n")[4][3:] == pay_main_no                     # 首页编号
    assert pdf_text.split("\n")[-14][6:32] == pay_main_no                 # 尾页编号
    assert pdf_text.split("\n")[13][3:] == "cm18616005900@163.com"        # 甲方邮箱
    assert pdf_text.split("\n")[14][-10:] == "测试Z500公司J2"               # 乙方（承租人）
    assert pdf_text.split("\n")[15][3:] == "北京市市辖区东城区上海"           # 乙方住所
    assert pdf_text.split("\n")[16][6:] == "季晓伟"                      # 乙方法定代表人
    assert pdf_text.split("\n")[17][3:] == "123@163.com"              # 乙方邮箱
    assert pdf_text.split("\n")[18][3:] == "15705101126"              # 乙方电话
    assert pdf_text.split("\n")[20][-32:-3] == pay_main_no + "-GM"    # 买卖合同/转让协议的合同编号
    assert pdf_text.split("\n")[22][25:35] == "154,000.00"            # 设备购买价款
    assert pdf_text.split("\n")[22][40:48] == "壹拾伍万肆仟元整"      # 设备购买价款大写
    assert pdf_text.split("\n")[23][3:13] == "138,600.00"         # 首付款
    assert pdf_text.split("\n")[23][18:28] == "壹拾叁万捌仟陆佰元整"    # 首付款大写
    assert pdf_text.split("\n")[25][21:23] == "12"                # 租赁期限
    assert pdf_text.split("\n")[26][12:14] == "12"                # 租金支付期数
    assert pdf_text.split("\n")[27][11:15] == "每月一次"          #租金支付周期
    assert pdf_text.split("\n")[30][17:26] == "16,632.00"         #租金总额
    assert pdf_text.split("\n")[30][31:42] == "壹万陆仟陆佰叁拾贰元整"       #租金总额大写
    assert pdf_text.split("\n")[32][:1] == "☒"          #租金偿还方式
    assert pdf_text.split("\n")[39][4:19] == "中国民生银行北京望京科技园支行"    #开户行
    assert pdf_text.split("\n")[41][6:15] == "633917033"            #银行账号
    assert pdf_text.split("\n")[43][10:16] == "300.00"            #首期租金
    assert pdf_text.split("\n")[43][21:25] == "叁佰元整"            #首期租金大写
    assert pdf_text.split("\n")[44][11:21] == "138,600.00"         #首付款
    assert pdf_text.split("\n")[44][26:36] == "壹拾叁万捌仟陆佰元整"   #首付款大写
    assert pdf_text.split("\n")[47][9:13] == "0.00"                #保证金金额
    assert pdf_text.split("\n")[47][18:19] == "零"                   #保证金金额大写
    assert pdf_text.split("\n")[55][:7] == "自然人保证：/"           #自然人保证
    assert pdf_text.split("\n")[56][:6] == "法人保证：/"             #法人保证
    assert pdf_text.split("\n")[57][:4] == "回购：/"                #回购
    assert pdf_text.split("\n")[58][3:14].strip() == "测试Z500公司J2、" # 抵押人、抵押合同编号、抵押物详见《抵押合同》附件一抵押财产清单
    assert pdf_text.split("\n")[58][14:43].strip() == pay_main_no + '-DY'
    assert pdf_text.split("\n")[58][44:].strip() == "抵押物详见《抵押合同》附件一抵押财产清单"
    assert pdf_text.split("\n")[59][:].strip() == "质押：/"        #质押
    assert pdf_text.split("\n")[65][11:14] == "20%"               #全部剩余利息的比例
    assert pdf_text.split("\n")[399]+pdf_text.split("\n")[400]+pdf_text.split("\n")[401]+pdf_text.split("\n")[402]+pdf_text.split("\n")[403]+pdf_text.split("\n")[404]+pdf_text.split("\n")[405] == "1第一个租赁物1 123 11000.00 11000.00测试Z500品牌三级测试Z500供应商合同公司J3北京市市辖区东城区上海"
    assert pdf_text.split("\n")[406]+pdf_text.split("\n")[407]+pdf_text.split("\n")[408]+pdf_text.split("\n")[409]+pdf_text.split("\n")[410]+pdf_text.split("\n")[411]+pdf_text.split("\n")[412] == "2第二个租赁物2 456 22000.00 44000.00测试Z500品牌三级测试Z500供应商合同公司J3北京市市辖区东城区上海"
    assert pdf_text.split("\n")[413]+pdf_text.split("\n")[414]+pdf_text.split("\n")[415]+pdf_text.split("\n")[416]+pdf_text.split("\n")[417]+pdf_text.split("\n")[418]+pdf_text.split("\n")[419] == "3第三个租赁物3 789 33000.00 99000.00测试Z500品牌三级测试Z500供应商合同公司J3北京市市辖区东城区上海"
    assert pdf_text.split("\n")[420][3:].strip() == "壹拾伍万肆仟元整"    #合计
    assert pdf_text.split("\n")[426].strip() == "第1期 1386.00"
    assert pdf_text.split("\n")[427].strip() == "第2期 1386.00"
    assert pdf_text.split("\n")[428].strip() == "第3期 1386.00"
    assert pdf_text.split("\n")[429].strip() == "第4期 1386.00"
    assert pdf_text.split("\n")[430].strip() == "第5期 1386.00"
    assert pdf_text.split("\n")[431].strip() == "第6期 1386.00"
    assert pdf_text.split("\n")[432].strip() == "第7期 1386.00"
    assert pdf_text.split("\n")[433].strip() == "第8期 1386.00"
    assert pdf_text.split("\n")[434].strip() == "第9期 1386.00"
    assert pdf_text.split("\n")[435].strip() == "第10期 1386.00"
    assert pdf_text.split("\n")[436].strip() == "第11期 1386.00"
    assert pdf_text.split("\n")[437].strip() == "第12期 1386.00"
    assert pdf_text.split("\n")[439][13:24] == "1,352.57BPs"   #租赁利率
    assert pdf_text.split("\n")[443][24:32] == "25.4695%"      #年化内部收益率


    print(pdf_text.split("\n"))

def checkPayment(pay_main_no):
    '''首付款确认函'''
    pdf_text = getPdfText('首付款确认函.pdf')

    # print(pdf_text.split("\n")[2][4:30])
    # print(pdf_text.split("\n")[3][7:36])
    # print(pdf_text.split("\n")[3][51:52])
    # print(pdf_text.split("\n")[4][38:]+pdf_text.split("\n")[5][:4])
    # print(pdf_text.split("\n")[5][17:32])
    # print(pdf_text.split("\n")[6][5:15])
    # print(pdf_text.split("\n")[6][23:33])
    # print(pdf_text.split("\n")[19][9:])
    # print(pdf_text.split("\n")[25][4:])
    # print(pdf_text.split("\n").index("出卖人∶测试Z500供应商合同公司J3"))
    print(pdf_text)


    assert pdf_text.split("\n")[2][4:30] == pay_main_no                     # 融资租赁合同编号
    assert pdf_text.split("\n")[3][7:36] == pay_main_no + '-GM'           #买卖合同编号
    assert pdf_text.split("\n")[3][51:52] == "☒"                  #买卖合同类型
    assert pdf_text.split("\n")[4][38:]+pdf_text.split("\n")[5][:4] == "测试Z500公司J2"   #承租人
    assert pdf_text.split("\n")[5][17:32] == "测试Z500供应商合同公司J3"        #出卖人
    assert pdf_text.split("\n")[6][5:15] == "138,600.00"                      #首付款金额
    assert pdf_text.split("\n")[6][23:33] == "壹拾叁万捌仟陆佰元整"                #首付款金额-大写
    assert pdf_text.split("\n")[19][9:] == "测试Z500公司J2"                     #承租人
    assert pdf_text.split("\n")[25][4:] == "测试Z500供应商合同公司J3"                #出卖人

def checkDiscount(pay_main_no):
    '''贴息确认函'''
    pdf_text = getPdfText('贴息确认函.pdf')

    # print(pdf_text.split("\n")[1][55:])
    # print(pdf_text.split("\n")[3][2:])
    # print(pdf_text.split("\n")[5][25:35])
    # print(pdf_text.split("\n")[6][1:27])
    # print(pdf_text.split("\n")[7][16:45])
    # print(pdf_text.split("\n")[9][18:47])
    # print(pdf_text.split("\n")[12][2:8])
    # print(pdf_text.split("\n")[12][13:17])
    # print(pdf_text.split("\n")[16][-12:])
    # print(pdf_text.split("\n")[22][32:58])
    # print(pdf_text.split("\n")[23][32:61])
    # print(pdf_text.split("\n")[26][-15:])



    print(pdf_text)

    assert pdf_text.split("\n")[1][55:] == pay_main_no + '-TXQRH'         #首页编号
    assert pdf_text.split("\n")[3][2:] == "测试Z500供应商合同公司J3"         #供应商
    assert pdf_text.split("\n")[5][25:35] == "测试Z500公司J2"             #承租人
    assert pdf_text.split("\n")[6][1:27] == pay_main_no                  #融资租赁合同编号
    assert pdf_text.split("\n")[7][16:45] == pay_main_no + "-GM"          #买卖合同编号
    assert pdf_text.split("\n")[9][18:47] == pay_main_no + "-TX"          #融资租赁合同之补充协议
    assert pdf_text.split("\n")[12][2:8] == "200.00"                      #贴息款金额-小写
    assert pdf_text.split("\n")[12][13:17] == "贰佰元整"                     #贴息款金额-大写
    assert pdf_text.split("\n")[16][-12:] == "民生金融租赁股份有限公司"         #出租人
    assert pdf_text.split("\n")[22][32:58]== pay_main_no                   #融资租赁合同编号
    assert pdf_text.split("\n")[23][32:61] == pay_main_no + "-TX"          #融资租赁合同之补充协议
    assert pdf_text.split("\n")[26][-15:] == "测试Z500供应商合同公司J3"       #确认人

def checkRisk():
    '''风险告知书'''
    pdf_text = getPdfText('风险告知书.pdf')

    # print(pdf_text.split("\n")[1][2:12])
    print(pdf_text)

    assert pdf_text.split("\n")[1][2:12] == "测试Z500公司J2"           #承租人

def checkDiscount(pay_main_no):
    '''厂商贴息合同'''
    pdf_text = getPdfText('厂商贴息合同.pdf')

    # print(pdf_text.split("\n")[1][4:])
    # print(pdf_text.split("\n")[-17][4:33])
    # print(pdf_text.split("\n")[9][13:])
    # print(pdf_text.split("\n")[10][6:])
    # print(pdf_text.split("\n")[11][4:])
    # print(pdf_text.split("\n")[12][17:])
    # print(pdf_text.split("\n")[13][6:])
    # print(pdf_text.split("\n")[14][4:])
    # print(pdf_text.split("\n")[17][12:38])
    # print(pdf_text.split("\n")[30][2:8])
    # print(pdf_text.split("\n")[30][16:20])
    # print(pdf_text.split("\n")[30][35:]+pdf_text.split("\n")[31][:5])
    # print(pdf_text.split("\n")[31][41:]+pdf_text.split("\n")[32][:27])
    # print(pdf_text.split("\n")[39][14:40])
    # print(pdf_text.split("\n")[40][16:45])
    # print(pdf_text.split("\n")[42][8:40])
    # print(pdf_text.split("\n")[47][5:])
    # print(pdf_text.split("\n")[48][6:])
    # print(pdf_text.split("\n")[51][3:])
    # print(pdf_text.split("\n")[52][7:])
    # print(pdf_text.split("\n")[53][3:])
    # print(pdf_text.split("\n")[54][3:])
    # print(pdf_text.split("\n")[55][4:])
    print(pdf_text.split("\n")[56][3:])


    print(pdf_text)

    assert pdf_text.split("\n")[1][4:] == pay_main_no + "-TX"        # 首页编号
    assert pdf_text.split("\n")[-17][4:33] == pay_main_no + "-TX"   #尾页编号
    assert pdf_text.split("\n")[9][13:] == "测试Z500公司J2"            #承租人（以下称“乙方”）
    assert pdf_text.split("\n")[10][6:] == "季晓伟"                    #承租人法定代表人
    assert pdf_text.split("\n")[11][4:] == "北京市市辖区东城区上海"        #承租人住所地
    assert pdf_text.split("\n")[12][17:] == "测试Z500供应商合同公司J3"      #出卖人/供应商（以下称“丙方”）
    assert pdf_text.split("\n")[13][6:] == "季晓伟"                    #供应商法定代表人
    assert pdf_text.split("\n")[14][4:] == "天津市市辖区河东区测试"        #供应商住所地
    assert pdf_text.split("\n")[17][12:38] == pay_main_no              #编号
    assert pdf_text.split("\n")[30][2:8] == "200.00"                   #贴息款金额
    assert pdf_text.split("\n")[30][16:20] == "贰佰元整"                #贴息款金额-大写
    assert pdf_text.split("\n")[30][35:]+pdf_text.split("\n")[31][:5] == pay_main_no + "-TXQRH"       #贴息款确认函编号
    assert pdf_text.split("\n")[31][41:]+pdf_text.split("\n")[32][:27] == pay_main_no + "-TXQRH"       #贴息款确认函编号
    assert pdf_text.split("\n")[39][14:40] == pay_main_no                     #融资租赁合同编号
    assert pdf_text.split("\n")[40][16:45] == pay_main_no + '-GM'             #买卖合同编号
    assert pdf_text.split("\n")[42][8:40] == pay_main_no + '-TXQRH'           #贴息款确认函编号
    assert pdf_text.split("\n")[47][5:] == "中国民生银行北京望京科技园支行"         #贴息款支付账号-开户行
    assert pdf_text.split("\n")[48][6:] == "633917033"                        #贴息款支付账号-账号
    assert pdf_text.split("\n")[51][3:] == "测试Z500供应商合同公司J3"            #丙方开票信息-名称
    assert pdf_text.split("\n")[52][7:] == "91330100ANTABEFN09"               #丙方开票信息-纳税人识别号
    assert pdf_text.split("\n")[53][3:] == "开票信息地址"                      #丙方开票信息-地址
    assert pdf_text.split("\n")[54][3:] == "15700000000"                     #丙方开票信息-电话
    assert pdf_text.split("\n")[55][4:] == "中国银行股份有限公司长乐支行"         #丙方开票信息-开户行
    assert pdf_text.split("\n")[56][3:] == "321321321"                      #丙方开票信息-账号












def getPdfText(pdf):
    pdf_file = open(pdf, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # 获取pdf页面数量
    # page_count = pdf_reader.getNumPages()

    # 定义空字符串变量，用于存储每一页的文本信息
    pdf_text = ""

    # 遍历每一个页面，进行文本提取
    for i in range(len(pdf_reader.pages)):
        # 获取pdf页面对象
        page = pdf_reader.pages[i]
        # 提取文本信息
        pdf_text += page.extract_text()
    return pdf_text

# def check



if __name__ == "__main__":

    pay_main_no = 'MSFL-2023-10-0087-Z-001-PH'
    # checkFinanceLease(pay_main_no)
    # checkPayment(pay_main_no)
    # checkDiscount(pay_main_no)
    # checkRisk()
    checkDiscount(pay_main_no)
