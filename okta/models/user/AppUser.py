from datetime import datetime

from okta.models.user.AppLoginCredentials import AppLoginCredentials
from okta.models.user.AppUserProfile import AppUserProfile
from okta.models.Link import Link


class AppUser:

	types = {
		'id': str,
		'status': str,
		'scope': str,
		'created': datetime,
		'statusChanged': datetime,
		'lastUpdated': datetime,
		'profile': AppUserProfile,
		'credentials': AppLoginCredentials
	}

	dict_types = {
		'_links': Link
	}

	alt_names = {
		'_links': 'links'
	}

	def __init__(self, **kwargs):

		# unique key for user
		self.id = None  # str

		# current status of user
		self.status = None  # str

		# current scope of user
		self.scope = None  # str
		
		# timestamp when user was created
		self.created = None  # datetime

		# timestamp when status last changed
		self.statusChanged = None  # datetime

		# timestamp when user was last updated
		self.lastUpdated = None  # datetime

		self.profile = None  # UserProfile

		self.credentials = None  # LoginCredentials

		self.links = None

		# Populate profile
		profile_attrs = ['login', 'email', 'secondEmail', 'firstName', 'lastName', 'mobilePhone']
		for attr in profile_attrs:
			if attr in kwargs:
				self.profile = self.profile or UserProfile()
				setattr(self.profile, attr, kwargs[attr])