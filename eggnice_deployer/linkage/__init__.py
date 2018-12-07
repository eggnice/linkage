#!/apps/svr/pyenv/versions/linkage/bin/python
# --- edit by lambda ---

from importconfig import conf
# set op config
opconfig = conf()
opconfig.from_pyfile('opconfig.py')
#opconfig.from_pyfile('/apps/data/tomcat_8080/jenkins_file/linkage/config.py')
# opconfig.from_envvar(varname)

# set ec config
ecconfig = conf()
ecconfig.from_pyfile('ecconfig.py')
#ecconfig.from_pyfile('/apps/data/tomcat_8080/jenkins_file/linkage/config.py')
# ecconfig.from_envvar(varname)

# set sdn config
sdnconfig = conf()
sdnconfig.from_pyfile('sdnconfig.py')
#sdnconfig.from_pyfile('/apps/data/tomcat_8080/jenkins_file/linkage/config.py')
# sdnconfig.from_envvar(varname)


import logging
linkageconfig = conf()
linkageconfig.from_pyfile('linkageconfig.py')

logging.basicConfig(level=logging.INFO, filename=linkageconfig['FILENAME'],
                    filemode=linkageconfig['FILEMODE'],
                    format="%(asctime)s[%(levelname)s] -- %(filename)s:%(lineno)d -- %(message)s")
loggers = logging.getLogger(__name__)

from linkage.utils import utils
Utils = utils()
