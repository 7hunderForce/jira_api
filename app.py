import config
from jira.client import JIRA

#=====================================================================================
# CONFIG
#=====================================================================================

SERVER_NAME = 'https://your-jira-server.com'
SERVER_CERT = r'local path of certificate downloaded from jira server'
OPTIONS = {'server': SERVER_NAME, 'verify': SERVER_CERT}
PROJECT_NAME = 'project name'

#=====================================================================================
# FUNCTIONS
#=====================================================================================

def get_project(project_name):
    jira = JIRA(options=OPTIONS, basic_auth=(config.UID,config.PWD))
    for singleIssue in jira.search_issues(jql_str=f'project={project_name}'):
        output = f'{singleIssue.key}: {singleIssue.fields.summary} [{singleIssue.fields.reporter.displayName}]'
        print(output)

#=====================================================================================
# MAIN
#=====================================================================================

if __name__ == '__main__':
    get_project(PROJECT_NAME)
