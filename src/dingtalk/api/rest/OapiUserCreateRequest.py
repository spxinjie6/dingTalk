'''
Created by auto_sdk on 2021.06.08
'''
from dingtalk.api.base import RestApi
class OapiUserCreateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.department = None
		self.email = None
		self.extattr = None
		self.hiredDate = None
		self.isHide = None
		self.isSenior = None
		self.jobnumber = None
		self.mobile = None
		self.name = None
		self.orderInDepts = None
		self.orgEmail = None
		self.position = None
		self.positionInDepts = None
		self.remark = None
		self.tel = None
		self.userid = None
		self.workPlace = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.user.create'
