%define gitdate 20200724

Summary:   Cached AppStream metadata
Name:      appstream-data
Version:   8
Release:   %{gitdate}%{?dist}
BuildArch: noarch
License:   CC0 and CC-BY and CC-BY-SA and GFDL
URL:       http://people.redhat.com/rhughes/metadata/
Source1:   http://people.redhat.com/rhughes/metadata/rhel-%{version}-%{gitdate}.xml.gz
Source2:   http://people.redhat.com/rhughes/metadata/rhel-%{version}-%{gitdate}-icons.tar.gz
Source3:   https://raw.githubusercontent.com/hughsie/fedora-appstream/master/appstream-extra/adobe-flash.xml
Source4:   https://raw.githubusercontent.com/hughsie/fedora-appstream/master/appstream-extra/gstreamer-non-free.xml
Source5:   https://raw.githubusercontent.com/hughsie/fedora-appstream/master/appstream-extra/other-repos.xml
Source6:   https://raw.githubusercontent.com/hughsie/fedora-appstream/master/appstream-extra/fedora-categories.xml
Source7:   https://raw.githubusercontent.com/hughsie/fedora-appstream/master/appstream-extra/fedora-popular.xml

# extra applications not in RHEL
Source9:   http://people.redhat.com/rhughes/metadata/epel-%{version}-%{gitdate}.xml.gz
Source10:  http://people.redhat.com/rhughes/metadata/epel-%{version}-%{gitdate}-icons.tar.gz

# This is built using:
# dnf install fuse-sshfs -y
# sshfs user@host:/mnt/mirror/RHEL mnt
# dnf reposync --setopt=*.module_hotfixes=1 --repo rhel-8-baseos -p mnt/ &> rhel-8-baseos.log
# dnf reposync --setopt=*.module_hotfixes=1 --repo rhel-8-appstream -p mnt/ &> rhel-8-appstream.log
# dnf reposync --setopt=*.module_hotfixes=1 --repo rhel-8-crb -p mnt/ &> rhel-8-crb.log
# https://github.com/hughsie/appstream-scripts/blob/master/rhel/rhel-8.1-candidate.sh
#
# [rhel-8-baseos]
# name=Nightly Packages for Enterprise Linux 8
# baseurl=http://download.eng.brq.redhat.com/composes/nightly/latest-RHEL-8/compose/BaseOS/x86_64/os/
# enabled=1
# gpgcheck=0
#
# [rhel-8-appstream]
# name=Nightly Packages for Enterprise Linux 8
# baseurl=http://download.eng.brq.redhat.com/composes/nightly/latest-RHEL-8/compose/AppStream/x86_64/os/
# enabled=1
# gpgcheck=0
#
# [rhel-8-crb]
# name=Nightly Packages for Enterprise Linux 8
# baseurl=http://download.eng.brq.redhat.com/composes/nightly/latest-RHEL-8/compose/CRB/x86_64/os/
# enabled=1
# gpgcheck=0

BuildRequires: libappstream-glib

%description
This package provides the distribution specific AppStream metadata required
for the GNOME and KDE software centers.

%install

DESTDIR=%{buildroot} appstream-util install-origin rhel-%{version} %{SOURCE1} %{SOURCE2}
DESTDIR=%{buildroot} appstream-util install-origin epel-%{version} %{SOURCE9} %{SOURCE10}
DESTDIR=%{buildroot} appstream-util install \
	%{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7}

%files
%attr(0644,root,root) %{_datadir}/app-info/xmls/*
%{_datadir}/app-info/icons/rhel-%{version}/*/*.png
%{_datadir}/app-info/icons/epel-%{version}/*/*.png
%dir %{_datadir}/app-info
%dir %{_datadir}/app-info/icons
%dir %{_datadir}/app-info/icons/rhel-%{version}/64x64
%dir %{_datadir}/app-info/icons/rhel-%{version}/128x128
%dir %{_datadir}/app-info/icons/epel-%{version}/64x64
%dir %{_datadir}/app-info/icons/epel-%{version}/128x128
%dir %{_datadir}/app-info/xmls

%changelog
* Fri Jul 24 2020 Richard Hughes <richard@hughsie.com> 8-20200724
- Regenerate the RHEL metadata to include the EPEL apps too
- Resolves: #1844488

* Tue Jun 30 2020 Richard Hughes <richard@hughsie.com> 8-20200630
- Regenerate the RHEL metadata
- Resolves: #1844488

* Fri Nov 29 2019 Richard Hughes <richard@hughsie.com> 8-20191129
- Regenerate the RHEL metadata to include the latest evince changes
- Resolves: #1768461

* Mon Aug 05 2019 Richard Hughes <richard@hughsie.com> 8-20190805
- Regenerate the RHEL metadata to include the latest cockpit changes
- Resolves: #1673011

* Fri Jul 19 2019 Richard Hughes <richard@hughsie.com> 8-20190719
- Regenerate the RHEL metadata
- Resolves: #1673011

* Fri Jul 20 2018 Richard Hughes <richard@hughsie.com> 8-20180721
- Regenerate the RHEL metadata using rhel-8.0-appstream

* Thu Jul 19 2018 Richard Hughes <richard@hughsie.com> 8-20180720
- Regenerate the RHEL metadata using rhel-8.0-candidate

