import os
import time
import ddlogs

os.system("python setup.py install")

os.system("pandoc README.md --from=markdown --to=rst > README.txt")
os.system("python setup.py sdist")
os.system("twine upload dist/*")
os.remove('README.txt')

time.sleep(60)

os.system("git tag v{}".format(ddlogs.__version__))
os.system("git push origin v{}".format(ddlogs.__version__))
