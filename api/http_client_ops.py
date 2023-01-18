# -*- coding: utf-8 -*-

from utils.http.helper import get_ops, put_ops, patch_ops, delete_ops, post_ops
from utils.http import BaseClient


class HttpClientOps(BaseClient):
    @get_ops("/eduOps/api/v1/camp/businessType/1")
    def camp_businesstype_one(self, timeStamp,mobile, password):
        """
        牛津树训练营列表
        """

    @get_ops("/eduOps/api/v1/camp/businessType/2")
    def camp_businesstype_two(self, timeStamp,mobile, password):
        """
        通用训练营列表
        """

    @get_ops("/eduOps/api/v1/camp/businessType/4")
    def camp_businesstype_four(self, timeStamp,mobile, password):
        """
        书虫训练营列表
        """

    @get_ops("/eduOps/api/v1/camp/businessType/6")
    def camp_businesstype_six(self, timeStamp,mobile, password):
        """
        自然拼读训练营列表
        """

    @get_ops("/eduOps/api/v1/camp/businessType/8")
    def camp_businesstype_eight(self, timeStamp,mobile, password):
        """
        何秋光数学训练营列表
        """

    @get_ops("/eduOps/api/v1/camp/businessType/9")
    def camp_businesstype_nine(self, timeStamp,mobile, password):
        """
        亲子儿童训练营列表
        """

    @get_ops("/eduOps/api/v1/camp/businessType/10")
    def camp_businesstype_ten(self, timeStamp,mobile, password):
        """
        喜马大学训练营列表
        """

    @get_ops("/eduOps/api/v1/camp/businessType/11")
    def camp_businesstype_eleven(self, timeStamp,mobile, password):
        """
        新概念训练营列表
        """

    @get_ops("/eduOps/api/v1/camp/23/lesson")
    def camp_lesson(self, timeStamp,mobile, password):
        """
        获取训练营id=23下所有课程列表
        """

    @get_ops("/eduOps/api/v1/camp/35/presale")
    def camp_presale(self, timeStamp,mobile, password):
        """
        获取售前页列表-老
        """

    @get_ops("/eduOps/api/v1/camp/21/semester/search")
    def camp_semester(self, timeStamp, index, size, campId,mobile, password):
        """
        获取所有训练营下的学期
        """

    @get_ops("/eduOps/api/v1/semester/595/class/search")
    def camp_class(self, timeStamp, page, pageSize, sum, numCondition,mobile, password):
        """
        按照班级ID查询班级
        """

    @get_ops("/eduOps/dev/memberInClass/1093/search")
    def camp_member_in_class(self, timeStamp, index, size, numCondition,mobile, password):
        """
        获取学员列表
        """

    @get_ops("/eduOps/api/v1/21/presalePages/new")
    def camp_presale_pages_one(self, timeStamp, currentPage, pageSize,mobile, password):
        """
        获取campID=21下面新售前页列表
        """

    @get_ops("/eduOps/api/v1/0/presalePages/new")
    def camp_presale_pages_two(self, timeStamp, currentPage, pageSize,mobile, password):
        """
        获取campID=0（不存在的campID）下面新售前页列表
        """

    @get_ops("/eduOps/api/v1/presalePage/384/new")
    def camp_presalepage_one(self, timeStamp,mobile, password):
        """
        获取新售前页为384的详情
        """

    @get_ops("/eduOps/api/v1/presalePage/0/new")
    def camp_presalepage_two(self, timeStamp,mobile, password):
        """
        获取新售前页为不存在的详情
        """

    # @get_ops("/eduOps/api/v1/class/permission/classes")
    # def class_permission_classes(self, timeStamp, page, pageSize, teacherNameOrClassName, classId, departmentId,mobile, password):
    #     """
    #     获取班级信息
    #     """

    @get_ops("/eduOps/api/v1/class/departments")
    def class_departments(self, timeStamp,mobile, password):
        """
        获取部门信息
        """

    @get_ops("/eduOps/api/v1/teacher/permission")
    def teacher_permission(self, timeStamp,mobile, password):
        """
        获取用户权限
        """

    @get_ops("/eduOps/api/v1/teacher/teacherList")
    def teacher_list(self, timeStamp, pageSize, page,mobile, password):
        """
        获取老师列表
        """

    @get_ops("/eduOps/api/v1/teacher/1109")
    def teacher_id_list(self, timeStamp,mobile, password):
        """
        获取老师信息详情
        """

    @get_ops("/eduOps/api/v1/groupRecall/semesterList")
    def grouprecall_semester_list(self, timeStamp, pageSize, page, semesterId,mobile, password ):
        """
        获取用户召回列表
        """

    @get_ops("/eduOps/api/v1/groupRecall/538/classMateList")
    def grouprecall_Classmate_list(self, timeStamp, pageSize, page, status,mobile, password):
        """
        获取召回班列表
        """

    @get_ops("/eduOps/api/v1/groupRecall/getPhone")
    def grouprecall_getphone(self, timeStamp, studentId,mobile, password):
        """
        获取召回学员手机号
        """

    @get_ops("/eduOps/api/v1/user/groupCode")
    def user_groupcode(self, timeStamp, param,mobile, password):
        """
        获取学员信息
        """

    @get_ops("/eduOps/api/v1/ortstatistic/user/study")
    def user_study(self, timeStamp, userId, classRef,mobile, password):
        """
        获取学员学习数据
        """

    @get_ops("/eduOps/api/v1/user/89/307923")
    def user_detail_info(self, timeStamp,mobile, password):
        """
        获取学员详细信息
        """

    @get_ops("/eduOps/api/v1/ortstatistic/class/campus")
    def class_campus_type(self, timeStamp, classRef,mobile, password):
        """
        获取班级所属训练营类型
        """

    @get_ops("/eduOps/api/v1/class/220")
    def class_is_available_YES(self, timeStamp,mobile, password):
        """
        获取班级是否可用_YES
        """

    @get_ops("/eduOps/api/v1/class/0")
    def class_is_available_NO(self, timeStamp,mobile, password):
        """
        获取班级是否可用_NO
        """

    @get_ops("/eduOps/dev/queryUserInfo/347184")
    def query_user_info_is_exist(self,mobile, password):
        """
        添加学员时查询学员存在
        """

    @get_ops("/eduOps/dev/queryUserInfo/00000")
    def query_user_info_is_not_exist(self,mobile, password):
        """
        添加学员时查询学员不存在
        """

    @get_ops("/eduOps/api/v1/semester/0/class/1093")
    def query_class_info_is_exist(self,mobile, password):
        """
        调整学员班级时查询班级可用
        """

    @get_ops("/eduOps/api/v1/semester/0/class/0000")
    def query_class_info_is_not_exist(self,mobile, password):
        """
        调整学员班级时查询班级不可用
        """

    @get_ops("/eduOps/dev/addUserToClass/347184/69508")
    def add_user_to_class(self, timeStamp,mobile, password):
        """
        添加学员
        """

    @get_ops("/eduOps/dev/addUserToClass/347184/1093")
    def add_user_to_class_same(self, timeStamp,mobile, password):
        """
        添加学员是学员为同期学员
        """

    @get_ops("/eduOps/dev/addUserToClass/347184/878")
    def add_user_to_class_different_same(self, timeStamp,mobile, password):
        """
        添加学员是学员为同canp不同期学员
        """

    @get_ops("/eduOps/dev/addUserToClass/347184/69220")
    def add_user_to_class_different_camp(self, timeStamp,mobile, password):
        """
        添加学员是学员为不同canp学员同business_type
        """

    @get_ops("/eduOps/dev/addUserToClass/347184/70065")
    def add_class_different_business_type(self, timeStamp,mobile, password):
        """
        添加学员是学员为不同business_type学员
        """

    @get_ops("/eduOps/dev/change/347184/semester/595/to/69508")
    def change_user_to_new_class(self, timeStamp,mobile, password):
        """
        学员调班
        """

    @get_ops("/eduOps/dev/change/347184/semester/595/to/1210")
    def change_user_to_new_class_1210(self, timeStamp,mobile, password):
        """
        学员调班
        """

    @get_ops("/eduOps/dev/change/347184/semester/536/to/878")
    def change_user_to_new_class_different_semester(self, timeStamp,mobile, password):
        """
        学员调班
        """

    @get_ops("/eduOps/dev/change/347184/semester/773/to/69220")
    def change_user_to_new_class_different_camp(self, timeStamp,mobile, password):
        """
        学员调班
        """

    @get_ops("/eduOps/api/v1/rebuy/channels")
    def rebuy_channels(self, timeStamp,mobile, password):
        """
        获取订单明细数据的渠道名list
        """

    @get_ops("/eduOps/api/v1/rebuy")
    def rebuy(self, timeStamp, pageSize, page, channel, orderNoOrUserId,mobile, password):
        """
        获取订单明细数据
        """

    @get_ops("/xmkp-middle/middleOps/api/v1/salary/list")
    def salary_list(self, timeStamp, pageSize, page, teacherId, campus,mobile, password):
        """
        获取薪资统计表
        """

    @get_ops("/xmkp-middle/middleOps/api/v1/salary/dropdownlist/list")
    def salary_dropdown_list(self, timeStamp, campus, dropDownListType, teacherId,mobile, password):
        """
        获取薪资统计表的渠道名list
        """

    @post_ops("/eduOps/api/v1/ortstatistic/monthlyClass/users", is_json_req=True)
    def monthly_class_users(self, classId, currentPage, pageSize, searchContent, hasFugou, notDakaDay, studyDay,
                            studyStatus,mobile, password):
        """
        获取月课类型的班级信息
        """

    @post_ops("/eduOps/api/v1/ortReport/study/genClassStudyReport", is_json_req=True)
    def gen_class_study_report(self, classRef, comment,mobile, password):
        """
        生成学习报告
        """

    @post_ops("/eduOps/api/v1/ortReport/rank/genClassDiamondRank", is_json_req=True)
    def gen_class_diamond_rank(self, classRef, beginDate, endDate, opsId,mobile, password):
        """
        生成周榜
        """

    # @post_ops("/eduOps/api/v1/ortstatistic/users/remarks", is_json_req=True)
    # def users_remarks(self, classRef, teacherRemarks, userId, mobile, password):
    #     """
    #     写笔记
    #     """

    @post_ops("/cacsi/pageview/save", is_json_req=False)
    def cacsi_pageview_save(self, menuId,mobile, password):
        """
        获取订单数据中心Tab
        """

    @get_ops("/ort/ai/ops/word")
    def ops_word(self, timeStamp, lessonId,mobile, password):
        """
        关联课程列表
        """

    @post_ops("/eduOps/api/v1/semester/oldOxford", is_json_req=True)
    def semester_oldOxford(self, timeStamp,mobile, password):
        """
        新建学期
        """

    @post_ops("/trainingcamp/ops/semester/semesterid}/class", is_json_req=True)
    def semester_class(self, timeStamp,mobile, password):
        """
        新建班级
        """

    # @post_ops("/eduOps/api/v1/21/presalePage/new", is_json_req=True)
    # def presalePage_new(self, needCallback, addTeacherProcess, title, couponRef, firstLevelTitle, secondLevelTitle,
    #                     adFeedType, headPicture, briefIntroPic1, briefIntroPic2, briefIntroPic3, briefIntroPic4,
    #                     promotionText, promotionUnit, originalPrice, couponTitle, notBoughtText, boughtText,
    #                     canNotBuyText, isDeleted, campRef, channel,mobile, password):
    #     """
    #     新建新售前页
    #     """
    @get_ops("/eduOps/dev/deleteUser/{{uId}}/{{semesterId}}")
    def delete_user(self, timeStamp,mobile, password):
        """
        删除学员
        """

    @put_ops("/eduOps/api/v1/presalePage/{{presaleId}}/new", is_json_req=True)
    def presalePage_edit(self, needCallback, addTeacherProcess, title, couponRef, firstLevelTitle, secondLevelTitle,
                         adFeedType, headPicture, briefIntroPic1, briefIntroPic2, briefIntroPic3, briefIntroPic4,
                         promotionText, promotionUnit, originalPrice, couponTitle, notBoughtText, boughtText,
                         canNotBuyText, isDeleted, campRef, channel, mobile, password,**kwargs):
        """
        编辑售前页
        """

    @delete_ops("/eduOps/api/v1/presalePage/{{presaleId}}/new", is_json_req=True)
    def presalePage_delete(self, mobile, password,**kwargs):
        """
        删除售前页
        """

