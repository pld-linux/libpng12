Summary:	PNG library
Summary(de):	PNG-Library
Summary(es):	Biblioteca PNG
Summary(fr):	Librarie PNG
Summary(pl):	Biblioteka PNG
Summary(pt_BR):	Biblioteca PNG
Summary(tr):	PNG kitaplýðý
Name:		libpng
Version:	1.2.6
%define	_pre	rc1
Release:	0.%{_pre}.2
Epoch:		2
License:	distributable
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/libpng/%{name}-%{version}%{_pre}.tar.bz2
# Source0-md5:	346bd648912e31fd4ff900b25979f5f2
Patch0:		%{name}-pngminus.patch
Patch1:		%{name}-badchunks.patch
Patch2:		%{name}-opt.patch
Patch3:		%{name}-revert.patch
Patch4:		%{name}-norpath.patch
Patch5:		%{name}-libdirfix.patch
Patch6:		%{name}-irowbytes.patch
URL:		http://www.libpng.org/pub/png/libpng.html
BuildRequires:	zlib-devel
%ifarch amd64 ia64 ppc64 s390x sparc64
Provides:	libpng.so.3()(64bit)
%else
Provides:	libpng.so.3
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PNG library is a collection of routines used to create and
manipulate PNG format graphics files. The PNG format was designed as a
replacement for GIF, with many improvements and extensions.

%description -l de
Die PNG-Library ist eine Sammlung von Routinen zum Erstellen und
Bearbeiten von Grafiken im PNG-Format. Das PNG-Format wurde als Ersatz
für GIF entwickelt und enthält viele Verbesserungen und Erweiterungen.

%description -l es
Esta biblioteca es una colección de rutinas para crear y manipular
archivos gráficos en el formato PNG. Este formato fue proyectado para
substituir el

%description -l fr
La librairie PNG est un ensemble de routines utilisées pour créer et
manipuler des fichiers graphiques au format PNG. Le format PNG a été
élaboré pour remplacer le GIF, avec de nombreuses améliorations et
extensions.

%description -l pl
Biblioteki PNG s± kolekcj± form u¿ywanych do tworzenia i manipulowania
plikami w formacie graficznym PNG. Format ten zosta³ stworzony jako
zamiennik dla formatu GIF, z wieloma rozszerzeniami i nowo¶ciami.

%description -l pt_BR
Esta biblioteca é uma coleção de rotinas para criar e manipular
arquivos gráficos no formato PNG. Este formato foi projetado para
substituir o formato GIF, com extensões e melhorias.

%description -l tr
PNG kitaplýðý, PNG formatýndaki resim dosyalarýný iþlemeye yönelik
yordamlarý içerir. PNG, GIF formatýnýn yerini almak üzere tasarlanmýþ
bir resim formatýdýr.

%package devel
Summary:	Header files for libpng
Summary(de):	libpng Headers
Summary(es):	Archivos de inclusión y bibliotecas estáticas
Summary(fr):	en-têtes et bibliothèques statiques
Summary(pl):	Pliki nag³ówkowe libpng
Summary(pt_BR):	Arquivos de inclusão e bibliotecas estáticas
Summary(tr):	baþlýk dosyalarý ve statik kitaplýklar
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	zlib-devel
Conflicts:	libpng < 1.0.15

%description devel
The header files are only needed for development of programs using the
PNG library.

%description devel -l de
Die Header-Dateien werden nur zur Entwicklung von Programmen mit der
PNG-Library benötigt.

%description devel -l es
Archivos de inclusión y bibliotecas estáticas que son necesarios
solamente para el desarrollo de programas que usan la biblioteca PNG.

%description devel -l fr
Fichiers d'en-tete et les librairies qui sont requis seulement pour le
développement avec la librairie PNG.

%description devel -l pl
W pakiecie tym znajduj± siê pliki nag³ówkowe, przeznaczone dla
programistów u¿ywaj±cych bibliotek PNG.

%description devel -l pt_BR
Arquivos de inclusão e bibliotecas estáticas que são necessários
somente para o desenvolvimento de programas que usam a biblioteca PNG.

%description devel -l tr
PNG kitaplýðýný kullanan programlar geliþtirmek için gereken
kitaplýklar ve baþlýk dosyalarý.

%package static
Summary:	Static PNG libraries
Summary(de):	Statischen PNG Libraries
Summary(pl):	Biblioteki statyczne PNG
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com libpng
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static PNG libraries.

%description static -l de
Statischen PNG Libraries.

%description static -l pl
Biblioteki statyczne PNG.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com libpng.

%package progs
Summary:	libpng utility programs
Summary(pl):	Narzêdzia do plików PNG
Group:		Applications/Graphics

%description progs
This package contains utility programs to convert PNG files to and
from PNM files.

%description progs -l pl
Narzêdzia do konwersji plików PNG z lub do plików PNM.

%prep
%setup -q -n %{name}-%{version}%{_pre}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%ifarch %{ix86}
ln -sf scripts/makefile.gcmmx ./Makefile
%else
ln -sf scripts/makefile.linux ./Makefile
%endif

%build
%{__make} \
	prefix=%{_prefix} \
	LIBPATH=%{_libdir} \
	CC="%{__cc}" \
	OPT_FLAGS="%{rpmcflags}"
%{__make} -C contrib/pngminus -f makefile.std \
	LIBPATH=%{_libdir} \
	CC="%{__cc}" \
	OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man{3,5}} \
	$RPM_BUILD_ROOT{%{_pkgconfigdir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	LIBPATH=%{_libdir} \
	MANPATH=%{_mandir}

install contrib/pngminus/{png2pnm,pnm2png} $RPM_BUILD_ROOT%{_bindir}
install example.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES KNOWNBUG README LICENSE
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_libdir}/libpng.so.3

%files devel
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/libpng*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*
%{_includedir}/*
%{_mandir}/man?/*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/p*
