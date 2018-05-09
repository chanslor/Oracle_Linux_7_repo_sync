#!/bin/bash

# Mon Aug 28 10:15:44 CDT 2017
# Wed May  9 11:12:51 CDT 2018 mdchansl@southernco.com
# createrepo clobbers the CVE data, only do wget

exec 1> /var/log/ol-repo-sync.log 2>&1

/usr/bin/reposync -l -m -d -r ol7_latest -p /repo/OL/

cd /repo/OL/ol7_latest/
cd /repo/OL/ol7_latest/repodata/
/usr/bin/wget -q -N http://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/repodata/comps.xml
/usr/bin/wget -q -N http://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/repodata/filelists.xml.gz
/usr/bin/wget -q -N http://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/repodata/other.xml.gz
/usr/bin/wget -q -N http://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/repodata/primary.xml.gz
/usr/bin/wget -q -N http://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/repodata/repomd.xml
/usr/bin/wget -q -N http://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/repodata/updateinfo.xml.gz

#Next, the UEK kernel
cd /repo/OL/ol7_UEKR4
/usr/bin/reposync --download-metadata --downloadcomps -l -m -d -r ol7_UEKR4 -p /repo/OL/

cd /repo/OL/ol7_UEKR4/repodata/
/usr/bin/wget -q -N http://yum.oracle.com/repo/OracleLinux/OL7/UEKR4/x86_64/repodata/filelists.xml.gz
/usr/bin/wget -q -N http://yum.oracle.com/repo/OracleLinux/OL7/UEKR4/x86_64/repodata/other.xml.gz
/usr/bin/wget -q -N http://yum.oracle.com/repo/OracleLinux/OL7/UEKR4/x86_64/repodata/primary.xml.gz
/usr/bin/wget -q -N http://yum.oracle.com/repo/OracleLinux/OL7/UEKR4/x86_64/repodata/repomd.xml
/usr/bin/wget -q -N http://yum.oracle.com/repo/OracleLinux/OL7/UEKR4/x86_64/repodata/updateinfo.xml.gz