class XmkpPmsUsergroupWebService(BaseClient):
    """
    用户分群web服务
    """

    @post_ops("/xmkp-pms-usergroup-web/userGroup/ops/group", is_json_req=True)
    def new_userGroup(self, business, groupName, rule,mobile,password):
        """
        新建用户分群
        """

    @put_ops("/xmkp-pms-usergroup-web/userGroup/ops/enable/{{groupId}}")
    def enable_userGroup(self, mobile,password,**kwargs):
        """
        启用用户分群
        """

    @put_ops("/xmkp-pms-usergroup-web/userGroup/ops/disable/{{groupId}}")
    def disable_userGroup(self,mobile,password, **kwargs):
        """
        关闭用户分群
        """

    @get_ops("/xmkp-pms-usergroup-web/userGroup/ops/label")
    def get_userGroup_label(self,mobile,password):
        """
        查询所有标签规则
        """

    @get_ops("/xmkp-pms-usergroup-web/userGroup/ops/{{groupId}}")
    def get_userGroup_detail(self,mobile,password, **kwargs):
        """
        查询分群规则详情
        """

    @get_ops("/xmkp-pms-usergroup-web/userGroup/ops/page?current={{current}}&pageSize={{pageSize}}&pageNum={{pageNum}}")
    def get_userGroup_by_page(self,mobile,password, **kwargs):
        """
        分页查询用户分群
        """


