import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkrds.request.v20140815 import DescribeDBInstancesRequest
from aliyunsdkrds.request.v20140815 import DescribeDBInstanceAttributeRequest
from aliyunsdkcorev3.clientv3 import AcsClient as AcsClientv3
from aliyunsdkcorev3.request import CommonRequest
from flask import current_app

class datainfo():
	def __init__(self):
		self.types = ['sharding', 'replicate']
		self.DBid = []
		self.DBinfo = []
		self.redis = []
		self.mogo = []

	def query_mysql(self):
		try:
			for zone in current_app.config['ALIYUN_ZONE']:
				client = AcsClient(current_app.config['ALIYUN_ACCESS_KEYID'], current_app.config['ALIYUN_ACCESS_KEY_SECRET'], zone)
				request = DescribeDBInstancesRequest.DescribeDBInstancesRequest()
				request.set_accept_format('json')
				response = json.loads(client.do_action_with_exception(request))
				self.DBid.append(response['Items']['DBInstance'])
		except Exception as e:
			raise e
		for zone in current_app.config['ALIYUN_ZONE']:
			client = AcsClient(current_app.config['ALIYUN_ACCESS_KEYID'], current_app.config['ALIYUN_ACCESS_KEY_SECRET'],zone)
			for ids in sum(self.DBid, []):
				request = DescribeDBInstanceAttributeRequest.DescribeDBInstanceAttributeRequest()
				request.set_accept_format('json')
				request.set_DBInstanceId(ids['DBInstanceId'])
				response = json.loads(client.do_action_with_exception(request))
				self.DBinfo.append(response['Items']['DBInstanceAttribute'])
			return self.DBinfo
	#
	# def query_redis(self):
	# 	for zone in current_app.config['ALIYUN_ZONE']:
	# 		client  = AcsClientv3(current_app.config['ALIYUN_ACCESS_KEYID'], current_app.config['ALIYUN_ACCESS_KEY_SECRET'],zone)
	# 		request = CommonRequest()
	# 		request.set_accept_format('json')
	# 		request.set_domain('r-kvstore.aliyuncs.com')
	# 		request.set_action_name('DescribeInstances')
	# 		request.set_version('2015-01-01')
	# 		response = json.loads(client.do_action_with_exception(request))
	# 		self.redis.append(response['Instances']['KVStoreInstance'])
	# 	return self.DBinfo
	#
	# def query_mogo(self):
	# 	for zone in current_app.config['ALIYUN_ZONE']:
	# 		client  = AcsClientv3(current_app.config['ALIYUN_ACCESS_KEYID'], current_app.config['ALIYUN_ACCESS_KEY_SECRET'],zone)
	# 		for types in self.types:
	# 			request = CommonRequest()
	# 			request.set_accept_format('json')
	# 			request.set_domain('mongodb.aliyuncs.com')
	# 			request.set_action_name('DescribeDBInstances')
	# 			request.set_version('2015-12-01')
	# 			request.add_query_param('DBInstanceType',types)
	# 			response = json.loads(client.do_action_with_exception(request))
	# 			self.mogo.append(response['DBInstances']['DBInstance'])
	# 	return self.DBinfo

