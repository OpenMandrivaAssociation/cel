Summary:	Crystal Entity Layer
Name:		cel
Version:	1.2
Release:	%mkrel 1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.crystalspace3d.org/
Source0:	http://www.crystalspace3d.org/downloads/release/%{name}-src-%{version}.tar.bz2
BuildRequires:	ftjam
BuildRequires:	crystalspace-devel >= 1.0
BuildRequires:	python-devel
BuildRequires:	cppunit-devel
BuildRequires:	zlib-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRequires:	doxygen
BuildRequires:	imagemagick
BuildRequires:	perl(Template::Base)
BuildRequires:	tetex-dvips
BuildRequires:	tetex-dvipdfm
BuildRequires:	icoutils
BuildRequires:	librsvg
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Crystal Entity Layer (CEL) is a game entity layer based on Crystal Space.
It makes it easier for game developers to create games based on Crystal Space.
CEL can optionally be used together with Python or other scripting languages.

%package devel
Group:		Development/C
Summary:	Development headers and libraries for %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers and libraries for %{name}

%prep
%setup -q -n %{name}-src-%{version}

%build
./autogen.sh

perl -pi -e "s#cspycommon##g" configure

%configure2_5x \
	--disable-separate-debug-info \
	--disable-meta-info-embedding

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
