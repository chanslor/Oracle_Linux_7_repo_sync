#!/bin/bash

# Mon Aug 28 10:15:44 CDT 2017
# Wed May  9 11:12:51 CDT 2018 mdchansl@southernco.com
# createrepo clobbers the CVE data, only do wget

# Wed Jun 12 13:33:41 CDT 2019 - Oracle changed the meta data in MAY 2019

REPOSYNC=/usr/bin/reposync
CREATEREPO=/usr/bin/createrepo

exec 1> /var/log/ol-repo-sync.log 2>&1

$REPOSYNC --download-metadata --downloadcomps -l -m -d -r ol7_latest -p /repo/OL/
$CREATEREPO --update -v /repo/OL/ol7_latest -g /repo/OL/ol7_latest/comps.xml

if [ -d /repo/OL/ol7_latest ] ; then
        cd /repo/OL/ol7_latest/
        gzip -d *-updateinfo.xml.gz
        mv *-updateinfo.xml updateinfo.xml
        modifyrepo /repo/OL/ol7_latest/updateinfo.xml /repo/OL/ol7_latest/repodata
else
	echo "Could NOT find /repo/OL/ol7_latest."
	exit 1
fi


$REPOSYNC --download-metadata --downloadcomps -l -m -d -r ol7_UEKR4 -p /repo/OL/
$CREATEREPO --update -v /repo/OL/ol7_UEKR4

if [ -d /repo/OL/ol7_UEKR4 ] ; then
        cd /repo/OL/ol7_UEKR4
        gzip -d *-updateinfo.xml.gz
        mv *-updateinfo.xml updateinfo.xml
        modifyrepo /repo/OL/ol7_UEKR4/updateinfo.xml /repo/OL/ol7_UEKR4/repodata
else
	echo "Could NOT find /repo/OL/ol7_UEKR4."
	exit 1
fi

$REPOSYNC --download-metadata --downloadcomps -l -m -d -r ol7_UEKR5 -p /repo/OL/
$CREATEREPO --update -v /repo/OL/ol7_UEKR5

if [ -d /repo/OL/ol7_UEKR5 ] ; then
        cd /repo/OL/ol7_UEKR5
        gzip -d *-updateinfo.xml.gz
        mv *-updateinfo.xml updateinfo.xml
        modifyrepo /repo/OL/ol7_UEKR5/updateinfo.xml /repo/OL/ol7_UEKR5/repodata
else
	echo "Could NOT find /repo/OL/ol7_UEKR5"
	exit 1
fi

$REPOSYNC --download-metadata --downloadcomps -l -m -d -r ol7_optional_latest -p /repo/OL/
$CREATEREPO --update -v /repo/OL/ol7_optional_latest

if [ -d /repo/OL/ol7_optional_latest ] ; then
        cd /repo/OL/ol7_optional_latest
        gzip -d *-updateinfo.xml.gz
        mv *-updateinfo.xml updateinfo.xml
        modifyrepo /repo/OL/ol7_optional_latest/updateinfo.xml /repo/OL/ol7_optional_latest/repodata
else
	echo "Could NOT find /repo/OL/ol7_optional_latest"
	exit 1
fi

$REPOSYNC --download-metadata --downloadcomps -l -m -d -r ol7_addons -p /repo/OL/
$CREATEREPO --update -v /repo/OL/ol7_addons

if [ -d /repo/OL/ol7_addons ] ; then
        cd /repo/OL/ol7_addons
        gzip -d *-updateinfo.xml.gz
        mv *-updateinfo.xml updateinfo.xml
        modifyrepo /repo/OL/ol7_addons/updateinfo.xml /repo/OL/ol7_addons/repodata
else
	echo "Could NOT find /repo/OL/ol7_addons"
	exit 1
fi

