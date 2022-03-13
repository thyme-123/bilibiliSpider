import os

package_list=['requests','jsonpath','lxml']

for package in package_list:
    os.system('pip install {}'.format(package))