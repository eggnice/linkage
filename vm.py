#!/apps/svr/pyenv/versions/linkage/bin/python
# *_* coding: utf-8 *_* 
# _author: eggnice

import optparse
from linkage.openstack.ec.built.main import main

parser = optparse.OptionParser()
parser.add_option('-m', dest='module', default='12345678')
options, args = parser.parse_args()
main(args, options.module)