class TrainingCampService(BaseClient):
    """
    TrainingCamp 服务模块
    """

    @post_ops("/trainingcamp/ops/semester/{{semesterId}}/class", is_json_req=True)
    def new_class(self,mobile, password, **kwargs):
        """
        新建班级
        """

    @post_ops("/trainingcamp/ops/semester", is_json_req=True)
    def new_semester(self, mobile, password,**kwargs):
        """
        新建学期
        """

    @patch_ops("/trainingcamp/ops/semester/{{semesterId}}/class/{{classId}}", is_json_req=True)
    def edit_classInfo(self, mobile, password,**kwargs,):
        """
        编辑班级信息
        """




class eduOpsService(BaseClient):
    """
    eduOps服务
    """

    @delete_ops("/eduOps/api/v1/semester/{{semesterId}}")
    def del_semester(self,mobile, password, **kwargs):
        """
        删除学期
        args:semesterId:学期ID
        """

    @delete_ops("/eduOps/api/v1/semester/{{semesterId}}/class/{{classId}}")
    def del_class(self, mobile, password,**kwargs):
        """
        删除班级
        """

    @patch_ops('/eduOps/api/v1/semester/class/move?classId={{classId}}&operationId={{operationId}}')
    def move_class(self, mobile, password,**kwargs):
        """
        班级上移/下移 operationId ：1为下移-1上移
        """

    @get_ops('/eduOps/api/v1/semester/{{semesterId}}/class/search')
    def class_list(self, mobile, password,**kwargs):
        """
        班级列表
        """

    @patch_ops("/eduOps/api/v1/semester/ai-switch?semesterId={{semesterId}}", is_json_req=True)
    def enable_voiceComments(self, mobile, password,**kwargs):
        """
        开启语音点评
        """
