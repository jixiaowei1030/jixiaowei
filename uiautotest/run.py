import os
import allure

os.system("pytest /Users/xmly/PycharmProjects/uiautotest/cases/test_case.py --alluredir=allure_reports")



# os.system("pytest -alluredir=allure_reports")

# os.system("allure generate allure_reports -o allure_html_report --clean")