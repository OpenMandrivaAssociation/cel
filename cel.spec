Summary:	Crystal Entity Layer
Name:		cel
%define	major	1.4
Version:	%{major}.1
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.crystalspace3d.org/
Source0:	http://www.crystalspace3d.org/downloads/release/%{name}-src-%{version}.tar.bz2
Patch0:		cel-1.4.1-fix-str-fmt.patch
BuildRequires:	ftjam >= 2.5.3rc2-0.9
BuildRequires:	crystalspace-devel >= %{major}
BuildRequires:	python-devel
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRequires:	doxygen
BuildRequires:	imagemagick
BuildRequires:	perl(Template::Base)
BuildRequires:	tetex-dvips
BuildRequires:	tetex-dvipdfm
BuildRequires:	icoutils
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	crystalspace-bindings-python

%description
Crystal Entity Layer (CEL) is a game entity layer based on Crystal Space.
It makes it easier for game developers to create games based on Crystal Space.
CEL can optionally be used together with Python or other scripting languages.

%package	devel
Summary:	Development headers and libraries for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description	devel
Development headers and libraries for %{name}.

%package	doc
Summary:	Documentation for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description	doc
Documentation for %{name}.

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1 -b .str_fmt~

%build
CXXFLAGS="%{optflags} -fpermissive" \
%configure2_5x \
	--disable-separate-debug-info \
	--disable-meta-info-embedding

jam -d2 %{_smp_mflags}

%install
DESTDIR=%{buildroot} jam -d2 install

%files
%doc README docs/todo.txt docs/history.txt
%{_bindir}/*
%exclude %{_bindir}/%{name}-config
%{_datadir}/%{name}-%{major}
%dir %{_sysconfdir}/%{name}-%{major}
%config(noreplace) %{_sysconfdir}/%{name}-%{major}/*.cfg
%{_libdir}/libceltool-%{major}.so
%dir %{_libdir}/%{name}-%{major}
%{_libdir}/%{name}-%{major}/*.so
%{_libdir}/%{name}-%{major}/*.csplugin
%{python_sitearch}/blcelc.pth

%files devel
%{_bindir}/%{name}-config
%dir %{_includedir}/%{name}-%{major}
%{_includedir}/%{name}-%{major}/*

%files doc
%{_docdir}/%{name}-%{version}


%changelog
* Mon Jan 23 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.4.1-1
+ Revision: 767385
- update string format patch
- make sure we pull in a non-segfaulting ftjam
- use pkgconfig() dependencies
- use %%{EVRD} macro
- cleanups
- new version

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Mon Oct 05 2009 Emmanuel Andry <eandry@mandriva.org> 1.2.1-4mdv2010.0
+ Revision: 453949
- disable useless autogen

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jan 22 2009 Funda Wang <fwang@mandriva.org> 1.2.1-3mdv2009.1
+ Revision: 332565
- fix str fmt

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-2mdv2009.0
+ Revision: 266476
- rebuild early 2009.0 package (before pixel changes)

* Thu May 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.1-1mdv2009.0
+ Revision: 213003
- fix file list
- update to new version 1.2.1

* Thu Apr 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2-2mdv2009.0
+ Revision: 197309
- rebuild

* Thu Apr 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2-1mdv2009.0
+ Revision: 197101
- add build requires on crystalspace-bindings-python
- add new subpackage with documentation
- spec file clean
- fix file list
- add lot of missing buildrequires
- spec file clean
- new version
- drop patch 0
- add missing buildrequires on libtool, texinfo and imagemagick

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jan 22 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0-1mdv2007.0
+ Revision: 111832
- fix build on x86_64 (P0)
- buildrequires on zlib-devel (??)
- new release: 1.0
  clean out old junk
  lib64 fix for cel-config
- Import cel

* Wed Mar 09 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.99-0.20050309.2mdk
- gah, headers went in the wrong place

* Wed Mar 09 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.99-0.20050309.1mdk
- new cvs snapshot
- fix buildrequires
- drop P0

