Summary:	PNG library
Summary(de):	PNG-Library
Summary(fr):	Librarie PNG
Summary(pl):	Biblioteka PNG
Summary(tr):	PNG kitaplýðý
Name:		libpng
Version:	1.0.15
Release:	3
Epoch:		2
License:	distributable
Group:		Libraries
Source0:	ftp://swrinde.nde.swri.edu/pub/png/src/%{name}-%{version}.tar.bz2
# Source0-md5:	69569534bd0d6a9443189ba56cd89ef3	
Patch0:		%{name}-opt.patch
Patch1:		%{name}-pngminus.patch
Patch2:		%{name}-badchunks.patch
Patch3:		%{name}-SONAME.patch
Patch4:		%{name}-16bit-overflow.patch
Patch5:		%{name}-pngerror.patch
URL:		http://www.libpng.org/pub/png/libpng.html
Provides:	libpng10.so.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libpng2

%description
The PNG library is a collection of routines used to create and
manipulate PNG format graphics files. The PNG format was designed as a
replacement for GIF, with many improvements and extensions.

%description -l de
Die PNG-Library ist eine Sammlung von Routinen zum Erstellen und
Bearbeiten von Grafiken im PNG-Format. Das PNG-Format wurde als Ersatz
für GIF entwickelt und enthält viele Verbesserungen und Erweiterungen.

%description -l fr
La librairie PNG est un ensemble de routines utilisées pour créer et
manipuler des fichiers graphiques au format PNG. Le format PNG a été
élaboré pour remplacer le GIF, avec de nombreuses améliorations et
extensions.

%description -l pl
Biblioteka PNG to zestaw funkcji u¿ywanych do tworzenia i obróbki
plików w formatacie graficznym PNG. Format ten zosta³ stworzony jako
zamiennik dla formatu GIF, z wieloma ulepszeniami i rozszerzeniami.

%description -l tr
PNG kitaplýðý, PNG formatýndaki resim dosyalarýný iþlemeye yönelik
yordamlarý içerir. PNG, GIF formatýnýn yerini almak üzere tasarlanmýþ
bir resim formatýdýr.

%package devel
Summary:	libpng header files
Summary(de):	Headers und statische Libraries
Summary(fr):	En-têtes et bibliothèques statiques
Summary(pl):	Pliki nag³ówkowe libpng
Summary(tr):	Baþlýk dosyalarý ve statik kitaplýklar
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	zlib-devel
Obsoletes:	libpng2-devel

%description devel
The header files and static libraries are only needed for development
of programs using the PNG library.

%description devel -l de
Die Header-Dateien und statischen Libraries werden nur zur Entwicklung
von Programmen mit der PNG-Library benötigt.

%description devel -l fr
Fichiers d'en-tete et les librairies qui sont requis seulement pour le
développement avec la librairie PNG.

%description devel -l pl
W pakiecie tym znajduj± siê pliki nag³ówkowe, przeznaczone dla
programistów u¿ywaj±cych biblioteki PNG.

%description devel -l tr
PNG kitaplýðýný kullanan programlar geliþtirmek için gereken
kitaplýklar ve baþlýk dosyalarý.

%package static
Summary:	Static libpng libraries
Summary(pl):	Biblioteki statyczne libpng
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries.

%description static -l pl
Biblioteki statyczne.

%package progs
Summary:	libpng utility programs
Summary(pl):	Programy u¿ytkowe libpng
Group:		Applications/Graphics
Requires:	%{name} = %{version}

%description progs
This package contains utility programs to convert png files to and
from pnm files.

%description progs -l pl
Narzêdzia do konwersji plików png z lub do plików pnm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

ln -s scripts/makefile.linux ./Makefile

%build
%{__make} \
	CC="%{__cc}" \
	OPT_FLAGS="%{rpmcflags}" \
	prefix=%{_prefix}

%{__make} -C contrib/pngminus -f makefile.std \
	CC="%{__cc}" \
	OPT_FLAGS="%{rpmcflags} -I../../"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{3,5}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	MANPATH=%{_mandir}

install contrib/pngminus/{png2pnm,pnm2png} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES KNOWNBUG README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libpng10.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libpng*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_pkgconfigdir}/libpng*.pc
%{_mandir}/man[35]/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pn*
