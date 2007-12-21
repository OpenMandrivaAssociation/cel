%define	name	cel
%define	version	1.0
%define	release	%mkrel 1

Summary:	Crystal Entity Layer
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		System/Libraries
License:	LGPL
Source0:	%{name}-src-%{version}.tar.bz2
Patch0:		cel-1.0-x86_64-fix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.sourceforge.net/projects/cel/
BuildRequires:	jam crystalspace-devel >= 1.0 python-devel cppunit-devel
BuildRequires:	zlib-devel

%description
Crystal Entity Layer (CEL) is a game entity layer based on Crystal Space.
It makes it easier for game developers to create games based on Crystal Space.
CEL can optionally be used together with Python or other scripting languages.

%package	devel
Group:		Development/C
Summary:	Development headers and libraries for %{name}
Requires:	%{name} = %{version}

%description	devel
Development headers and libraries for %{name}

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1 -b .x86_64

%build
./autogen.sh
perl -pi -e "s#cspycommon##g" configure
%configure	--disable-separate-debug-info
jam %{_smp_mflags}

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} jam -d2 install

sed -i -e "s#/lib/#/%{_lib}/#g" %{buildroot}%{_bindir}/cel-config

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README docs/todo.txt docs/history.txt
%{_bindir}/*
%exclude %{_bindir}/cel.cex
%exclude %{_bindir}/%{name}-config
%{_datadir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.cfg
%{_bindir}/%{name}tst
%{_bindir}/bootstrap
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so

%files devel
%defattr(-,root,root)
%{_bindir}/cel.cex
%{_bindir}/%{name}-config
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.a


