import pytest

from utils.common import get_redis, get_mysql
from api.http_client_ops import TrainingCampService, eduOpsService
from utils.common import get_redis, get_mysql
from api.http_client_ops import HttpClientOps, XmkpPmsAdvertisementService
import pytest
import time
from attrdict.dictionary import AttrDict


@pytest.fixture(scope="session", autouse=True)
def trainingCamp_cli():
    yield TrainingCampService()


@pytest.fixture(scope="session", autouse=True)
def eduOps_cli():
    yield eduOpsService()


@pytest.fixture(scope="session", autouse=True)
def mysql_cli():
    yield get_mysql()


@pytest.fixture(scope="function")
def new_semester(trainingCamp_cli, eduOps_cli, data, setupdata):
    """
    新建学期 &&删除学期
    """
    semester_id = trainingCamp_cli.new_semester(req_json=data["req_new_semester"],
                                                mobile=setupdata["mobile"], password=setupdata["password"])["id"]
    yield semester_id
    eduOps_cli.del_semester(semesterId=str(semester_id),mobile=setupdata["mobile"], password=setupdata["password"])


@pytest.fixture(scope="function")
def new_class(trainingCamp_cli, new_semester, data, eduOps_cli, setupdata):
    """
    新建班级
    """
    semester_id = new_semester
    res = trainingCamp_cli.new_class(req_json=data["req_new_class"], semesterId=str(semester_id),
                                     mobile=setupdata["mobile"], password=setupdata["password"])
    class_id = res["id"]
    yield class_id, semester_id
    eduOps_cli.del_class(semesterId=str(semester_id), classId=str(class_id),
                         mobile=setupdata["mobile"], password=setupdata["password"])


@pytest.fixture(scope="function")
def del_semester(eduOps_cli, semester_id,setupdata):
    """
    删除学期
    """
    eduOps_cli.del_semester(semesterId=str(semester_id),
                            mobile=setupdata["mobile"], password=setupdata["password"])


@pytest.fixture(scope="function")
def del_class(eduOps_cli, setupdata):
    """
    删除班级
    """
    semester_id = []
    class_id = []
    yield semester_id, class_id
    eduOps_cli.del_class(semesterId=str(semester_id[0]), classId=str(class_id[0])
                         , mobile=setupdata["mobile"], password=setupdata["password"])


@pytest.fixture(scope="function")
def get_classList(eduOps_cli, new_semester,setupdata):
    """
    获取学期下的班级列表
    """
    semester_Id = new_semester
    res = eduOps_cli.class_list(semesterId=str(semester_Id),
                                mobile=setupdata["mobile"], password=setupdata["password"])
    yield res


@pytest.fixture(scope="session")
def Http_cl():
    yield HttpClientOps()


@pytest.fixture(scope="function")
def new_presalePage(Http_cl, data):
    """
    开启用户分群
    """
    presalePage_new_list = Http_cl.presalePage_new(data.needCallback, data.addTeacherProcess, data.title,
                                                   data.couponRef, data.firstLevelTitle, data.secondLevelTitle,
                                                   data.adFeedType, data.headPicture,
                                                   data.briefIntroPic1, data.briefIntroPic2, data.briefIntroPic3,
                                                   data.briefIntroPic4, data.promotionText,
                                                   data.promotionUnit, data.originalPrice, data.couponTitle,
                                                   data.notBoughtText, data.boughtText, data.canNotBuyText,
                                                   data.isDeleted, data.campRef, data.channel)
    print(presalePage_new_list)
    presaleId = presalePage_new_list["data"]["id"]
    yield presaleId
