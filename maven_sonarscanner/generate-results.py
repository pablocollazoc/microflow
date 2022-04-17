#!/usr/bin/python

import json
from textwrap import indent

from mdutils.mdutils import MdUtils
from mdutils import Html
from sonarqube import SonarQubeClient

class ResultsGenerator:
    def __init__(self):
        sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", username='admin', password='sonar')
        self.sonar = sonar

    def generate_results(self):

        issues = []

        component = self.sonar.components.get_project_component_and_ancestors("Devops-API")
        project_json = json.dumps(component, indent=2)
        project_json = json.loads(project_json)

        bugs = list(self.sonar.issues.search_issues(componentKeys="Devops-API", types="BUG"))
        bugs_json = json.dumps(bugs, indent=2)
        bugs_json = json.loads(bugs_json)
        issues.append(bugs_json)

        code_smells = list(self.sonar.issues.search_issues(componentKeys="Devops-API", types="CODE_SMELL"))
        code_smells_json = json.dumps(code_smells, indent=2)
        code_smells_json = json.loads(code_smells_json)
        issues.append(code_smells_json)

        vulnerabilities = list(self.sonar.issues.search_issues(componentKeys="Devops-API", types="VULNERABILITY"))
        vulnerabilities_json = json.dumps(vulnerabilities, indent=2)
        vulnerabilities_json = json.loads(vulnerabilities_json)
        issues.append(vulnerabilities_json)

        mdFile = MdUtils(file_name='results_markdown', title='Analysis results for' + project_json["component"]["name"] + 'project')
        mdFile.new_paragraph("This GitHub page shows the analysis results for the requested flow execution for "
                               + project_json["component"]["name"] + "project")

        for y in range(len(issues)):
            if y == 0:
                mdFile.new_header(level=2, title='Bugs found:')
            elif y == 1:
                mdFile.new_header(level=2, title='Code smells found:')
            else:
                mdFile.new_header(level=2, title='Vulnerabilities found:')

            list_of_strings = ["Nº", "Description", "Severity", "Estimated resolution time", "File", "Line"]

            for x in range(len(issues[y])):
                print(issues[y][x])
                if "effort" in issues[y][x].keys():
                    list_of_strings.extend([str(x), issues[y][x]["message"], issues[y][x]["severity"], issues[y][x]["effort"], issues[y][x]["component"], issues[y][x]["line"]])
                else:
                    list_of_strings.extend([str(x), issues[y][x]["message"], issues[y][x]["severity"], "-", issues[y][x]["component"], issues[y][x]["line"]])
            mdFile.new_line()
            mdFile.new_table(columns=6, rows=len(issues[y]) + 1, text=list_of_strings, text_align='center')
        mdFile.create_md_file()

if __name__ == "__main__":
    ResultsGenerator().generate_results()