class XmkpPmsAdvertisementService(BaseClient):
    """
    用户投放Service
    """

    @get_ops("/xmkp-pms-ad/adOps/api/v1/userGroup/userGroups")
    def get_available_userGroups(self,mobile, password):
        """
        获取所有可用分群（人群包）
        """

    @get_ops("/xmkp-pms-ad/adOps/api/v1/userGroup/task/export", is_json_req=True)
    def export_encrypted_phoneNumber(self, taskId,mobile, password):
        """
        导出加密手机号
        """

    @delete_ops("/xmkp-pms-ad/adOps/api/v1/userGroup/task/status/{{taskId}}", is_json_req=True)
    def pause_start_task(self, taskStatus,mobile, password, **kwargs):
        """
        暂停/开启投放任务
        """

    @get_ops("/xmkp-pms-ad/adOps/api/v1/userGroup/tasks", is_json_req=True)
    def get_taskList(self, taskName, businessType, taskStatus, page, pageSize,mobile, password):
        """
        获取投放任务列表
        """

    @delete_ops("/xmkp-pms-ad/adOps/api/v1/userGroup/task/{{taskId}}", is_json_req=True)
    def delete_task(self,mobile, password, **kwargs):
        """
        删除投放任务
        """

    @get_ops("/xmkp-pms-ad/adOps/api/v1/userGroup/vendors")
    def get_ad_vendorSet(self,mobile, password):
        """
        获取广告引擎集合
        """

    @get_ops("/xmkp-pms-ad/adOps/api/v1/userGroup/businesses")
    def get_businessSet(self,mobile, password):
        """
        获取业务集合
        """

    @put_ops("/xmkp-pms-ad/adOps/api/v1/userGroup/task", is_json_req=True)
    def edit_task(self, id, taskName, businessType, vendorType, encryptMethod, userGroupId, updateFrequency, remark,mobile, password):
        """
        修改投放任务
        """

    @post_ops("/xmkp-pms-ad/adOps/api/v1/userGroup/task", is_json_req=True)
    def post_task(self, taskName, businessType, vendorType, encryptMethod, userGroupId, updateFrequency, remark,mobile, password):
        """
        新增投放任务
        """

class XmkpPmsAbtestService(BaseClient):
    """
    abtest服务
    """

    @get_ops("/xmkp-pms-abtesting/api/v1/abtestingConfig/get/list/systemNames")
    def get_systemNames_list(self, mobile,password,**kwargs):
        """
        获取所属业务列表
        """

    @get_ops("/xmkp-pms-abtesting/api/v1/abtestingConfig/get/list/businessTypes")
    def get_businessTypes_list(self, mobile, password, **kwargs):
        """
        获取业务类型列表
        """

    @post_ops("/xmkp-pms-abtesting/api/v1/abtestingConfig/add")
    def test_post_add_abtestingConfig(self, mobile, password, **kwargs):
        """
        新增实验配置
        """

    @get_ops("/xmkp-pms-abtesting/api/v1/get/abtesting")
    def get_abtesting_list(self, mobile, password,page,pageSize,status):
        """
        条件筛选实验
        """