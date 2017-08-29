Name:    ems-ol7-repo
Summary: Oracle Linux 7 EMS repo
Version: 1.0
Release: 1
License: Southern Company, EMS
Vendor:  Southern Company, EMS

Source0: OL7.repo
Source1: uvscan.repo

BuildRoot: /var/tmp/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch


AutoReqProv: no 
%global __os_install_post %{nil}


%description 
Oracle Linux 7 EMS repo


%install 

mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT/etc/cron.d/

cp %{SOURCE0} $RPM_BUILD_ROOT/etc/sysconfig/uvscan
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/yum.repos.d/



%files 
%defattr(-,root,root) 
%config(noreplace)/etc/sysconfig/uvscan
%config(noreplace)/etc/yum.repos.d/uvscan.repo
%config(noreplace)/usr/local/uvscan/exclude.list
/etc/cron.d/uvscan-client.crontab
/usr/local/uvscan/uvscan-client-update.bash
/usr/local/uvscan/uvscan.bash



%changelog
