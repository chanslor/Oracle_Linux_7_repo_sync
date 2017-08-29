Name:    ems-ol7-repo
Summary: Oracle Linux 7 EMS repo
Version: 1.0
Release: 1
License: Southern Company, EMS
Vendor:  Southern Company, EMS

Source0: OL7.repo
Source1: ol7-repo-sync.cron
Source1: ol7-repo-sync.bash

BuildRoot: /var/tmp/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch


AutoReqProv: no 
%global __os_install_post %{nil}


%description 
Oracle Linux 7 EMS repo


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
