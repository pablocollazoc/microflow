#!/usr/bin/python

from mdutils.mdutils import MdUtils
from mdutils import Html
import os
import datetime
import time


class SpotbugsResults:

  def generate_results(self):

    bugs = os.getenv('bugs')

    date1 = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    date2 = str(datetime.datetime.now().strftime("%Y.%m.%d"))
    time1 = str(time.strftime("%H_%M"))
    mdFile = MdUtils(file_name=date2 + "-" + time1 + "-" + 'bug_report', title='Spotbugs analysis results')
    mdFile.new_header(1, "This GitHub page shows the spotbugs analysis results for the requested project")
    list_of_strings = ["Nº", "Severity", "Description", "Bug"]

    for y in range(bugs.count('[ERROR]')):
      description = bugs.split('[ERROR] ')[y+1].split(':', 1)[1].split(' ')
      bug = description.pop()
      description = " ".join(description)
      list_of_strings.extend([str(y), bugs.split('[ERROR] ')[y+1].split(':', 1)[0], description, bug])
    mdFile.new_table(columns=4, rows=bugs.count('[ERROR]')+1, text=list_of_strings, text_align='center')

    mdFile.create_md_file()
    

if __name__ == "__main__":
    SpotbugsResults().generate_results()
