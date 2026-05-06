class NetflixError(Exception):
	pass


class NetflixCookieError(NetflixError):
	pass


class NetflixCookieExpiredError(NetflixCookieError):
	def __init__(self, message, cookies_file=None):
		super().__init__(message)
		self.cookies_file = cookies_file


class NetflixRegionError(NetflixError):
	pass


class NetflixApiError(NetflixError):
	def __init__(self, message, status_code=None):
		super().__init__(message)
		self.status_code = status_code


class NetflixIdParseError(NetflixError):
	pass


class InvalidProfileError(NetflixError):
	pass


class NetflixUnsupportedContentError(NetflixError):
	pass
