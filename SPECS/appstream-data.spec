%define gitdate 20220302
%global enable_epel 1

Summary:   Cached AppStream metadata
Name:      appstream-data
Epoch:     1
Version:   9
Release:   %{gitdate}%{?dist}.1
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
%if 0%{?enable_epel}
Source9:   http://people.redhat.com/rhughes/metadata/epel-%{version}-%{gitdate}.xml.gz
Source10:  http://people.redhat.com/rhughes/metadata/epel-%{version}-%{gitdate}-icons.tar.gz
%endif

# This is built using:
# export ARCHIVE_PATH=/run/media/hughsie/Backup/mirror
# dnf reposync --setopt=*.module_hotfixes=1 --repo rhel-9-baseos -p ${ARCHIVE_PATH}/RHEL/ &> rhel-9-baseos.log
# dnf reposync --setopt=*.module_hotfixes=1 --repo rhel-9-appstream -p ${ARCHIVE_PATH}/RHEL/ &> rhel-9-appstream.log
# dnf reposync --setopt=*.module_hotfixes=1 --repo rhel-9-crb -p ${ARCHIVE_PATH}/RHEL/ &> rhel-9-crb.log
# https://github.com/hughsie/appstream-scripts/blob/master/rhel/rhel-9-candidate.sh

BuildRequires: libappstream-glib

%description
This package provides the distribution specific AppStream metadata required
for the GNOME and KDE software centers.

%install

DESTDIR=%{buildroot} appstream-util install-origin rhel-%{version} %{SOURCE1} %{SOURCE2}
%if 0%{?enable_epel}
DESTDIR=%{buildroot} appstream-util install-origin epel-%{version} %{SOURCE9} %{SOURCE10}
%endif
DESTDIR=%{buildroot} appstream-util install \
	%{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7}

