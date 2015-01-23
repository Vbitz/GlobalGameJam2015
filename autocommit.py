#!/usr/bin/env python2.7

import time
import subprocess

if __name__ == '__main__':
	while True:
		for i in range(0, 5):
			print "Commiting in %s minutes" % (str(5 - i))
			time.sleep(60)
		print "Commiting Progress"
		commitMessasge = "Process at: %s" % (time.strftime("%c"))
		subprocess.Popen(["git", "commit", "-a", "-m", commitMessasge]).wait()
