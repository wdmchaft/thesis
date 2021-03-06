#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import presentation, live, question
import sitewide_settings

class MainHandler(webapp.RequestHandler):
	def get(self):
		# if sitewide_settings.OPEN_FOR_BUSINESS:
		# 			greeting = 'open'
		# 		else:
		# 			greeting = 'closed'
		# 		self.response.out.write("Hello, we're %s!" % (greeting,))
		import web.all_presentations
		self.redirect(web.all_presentations.AllPresentationsPage.url())


def main():
	handlers = [('/', MainHandler)]
	
	if sitewide_settings.OPEN_FOR_BUSINESS:
		import presentation, live, question, web
		question.append_handlers(handlers)
		presentation.append_handlers(handlers)
		live.append_handlers(handlers)
		web.append_handlers(handlers)
		
	application = webapp.WSGIApplication(handlers,
                                         debug = sitewide_settings.DEBUG)
	util.run_wsgi_app(application)


if __name__ == '__main__':
	main()
