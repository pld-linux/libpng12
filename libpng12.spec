Summary:	PNG library version 1.2.x
Summary(pl.UTF-8):	Biblioteka PNG w wersji 1.2.x
Name:		libpng12
Version:	1.2.53
Release:	1
Epoch:		2
License:	distributable
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libpng/libpng-%{version}.tar.xz
# Source0-md5:	7d18a74e6fd2029aee76ccd00e00a9e6
Patch0:		libpng-pngminus.patch
Patch1:		libpng-opt.patch
Patch2:		libpng-norpath.patch
Patch3:		libpng-export_old.patch
Patch4:		libpng-revert.patch
Patch5:		http://downloads.sourceforge.net/libpng-apng/libpng-%{version}-apng.patch.gz
# Patch5-md5:	48dc9484d365f91435b5a4027dc56035
URL:		http://www.libpng.org/pub/png/libpng.html
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz >= 1:4.999.7
BuildRequires:	zlib-devel
%ifarch %{x8664} ia64 ppc64 s390x sparc64
Provides:	libpng.so.3()(64bit)
%else
Provides:	libpng.so.3
%endif
Provides:	libpng12(APNG) = 0.10
Obsoletes:	libpng < 2:1.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PNG library is a collection of routines used to create and
manipulate PNG format graphics files. The PNG format was designed as a
replacement for GIF, with many improvements and extensions.

This package provides older 1.2.x series of library.

%description -l pl.UTF-8
Biblioteki PNG są kolekcją form używanych do tworzenia i manipulowania
plikami w formacie graficznym PNG. Format ten został stworzony jako
zamiennik dla formatu GIF, z wieloma rozszerzeniami i nowościami.

Ten pakiet dostarcza bibliotekę ze starszej serii 1.2.x.

%package devel
Summary:	Header files for libpng 1.2.x
Summary(pl.UTF-8):	Pliki nagłówkowe libpng 1.2.x
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	zlib-devel
Provides:	libpng12(APNG)-devel = 0.10
Obsoletes:	libpng-devel < 2:1.4.0

%description devel
The header files are only needed for development of programs using the
PNG library version 1.2.x.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających biblioteki PNG w wersji 1.2.x.

%package static
Summary:	Static PNG library version 1.2.x
Summary(pl.UTF-8):	Biblioteka statyczna PNG w wersji 1.2.x
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	libpng12(APNG)-static = 0.10
Obsoletes:	libpng-static < 2:1.4.0

%description static
Static PNG library version 1.2.x.

%description static -l pl.UTF-8
Biblioteka statyczna PNG w wersji 1.2.x.

%prep
%setup -q -c -T -n libpng-%{version}
xzcat -dc %{SOURCE0} | tar xf - -C ..
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man{3,5}} \
	$RPM_BUILD_ROOT{%{_pkgconfigdir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpng.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpng12.la

# these come from libpng (1.4.x) now
%{__rm} $RPM_BUILD_ROOT%{_bindir}/libpng-config \
	$RPM_BUILD_ROOT%{_includedir}/png*.h \
	$RPM_BUILD_ROOT%{_libdir}/libpng.{so,a} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/libpng.pc
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/man[35]

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES KNOWNBUG README LICENSE
%attr(755,root,root) %{_libdir}/libpng12.so.*.*.*
%attr(755,root,root) %{_libdir}/libpng.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpng12.so.0
# alternative soname (symlink in PLD, so must be packaged)
%attr(755,root,root) %{_libdir}/libpng.so.3

%files devel
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/libpng12-config
%attr(755,root,root) %{_libdir}/libpng12.so
%{_pkgconfigdir}/libpng12.pc
%{_includedir}/libpng12

%files static
%defattr(644,root,root,755)
%{_libdir}/libpng12.a
