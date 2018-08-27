##########################################################
# Developer:Suresh Sakhare
# Language:Python
# Description: This script used to upload the attachments to cloud/server jira.Execute this script from attachment directory.Make sure that all issuekey present on server
##########################################
import commands
import sys,os
userNamePassword = "gadadechhaya28@gmail.com:chhaya5592"
serverBaseUrl = "https://testcloudservicedesk.atlassian.net"
attachmentDirectory = "/home/addteq/Development/Jira_Plugin/ServiceNow/upload"
for path, subdirs, files in os.walk('.'):
	data = path.split("/")
	for i in range(1,len(data)):
		incidentKey = data[i]
		print incidentKey
		for j in range(0,len(files)):
			fileName = files[j]		
			print fileName
			status, output = commands.getstatusoutput("curl -D- -u "+userNamePassword+" -X POST -H 'X-Atlassian-Token: no-check' -F 'file=@"+attachmentDirectory+"/"+incidentKey+"/"+fileName+"' "+serverBaseUrl+"/rest/api/2/issue/"+incidentKey+"/attachments")

print output






