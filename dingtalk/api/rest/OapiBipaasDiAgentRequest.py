'''
Created by auto_sdk on 2021.08.12
'''
from dingtalk.api.base import RestApi
class OapiBipaasDiAgentRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.request = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.bipaas.di.agent'
