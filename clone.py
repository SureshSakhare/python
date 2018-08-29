#!/usr/bin/env python

import stashy, os
stash = stashy.connect("http://sukhbitbucket.addteq.com/bitbucket", "alm", "alm")

projects = stash.projects.list()

for project in projects:
	print project["name"]
	for repo in stash.projects["%s" %(project["key"])].repos.list():
		print repo
		for url in repo["links"]["clone"]:
			# http or ssh
			if (url["name"] == "http"):
				print (url["href"])
				os.system("git clone %s" %(url["href"]))
