from utils.http import BaseClient
from utils.http.helper import post_rpc


class HttpClientRpc(BaseClient):
    """
    desc:  rpc统一接口,采用http的方式调用
    """

    @post_rpc("/thriftTester/v3/noauth/invoke.htm")
    def invoke_rpc(self, req):
        """
        desc:rpc接口统一URL
        @return:
        """