%files
%attr(0644,root,root) %{_datadir}/app-info/xmls/*
%{_datadir}/app-info/icons/rhel-%{version}/*/*.png
%if 0%{?enable_epel}
%{_datadir}/app-info/icons/epel-%{version}/*/*.png
%endif
%dir %{_datadir}/app-info
%dir %{_datadir}/app-info/icons
%dir %{_datadir}/app-info/icons/rhel-%{version}/64x64
%dir %{_datadir}/app-info/icons/rhel-%{version}/128x128
%if 0%{?enable_epel}
%dir %{_datadir}/app-info/icons/epel-%{version}/64x64
%dir %{_datadir}/app-info/icons/epel-%{version}/128x128
%endif
%dir %{_datadir}/app-info/xmls

%changelog
* Thu Mar 03 2022 Richard Hughes <richard@hughsie.com> 1:9-20220302
- New metadata version
- Resolves: rhbz#1994416

* Mon Nov 01 2021 Richard Hughes <richard@hughsie.com> 1:9-20211101
- New metadata version
- Resolves: rhbz#2005266

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1:9-20210805.1
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Aug 05 2021 Richard Hughes <richard@hughsie.com> 1:9-20210805
- New metadata version
- Resolves: rhbz#1926838

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 34-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Mar 31 2021 Richard Hughes <richard@hughsie.com> 34-1
- New metadata version

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Richard Hughes <richard@hughsie.com> 33-1
- New metadata version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 13 2020 Richard Hughes <richard@hughsie.com> 32-6
- New metadata version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Kalev Lember <klember@redhat.com> - 32-4
- New metadata version

* Mon Oct 14 2019 Kalev Lember <klember@redhat.com> - 32-3
- New metadata version

* Thu Sep 19 2019 Kalev Lember <klember@redhat.com> - 32-2
- Update webapps.xml

* Thu Sep 19 2019 Kalev Lember <klember@redhat.com> - 32-1
- New metadata version

* Wed Sep 18 2019 Kalev Lember <klember@redhat.com> - 31-4
- Update categories and popular xmls with renamed app ids

* Wed Sep 18 2019 Kalev Lember <klember@redhat.com> - 31-3
- New metadata version

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Richard Hughes <richard@hughsie.com> 31-1
- New metadata version

* Thu Apr 18 2019 Kalev Lember <klember@redhat.com> - 30-5
- New metadata version

* Thu Apr 11 2019 Kalev Lember <klember@redhat.com> - 30-4
- New metadata version
- Update changed app IDs in categories and popular xml files

* Mon Apr 01 2019 Kalev Lember <klember@redhat.com> - 30-3
- New metadata version
- Update fedora-categories.xml and fedora-popular.xml with changed app IDs
- Remove steam-oars.xml now that gnome-software no longer ships the steam plugin

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Kalev Lember <klember@redhat.com> - 30-1
- New metadata version

* Thu Dec 13 2018 Kalev Lember <klember@redhat.com> - 29-8
- New metadata version

* Wed Oct 10 2018 Kalev Lember <klember@redhat.com> - 29-7
- New metadata version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Kalev Lember <klember@redhat.com> - 29-5
- New metadata version

* Thu Apr 19 2018 Kalev Lember <klember@redhat.com> - 29-4
- New metadata version

* Wed Apr 04 2018 Kalev Lember <klember@redhat.com> - 29-3
- New metadata version

* Tue Mar 27 2018 Kalev Lember <klember@redhat.com> - 29-2
- New metadata version

* Fri Mar 02 2018 Kalev Lember <klember@redhat.com> - 29-1
- New metadata version

* Thu Feb 15 2018 Kalev Lember <klember@redhat.com> - 28-4
- New metadata version
- Sync other-repos.xml and webapps.xml with fedora-appstream
- Add google-chrome.xml with Google Chrome metadata

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 28 2017 Kalev Lember <klember@redhat.com> - 28-2
- New metadata version

* Tue Dec 12 2017 Kalev Lember <klember@redhat.com> - 28-1
- New metadata version

* Wed Nov 29 2017 Kalev Lember <klember@redhat.com> - 27-7
- New metadata version

* Mon Oct 16 2017 Kalev Lember <klember@redhat.com> - 27-6
- New metadata version

* Thu Aug 31 2017 Kalev Lember <klember@redhat.com> - 27-5
- New metadata version

* Thu Aug 03 2017 Kalev Lember <klember@redhat.com> - 27-4
- New metadata version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> 27-2
- New metadata version

* Wed Jun 14 2017 Kalev Lember <klember@redhat.com> 27-1
- New metadata version

* Tue Apr 11 2017 Kalev Lember <klember@redhat.com> 26-11
- New metadata version

* Mon Mar 06 2017 Kalev Lember <klember@redhat.com> 26-10
- New metadata version

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> 26-9
- New metadata version

* Mon Jan 23 2017 Kalev Lember <klember@redhat.com> 26-8
- New metadata version

* Mon Jan 09 2017 Kalev Lember <klember@redhat.com> 26-7
- New metadata version

* Fri Dec 30 2016 Kalev Lember <klember@redhat.com> 26-6
- New metadata version

* Tue Dec 20 2016 Kalev Lember <klember@redhat.com> 26-5
- New metadata version

* Fri Dec 02 2016 Kalev Lember <klember@redhat.com> 26-4
- New metadata version

* Fri Oct 14 2016 Richard Hughes <richard@hughsie.com> 26-3
- New metadata version

* Mon Sep 19 2016 Richard Hughes <richard@hughsie.com> 26-2
- New metadata version
- Add Steam OARS overrides

* Tue Aug 09 2016 Richard Hughes <richard@hughsie.com> 26-1
- New metadata version

* Sun Jun 12 2016 Richard Hughes <richard@hughsie.com> 25-4
- New metadata version

* Thu May 26 2016 Richard Hughes <richard@hughsie.com> 25-3
- Add the Fedora-specific popular metadata

* Thu May 26 2016 Kalev Lember <klember@redhat.com> 25-2
- New metadata version
- Add a test for gstreamer1-plugin-openh264

* Wed Apr 27 2016 Richard Hughes <richard@hughsie.com> 25-1
- New metadata version

* Mon Feb 15 2016 Richard Hughes <richard@hughsie.com> 24-4
- New metadata version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 16 2015 Richard Hughes <richard@hughsie.com> 24-2
- New metadata version

* Wed Aug 19 2015 Richard Hughes <richard@hughsie.com> 24-1
- New metadata version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Richard Hughes <richard@hughsie.com> 23-2
- New metadata version
- Fix the installed icon location for the new origin value

* Mon May 11 2015 Richard Hughes <richard@hughsie.com> 23-1
- New metadata version
- Debundle the appstream-extra files

* Thu Apr 23 2015 Richard Hughes <richard@hughsie.com> 22-7
- New metadata version.

* Fri Mar 20 2015 Kalev Lember <kalevlember@gmail.com> 22-6
- New metadata version.

* Wed Mar 04 2015 Richard Hughes <richard@hughsie.com> 22-5
- New metadata version, this time with all the icons.

* Tue Feb 24 2015 Richard Hughes <richard@hughsie.com> 22-4
- New metadata version.

* Mon Sep 29 2014 Richard Hughes <richard@hughsie.com> 22-3
- Ship HiDPI icons, harder

* Mon Sep 29 2014 Richard Hughes <richard@hughsie.com> 22-2
- Ship HiDPI icons

* Thu Jul 17 2014 Richard Hughes <richard@hughsie.com> 22-1
- New metadata version number, data unchanged.

* Wed Jul 02 2014 Richard Hughes <richard@hughsie.com> 21-5
- New metadata version with source screenshots.

* Mon Jun 30 2014 Richard Hughes <richard@hughsie.com> 21-4
- New metadata version that passes xmllint.

* Thu Jun 19 2014 Richard Hughes <richard@hughsie.com> 21-3
- New metadata version.

* Wed Jun 11 2014 Richard Hughes <richard@hughsie.com> 21-2
- Own the correct directories
- Resolves: https://bugzilla.redhat.com/show_bug.cgi?id=1107802#c5

* Tue Jun 10 2014 Richard Hughes <richard@hughsie.com> 21-1
- Initial version for Fedora package review
