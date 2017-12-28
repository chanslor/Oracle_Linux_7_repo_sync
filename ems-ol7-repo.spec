Name:    ems-ol7-repo-sync
Summary: Oracle Linux 7 EMS repo and sync
Version: 1.0
Release: 8
License: Southern Company, EMS
Vendor:  Southern Company, EMS

Source0: public-yum-ol7.repo
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
/etc/yum.repos.d/public-yum-ol7.repo
/etc/cron.d/ol7-repo-sync.cron
%attr(0755,root,root)/usr/local/bin/ol7-repo-sync.bash



%changelog
* Thu Dec 28 2017 mdchansl@southernco.com - 1.0-8
- Fixed path for updates after --download-metadata --downloadcomps replaces
  wgets on server

* Wed Aug 30 2017 mdchansl@southernco.com - 1.0-7
- Disable repo by default

* Wed Aug 30 2017 mdchansl@southernco.com - 1.0-6
- Made bash script executable

* Wed Aug 30 2017 mdchansl@southernco.com - 1.0-5
- Include re-direct to log file in cron

* Tue Aug 29 2017 mdchansl@southernco.com - 1.0-4
- SOURCE1 correction

* Tue Aug 29 2017 mdchansl@southernco.com
- Updated Description

* Tue Aug 29 2017 mdchansl@southernco.com
- Added cron entry

