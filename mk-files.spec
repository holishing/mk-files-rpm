Summary:   Support files for bmake, the NetBSD make(1) tool
Name:      mk-files
Version:   20140314
Release:   1%{?dist}
License:   BSD
Group:     Development/Tools
URL:       ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/
Source0:   ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/mk-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The mk-files package provides some bmake macros derived from the NetBSD
bsd.*.mk macros.  These macros allow the creation of simple Makefiles to
build all kinds of targets, including, for example, C/C++ programs and/or
shared libraries.

%prep
%setup -q -n mk
sed -i.timestamp -e 's|cp_f=-f|cp_f=-pf|' install-mk

%build

%install
rm -rf ${RPM_BUILD_ROOT}
install -m 755 -d ${RPM_BUILD_ROOT}%{_datadir}/mk
env FORCE_BSD_MK={RPM_BUILD_ROOT}/nonexistent \
    SYS_MK_DIR=${RPM_BUILD_ROOT}/nonexistent \
    sh install-mk -v -m 644 ${RPM_BUILD_ROOT}%{_datadir}/mk

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%dir %{_datadir}/mk
%{_datadir}/mk/*

%changelog
* Wed Apr 09 2014 Luis Bazan <lbazan@fedoraproject.org> - 20140314-1
- New Upstream Version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130401-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Luis Bazan <lbazan@fedoraproject.org> - 20130401-1
- New Upstream Version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120808-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 05 2012 Luis Bazan <lbazan@fedoraproject.org> - 20120808-1
- New Upstream Version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120420-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Luis Bazan <bazanluis20@gmail.com> - 20120420-1
- New Upstream version 20120420-1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Luis Bazan <bazanluis20@gmail.com> - 20111111-1
- New upstream version 20111111

* Thu Sep 29 2011 Luis Bazan <bazanluis20@gmail.com> - 20110808-1
- new upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081111-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Stepan Kasal <skasal@redhat.com> - 20081111-1
- new upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070430-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 2 2008 Julio M. Merino Vidal <jmmv@NetBSD.org> - 20070430-1
- Initial release for Fedora.
