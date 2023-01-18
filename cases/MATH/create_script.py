import os
import json

case_name = input('请输入用例名称（参照格式：test_math_lesson_info):')
is_workflow = input('输入y or yes代表为工作流用例，否则为单接口用例，请输入：')
is_workflow = True if is_workflow.lower() in ['y', 'yes'] else False

work_dir = 'test_workflow' if is_workflow else 'test_single'

case_file = os.path.join(os.path.dirname(__file__), 'test_cases', work_dir, case_name + '.py')
json_file = os.path.join(os.path.dirname(__file__), 'test_data', work_dir, case_name + '.json')

if os.path.isfile(case_file):
    print('***该用例脚本文件已存在，请检查***')
    raise SystemExit(1)

is_need_data = input('请输入是否需要参数，若需要输入y，输入其它任意键退出')
is_need_data = True if is_need_data == 'y' else False

with open('templates.py') as fp:
    lines = fp.readlines()

new_lines = []
for line in lines:
    demo_class = 'TestMain'
    demo_function = 'test_main'
    if demo_class in line:
        line = line.replace(demo_class, ''.join([c.capitalize() for c in case_name.split('_')]))
    if demo_function in line:
        line = line.replace(demo_function, case_name)
        if is_need_data:
            line = line.replace('math_client', 'math_client,data')
    new_lines.append(line)

with open(case_file, 'w') as fp:
    for line in new_lines:
        fp.write(line)

if is_need_data:
    with open(json_file, 'w') as fp:
        data = {"setup_data": {}, case_name: [{}]}
        json.dump(data, fp, indent=2)
