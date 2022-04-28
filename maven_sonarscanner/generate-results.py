#!/usr/bin/python

import gviz_api
import json

from textwrap import indent
from mdutils.mdutils import MdUtils
from mdutils import Html
from sonarqube import SonarQubeClient

page_template = """
<html>
  <script src="https://www.gstatic.com/charts/loader.js"></script>
  <script>
    google.charts.load('current', {packages:['corechart']});

    google.charts.setOnLoadCallback(drawTable);
    function drawTable() {
      %(jscode_pieChart)s
      var jscode_table = new google.visualization.PieChart(document.getElementById('table_div_jscode'));
      jscode_table.draw(jscode_data, {is3D: 'true'});

      %(jscode_reliability)s
      var jscode_table = new google.visualization.BubbleChart(document.getElementById('buble_div_jscode'));
      jscode_table.draw(jscode_data_reliability, {title:'- Color: Reliability Rating (1.0 = A, 2.0 = B, 3.0 = C, 4.0 = D, 5.0 = E)   - Size: Bugs', hAxis: {title: 'Lines of code'}, vAxis: {title: 'Remediation effort (in min)'}, colors: ['red', 'orange', 'yellow', 'lime', 'darkgreen']});

      %(jscode_security)s
      var jscode_table = new google.visualization.BubbleChart(document.getElementById('buble_div_jscode_security'));
      jscode_table.draw(jscode_data_security, {title:'- Color: Security Rating (1.0 = A, 2.0 = B, 3.0 = C, 4.0 = D, 5.0 = E)   - Size: Vulnerabilities', hAxis: {title: 'Lines of code'}, vAxis: {title: 'Remediation effort (in min)'}, colors: ['red', 'orange', 'yellow', 'lime', 'darkgreen']});
    }
  </script>
  <body>
    <H1><strong>Issue types distribution:</strong></H1>
    <div id="table_div_jscode" style="width: 800px; height: 400px;"></div>
    <H1><strong>Reliability:</strong></H1>
    <div id="buble_div_jscode" style="width: 800px; height: 400px;"></div>
    <H1><strong>Security:</strong></H1>
    <div id="buble_div_jscode_security" style="width: 800px; height: 400px;"></div>
  </body>
</html>
"""

