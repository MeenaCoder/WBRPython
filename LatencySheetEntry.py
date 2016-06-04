
#APP_ID,APP_NAME,BADGE_KEY,BADGE_VALUE,START_DATE,LATENCY,END_DATE
class LatencySheetEntry(object):
	def __init__(self, appId, appName, badgeKey, badgeValue, startDate, latency, endDate ):
		self._appId = appId
		self._appName = appName
		self._badgeKey = badgeKey
		self._badgeValue = badgeValue
		self._startDate = startDate
		self._latency = latency
		self._endDate = endDate


	@property
	def appId(self):
		return self._appId

	@appId.setter
	def appId(self, appId):
		self._appId = appId


	@property
	def appName(self):
		return self._appName

	@appName.setter
	def appName(self, appName):
		self._appName = appName


	@property
	def badgeKey(self):
		return self._badgeKey

	@badgeKey.setter
	def badgeKey(self, badgeKey):
		self._badgeKey = badgeKey


	@property
	def badgeValue(self):
		return self._badgeValue

	@badgeValue.setter
	def badgeValue(self, badgeValue):
		self._badgeValue = badgeValue


	@property
	def startDate(self):
		return self._startDate

	@startDate.setter
	def startDate(self, startDate):
		self._startDate = startDate


	@property
	def latency(self):
		return self._latency

	@latency.setter
	def latency(self, latency):
		self._latency = latency


	@property
	def endDate(self):
		return self._endDate

	@endDate.setter
	def endDate(self, endDate):
		self._endDate = endDate
		
		
		
	# Print object	
	def toString(self):
		return "Latency Sheet Entry [ AppId: " +self.appId +
		", AppName: " + self.appName +
		", StartDate: " + self.startDate +
		", EndDate: " + self.endDate + 
		", Latency: " + self.latency + " ]"
		
		
	