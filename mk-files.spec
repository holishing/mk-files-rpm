Summary: Support files for bmake, the NetBSD make(1) tool
Name: mk-files
Version: 20110808
Release: 1%{?dist}
License: BSD
Group: Development/Tools
URL: ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/
Source0: ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/mk-%{version}.tar.gz
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
