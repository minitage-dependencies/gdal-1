import os
def getgdalenv(options,buildout):
    # copy in LNK_FLAGS for gdal < 1.5 !
    # see http://trac.osgeo.org/gdal/wiki/FAQInstallationAndBuilding#HowcaniaddparticularLDFLAGSwithGDAL1.5 (little hack (kiorky))
    os.environ['LNK_FLAGS'] = os.environ['LDFLAGS']
    os.environ['LIBS'] = os.environ['LDFLAGS']
def installswq(options,buildout):
    # copy in LNK_FLAGS for gdal < 1.5 !
    # see http://trac.osgeo.org/gdal/wiki/FAQInstallationAndBuilding#HowcaniaddparticularLDFLAGSwithGDAL1.5 (little hack (kiorky))
    swqh = os.path.join(buildout['buildout']['directory'], 'parts', 'part', 'include', 'swq.h')
    swqho = os.path.join(buildout['buildout']['directory'], 'swq.h')
    open(swqh , "w").write(open(swqho).read())
# vim:set ts=4 sts=4 et  :
