'''
Created by auto_sdk on 2019.10.11
'''
from dingtalk.api.base import RestApi
class OapiProcessPrinterTemplateDeleteRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.request = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.process.printer.template.delete'
