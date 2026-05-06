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


class NetflixIdParseError(NetflixError):
	pass


class InvalidProfileError(NetflixError):
	pass


class NetflixUnsupportedContentError(NetflixError):
	pass
