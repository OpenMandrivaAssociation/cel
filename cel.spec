Summary:	Crystal Entity Layer
Name:		cel
Version:	1.2.1
Release:	%mkrel 4
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.crystalspace3d.org/
Source0:	http://www.crystalspace3d.org/downloads/release/%{name}-src-%{version}.tar.bz2
Patch0:		cel-1.2.1-fix-str-fmt.patch
BuildRequires:	ftjam
BuildRequires:	crystalspace-devel >= 1.2
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
BuildRequires:	crystalspace-bindings-python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Crystal Entity Layer (CEL) is a game entity layer based on Crystal Space.
It makes it easier for game developers to create games based on Crystal Space.
CEL can optionally be used together with Python or other scripting languages.

%package devel
Summary:	Development headers and libraries for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers and libraries for %{name}.

%package doc
Summary:	Documentation for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p0

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
%exclude %{_bindir}/%{name}-config
%{_datadir}/%{name}-1.2
%dir %{_sysconfdir}/%{name}-1.2
%config(noreplace) %{_sysconfdir}/%{name}-1.2/*.cfg
%dir %{_libdir}/%{name}-1.2
%{_libdir}/%{name}-1.2/*.so
%{_libdir}/%{name}-1.2/*.csplugin

%files devel
%defattr(-,root,root)
%{_bindir}/%{name}-config
%dir %{_includedir}/%{name}-1.2
%{_includedir}/%{name}-1.2/*
%{_libdir}/*.a

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}-%{version}
