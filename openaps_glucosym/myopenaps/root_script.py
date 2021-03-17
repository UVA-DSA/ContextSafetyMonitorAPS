from selenium import webdriver
from subprocess import call
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

#browser = webdriver.Firefox(executable_path='./geckodriver')

## Generate fault_scenario
#cmd = "python "+"gen_fault_code_openAPS.py"
#os.system(cmd)

browser = webdriver.Firefox()
browser.set_window_size(900,900)
browser.set_window_position(1000,0)
sleep(1)
browser.get("http://localhost:3000/")
sleep(2)
patient_id = ["patient_a","patient_b","patient_c","patient_d","patient_e","patient_f","patient_g","patient_h","patient_i"]
#patient_id = ["patient_a"]
for i in patient_id:
	browser.find_element_by_id(i).click()
	#call#(["python","initialize.py"])
	#cmd = "./run_fault_inject_campaign.sh"
	cmd = "python "+ "initialize.py"
	os.system(cmd)
	cmd = "python "+ "updated_ct_script_iob_based.py"
	os.system(cmd)
browser.close()

#browser.close()
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