class ResultsGenerator:
    def __init__(self):
        sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", username='admin', password='sonar')
        self.sonar = sonar

    def generate_results(self):

        issues = []

        component = self.sonar.components.get_project_component_and_ancestors("Devops-API")
        project_json = json.dumps(component, indent=2)
        project_json = json.loads(project_json)

        # Get reliability measure values
        component_tree = list(self.sonar.measures.get_component_tree_with_specified_measures(component="Devops-API",
                                                                                      metricSort="reliability_remediation_effort",
                                                                                      s="metric",
                                                                                      asc="false",
                                                                                      qualifiers="FIL",
                                                                                      metricKeys="bugs,reliability_remediation_effort,reliability_rating,ncloc"))
        reliability = json.dumps(component_tree, indent=2)
        reliability = json.loads(reliability)

        # Get security measure values
        component_tree_security = list(self.sonar.measures.get_component_tree_with_specified_measures(component="Devops-API",
                                                                                      metricSort="security_remediation_effort",
                                                                                      s="metric",
                                                                                      asc="false",
                                                                                      qualifiers="FIL",
                                                                                      metricKeys="vulnerabilities,security_remediation_effort,security_rating,ncloc"))
        security = json.dumps(component_tree_security, indent=2)
        security = json.loads(security)

        # Get quality gate status
        qualitygates_status = self.sonar.qualitygates.get_project_qualitygates_status(projectKey="Devops-API")
        quality_gate_status = json.dumps(qualitygates_status, indent=2)
        quality_gate_status = json.loads(quality_gate_status)

        # Get found bugs
        bugs = list(self.sonar.issues.search_issues(componentKeys="Devops-API", types="BUG"))
        bugs_json = json.dumps(bugs, indent=2)
        bugs_json = json.loads(bugs_json)
        issues.append(bugs_json)

        # Get found code smells
        code_smells = list(self.sonar.issues.search_issues(componentKeys="Devops-API", types="CODE_SMELL"))
        code_smells_json = json.dumps(code_smells, indent=2)
        code_smells_json = json.loads(code_smells_json)
        issues.append(code_smells_json)

        # Get found vulnerabilities
        vulnerabilities = list(self.sonar.issues.search_issues(componentKeys="Devops-API", types="VULNERABILITY"))
        vulnerabilities_json = json.dumps(vulnerabilities, indent=2)
        vulnerabilities_json = json.loads(vulnerabilities_json)
        issues.append(vulnerabilities_json)

        mdFile = MdUtils(file_name='results_markdown', title='Analysis results for ' + project_json["component"]["name"] + ' project')
        mdFile.new_paragraph("This GitHub page shows the analysis results for the requested flow execution for "
                               + project_json["component"]["name"] + "project")

        # QUality Gate result
        mdFile.new_header(1, '**Quality gate status:**')
        if quality_gate_status["projectStatus"]["status"] == "OK":
          mdFile.new_paragraph('***Passed*** :heavy_check_mark:')
          mdFile.new_paragraph("All conditions passed: \n"
                                "- No blocker issues \n"
                                "- Code coverage on new code greater than 80%")
        else:
          mdFile.new_paragraph('***Not passed*** :x:')
          mdFile.new_paragraph("Quality gate conditions do not passed. Check the related issues")

        # Pie chart creation
        description = {"Issue type": ("string", "Issue type"),
                      "quantity": ("number", "Quantity")}
        data = [
            {"Issue type": "Bugs", "quantity": len(bugs_json)},
            {"Issue type": "Code smells", "quantity": len(code_smells_json)},
            {"Issue type": "Vulnerabilities",  "quantity": len(vulnerabilities_json)}
          ]

        data_table = gviz_api.DataTable(description)
        data_table.LoadData(data)

        # Create a JavaScript code string for pieChart.
        jscode_pieChart = data_table.ToJSCode("jscode_data",
                               columns_order=("Issue type", "quantity"))


        # Reliability chart creation
        description = {"file_name": ("string", "File name"),
                      "Lines_of_code": ("number", "Lines of code"),
                      "Remediation_effort": ("number", "Reliability remediation effort"),
                      "reliability_rating": ("string", "Reliability rating"),
                      "bugs": ("number", "Bugs")}

        data = []
        for y in reliability:
          for x in range(len(y["measures"])):
            if y["measures"][x]["metric"] == "ncloc":
              Lines_of_code_value = y["measures"][x]["value"]
            elif y["measures"][x]["metric"] == "bugs":
              bugs_value = y["measures"][x]["value"]
            elif y["measures"][x]["metric"] == "reliability_remediation_effort":
              reliability_remediation_effort_value = y["measures"][x]["value"]
            elif y["measures"][x]["metric"] == "reliability_rating":
              reliability_rating_value = y["measures"][x]["value"]

          data.append({"file_name": y["name"], "Lines_of_code": int(Lines_of_code_value), "Remediation_effort": int(reliability_remediation_effort_value), "reliability_rating": reliability_rating_value, "bugs": float(bugs_value)})
        data_table = gviz_api.DataTable(description)
        data_table.LoadData(data)

        # Create a JavaScript code string for reliability chart.
        jscode_reliability = data_table.ToJSCode("jscode_data_reliability", ["file_name", "Lines_of_code", "Remediation_effort", "reliability_rating", "bugs"])

        # Security chart creation
        description = {"file_name": ("string", "File name"),
                      "Lines_of_code": ("number", "Lines of code"),
                      "Security_remediation_effort": ("number", "Security remediation effort"),
                      "security_rating": ("string", "security rating"),
                      "vulnerabilities": ("number", "Vulnerabilities")}

        data = []
        for y in security:
          for x in range(len(y["measures"])):
            if y["measures"][x]["metric"] == "ncloc":
              Lines_of_code_value = y["measures"][x]["value"]
            elif y["measures"][x]["metric"] == "vulnerabilities":
              vulnerabilities_value = y["measures"][x]["value"]
            elif y["measures"][x]["metric"] == "security_remediation_effort":
              security_remediation_effort_value = y["measures"][x]["value"]
            elif y["measures"][x]["metric"] == "security_rating":
              security_rating_value = y["measures"][x]["value"]

          data.append({"file_name": y["name"], "Lines_of_code": int(Lines_of_code_value), "Security_remediation_effort": int(security_remediation_effort_value), "security_rating": security_rating_value, "vulnerabilities": float(vulnerabilities_value)})
        data_table = gviz_api.DataTable(description)
        data_table.LoadData(data)

        # Create a JavaScript code string for security chart.
        jscode_security = data_table.ToJSCode("jscode_data_security", ["file_name", "Lines_of_code", "Security_remediation_effort", "security_rating", "vulnerabilities"])

        charts = open("charts.html","w+")
        charts.write(page_template % vars())
        charts.close()
        
        mdFile.new_paragraph("{% include charts.html %}")

        # Issues found table creation
        for y in range(len(issues)):
            if y == 0:
                mdFile.new_header(1, '**Bugs found:**')
            elif y == 1:
                mdFile.new_header(1, '**Code smells found:**')
            else:
                mdFile.new_header(1, '**Vulnerabilities found:**')

            list_of_strings = ["Nº", "Description", "Severity", "Estimated resolution time", "File", "Line"]

            for x in range(len(issues[y])):
                if "effort" in issues[y][x].keys():
                    list_of_strings.extend([str(x), issues[y][x]["message"], issues[y][x]["severity"], issues[y][x]["effort"], issues[y][x]["component"], issues[y][x]["line"]])
                else:
                    list_of_strings.extend([str(x), issues[y][x]["message"], issues[y][x]["severity"], "-", issues[y][x]["component"], issues[y][x]["line"]])
            mdFile.new_line()
            mdFile.new_table(columns=6, rows=len(issues[y]) + 1, text=list_of_strings, text_align='center')

        mdFile.create_md_file()

if __name__ == "__main__":
    ResultsGenerator().generate_results()
