Name:    ems-ol7-repo-sync
Summary: Oracle Linux 7 EMS repo and sync
Version: 1.0
Release: 18
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
* Wed Jun 12 2019 mdchansl@southernco.com - 1.0-18
- Updated for UEKR5

* Wed Jun 12 2019 mdchansl@southernco.com - 1.0-17
- Oracle change repo meta data in May 2019

* Wed May 09 2018 mdchansl@southernco.com - 1.0-16
- Removed the createrepo. Clobbers wget updateinfo.

* Thu Feb 15 2018 mdchansl@southernco.com - 1.0-15
- Changes not showing up unless createrepo is run

* Tue Jan 16 2018 mdchansl@southernco.com - 1.0-14
- Changed UEK repodata pathing in ol7-repo-sync.bash

* Tue Jan 16 2018 mdchansl@southernco.com - 1.0-13
- updating for wgets

* Tue Jan 16 2018 mdchansl@southernco.com - 1.0-12
- Added wgets back to UEK in ol7-repo-sync.bash

* Tue Jan 16 2018 mdchansl@southernco.com - 1.0-11
- Update repo to include the base media

* Mon Jan 08 2018 mdchansl@southernco.com - 1.0-10
- using wget -q flag. Logs files way to verbose on large down loads.

* Thu Dec 28 2017 mdchansl@southernco.com - 1.0-9
- Must use the public repo on ap04sec0

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

