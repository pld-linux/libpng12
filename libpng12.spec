Summary:	PNG library
Summary(de):	PNG-Library
Summary(es):	Biblioteca PNG
Summary(fr):	Librarie PNG
Summary(pl):	Biblioteka PNG
Summary(pt_BR):	Biblioteca PNG
Summary(tr):	PNG kitaplýðý
Name:		libpng
Version:	1.2.2
Release:	1
Epoch:		2
License:	distributable
Group:		Libraries
Source0:	http://download.sourceforge.net/libpng/%{name}-%{version}.tar.gz
Patch0:		%{name}-pngminus.patch
Patch1:		%{name}-badchunks.patch
Patch2:		%{name}-opt.patch
Patch3:		%{name}-symlinks.patch
BuildRequires:	zlib-devel
# remember to remove this if you remove libpng.so.3 symlink from %%file
Provides:	libpng.so.3
URL:		http://www.libpng.org/pub/png/libpng.html
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
Requires:	%{name} = %{version}
Requires:	zlib-devel

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
Summary(es):	Static libraries for libpng development
Summary(pl):	Biblioteki statyczne PNG
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com libpng
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static PNG libraries.

%description static -l de
Statischen PNG Libraries.

%description static -l es
Static libraries for libpng development.

%description static -l pl
Biblioteki statyczne PNG.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com libpng.

%package progs
Summary:	libpng utility programs
Summary(pl):	Narzêdzia do plików PNG
Group:		Applications/Graphics

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

ln -sf scripts/makefile.linux ./Makefile

%build
%{__make} \
	OPT_FLAGS="%{rpmcflags}"
%{__make} -C contrib/pngminus -f makefile.std \
	OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man{3,5}}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

install png.5 $RPM_BUILD_ROOT%{_mandir}/man5/
install {libpngpf,libpng}.3 $RPM_BUILD_ROOT%{_mandir}/man3/
install contrib/pngminus/{png2pnm,pnm2png} $RPM_BUILD_ROOT%{_bindir}

gzip -9nf *.txt ANNOUNCE CHANGES KNOWNBUG README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*
# for compatibility with libpng 1.2.[01]
%attr(755,root,root) %{_libdir}/*.so.3

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*
%{_includedir}/*
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
