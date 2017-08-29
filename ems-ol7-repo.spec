Name:    ems-ol7-repo-sync
Summary: Oracle Linux 7 EMS repo and sync
Version: 1.0
Release: 4
License: Southern Company, EMS
Vendor:  Southern Company, EMS

Source0: OL7.repo
Source1: ol7-repo-sync.cron
Source2: ol7-repo-sync.bash

BuildRoot: /var/tmp/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch


AutoReqProv: no 
%global __os_install_post %{nil}


%description 
Oracle Linux 7 EMS repo and sync


%install 

mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT/etc/cron.d/
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/

cp %{SOURCE0} $RPM_BUILD_ROOT/etc/yum.repos.d/
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.d/
cp %{SOURCE2} $RPM_BUILD_ROOT/usr/local/bin/



%files 
%defattr(-,root,root) 
/etc/yum.repos.d/OL7.repo
/etc/cron.d/ol7-repo-sync.cron
/usr/local/bin/ol7-repo-sync.bash



%changelog
* Tue Aug 29 2017 mdchansl@southernco.com - 1.0-4
- SOURCE1 correction

* Tue Aug 29 2017 mdchansl@southernco.com
- Updated Description

* Tue Aug 29 2017 mdchansl@southernco.com
- Added cron entry

