Summary:	PNG library
Summary(de):	PNG-Library
Summary(fr):	Librarie PNG
Summary(pl):	Biblioteka PNG 
Summary(tr):	PNG kitaplığı
Name:		libpng
Version:	1.2.0
Release:	2
Epoch:		2
License:	distributable
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
Source0:	http://download.sourceforge.net/libpng/%{name}-%{version}.tar.gz
Patch0:		%{name}-pngminus.patch
Patch1:		%{name}-badchunks.patch
Patch2:		%{name}-opt.patch
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

%description -l fr
La librairie PNG est un ensemble de routines utilisées pour créer et
manipuler des fichiers graphiques au format PNG. Le format PNG a été
élaboré pour remplacer le GIF, avec de nombreuses améliorations et
extensions.

%description -l pl
Biblioteki PNG s± kolekcj± form u¿ywanych do tworzenia i manipulowania
plikami w formacie graficznym PNG. Format ten zosta³ stworzony jako
zamiennik dla formatu GIF, z wieloma rozszerzeniami i nowo¶ciami.

%description -l tr
PNG kitaplığı, PNG formatındaki resim dosyalarını işlemeye yönelik
yordamları içerir. PNG, GIF formatının yerini almak üzere tasarlanmış
bir resim formatıdır.

%package devel
Summary:	Header files for libpng
Summary(de):	libpng Headers
Summary(fr):	en-têtes et bibliothèques statiques
Summary(pl):	Pliki nag³ówkowe libpng
Summary(tr):	başlık dosyaları ve statik kitaplıklar
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}
Requires:	zlib-devel

%description devel
The header files are only needed for development of programs using the
PNG library.

%description -l pl devel
W pakiecie tym znajduj± siê pliki nag³ówkowe, przeznaczone dla
programistów u¿ywaj±cych bibliotek PNG.

%description -l de devel
Die Header-Dateien werden nur zur Entwicklung von Programmen mit der
PNG-Library benötigt.

%description -l fr devel
Fichiers d'en-tete et les librairies qui sont requis seulement pour le
développement avec la librairie PNG.

%description -l tr devel
PNG kitaplığını kullanan programlar geliştirmek için gereken
kitaplıklar ve başlık dosyaları.

%package static
Summary:	Static PNG libraries
Summary(de):	Statischen PNG Libraries
Summary(pl):	Biblioteki statyczne PNG
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static PNG libraries.

%description -l de static
Statischen PNG Libraries.

%description -l pl static
Biblioteki statyczne PNG.

%package progs
Summary:	libpng utility programs
Summary(pl):	Narzêdzia do plików PNG
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Group(pt):	Aplicações/Gráficos

%description progs
This package contains utility programs to convert png files to and
from pnm files.

%description -l pl progs
Narzêdzia do konwersji plików png z lub do plików pnm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

ln -sf scripts/makefile.linux ./Makefile

%build
%{__make} OPT_FLAGS="%{rpmcflags}"
cd contrib/pngminus
%{__make} -f makefile.std \
	OPT_FLAGS="%{rpmcflags} -I../../"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man{3,5}}

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

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

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
