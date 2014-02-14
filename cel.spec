%define major 2.0
%define libname %mklibname %{name} %{major}

Summary:	Crystal Entity Layer
Name:		cel
Version:	%{major}
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.crystalspace3d.org/
Source0:	http://www.crystalspace3d.org/downloads/release/%{name}-src-%{version}.tar.bz2
BuildRequires:	doxygen
BuildRequires:	ftjam >= 2.5.3rc2-0.9
BuildRequires:	icoutils
BuildRequires:	imagemagick
BuildRequires:	perl(Template::Base)
BuildRequires:	tetex-dvips
BuildRequires:	tetex-dvipdfm
BuildRequires:	texinfo
BuildRequires:	crystalspace-devel >= %{major}
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(zlib)

%description
Crystal Entity Layer (CEL) is a game entity layer based on Crystal Space.
It makes it easier for game developers to create games based on Crystal Space.
CEL can optionally be used together with Python or other scripting languages.

%files
%doc README docs/todo.txt docs/history.txt
%{_bindir}/*
%exclude %{_bindir}/%{name}-config
%{_datadir}/%{name}-%{major}
%dir %{_sysconfdir}/%{name}-%{major}
%config(noreplace) %{_sysconfdir}/%{name}-%{major}/*.cfg
%dir %{_libdir}/%{name}-%{major}
%{_libdir}/%{name}-%{major}/*.so
%{_libdir}/%{name}-%{major}/*.csplugin

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Shared libraries for %{name}.

%files -n %{libname}
%{_libdir}/libcelstartcore-%{major}.so
%{_libdir}/libceltool-%{major}.so

#----------------------------------------------------------------------------

%package devel
Summary:	Development headers and libraries for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description devel
Development headers and libraries for %{name}.

%files devel
%{_bindir}/%{name}-config
%dir %{_includedir}/%{name}-%{major}
%{_includedir}/%{name}-%{major}/*

#----------------------------------------------------------------------------

%package	doc
Summary:	Documentation for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description	doc
Documentation for %{name}.

%files doc
%{_docdir}/%{name}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-src-%{version}

%build
CXXFLAGS="%{optflags} -fpermissive" \
%configure2_5x \
	--disable-separate-debug-info \
	--disable-meta-info-embedding \
	--without-python

jam -d2 %{_smp_mflags}

%install
DESTDIR=%{buildroot} jam -d2 install

# Fix unstripped-binary-or-object
chmod 0755 %{buildroot}%{_libdir}/libcelstartcore-%{major}.so
chmod 0755 %{buildroot}%{_libdir}/libceltool-%{major}.so

