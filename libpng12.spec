Summary:	PNG library
Summary(de.UTF-8):	PNG-Library
Summary(es.UTF-8):	Biblioteca PNG
Summary(fr.UTF-8):	Librarie PNG
Summary(pl.UTF-8):	Biblioteka PNG
Summary(pt_BR.UTF-8):	Biblioteca PNG
Summary(tr.UTF-8):	PNG kitaplığı
Name:		libpng
Version:	1.4.0
Release:	0.1
Epoch:		2
License:	distributable
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libpng/%{name}-%{version}.tar.xz
# Source0-md5:	2ce652ebe1589d7b2357aa6d0eccd07c
Patch0:		%{name}-pngminus.patch
# http://littlesvr.ca/apng/diff/%{name}-%{version}-apng.patch | dos2unix
Patch1:		%{name}-apng.patch
URL:		http://www.libpng.org/pub/png/libpng.html
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	xz >= 1:4.999.7
BuildRequires:	zlib-devel
Provides:	libpng(APNG) = 0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PNG library is a collection of routines used to create and
manipulate PNG format graphics files. The PNG format was designed as a
replacement for GIF, with many improvements and extensions.

%description -l de.UTF-8
Die PNG-Library ist eine Sammlung von Routinen zum Erstellen und
Bearbeiten von Grafiken im PNG-Format. Das PNG-Format wurde als Ersatz
für GIF entwickelt und enthält viele Verbesserungen und Erweiterungen.

%description -l es.UTF-8
Esta biblioteca es una colección de rutinas para crear y manipular
archivos gráficos en el formato PNG. Este formato fue proyectado para
substituir el

%description -l fr.UTF-8
La librairie PNG est un ensemble de routines utilisées pour créer et
manipuler des fichiers graphiques au format PNG. Le format PNG a été
élaboré pour remplacer le GIF, avec de nombreuses améliorations et
extensions.

%description -l pl.UTF-8
Biblioteki PNG są kolekcją form używanych do tworzenia i manipulowania
plikami w formacie graficznym PNG. Format ten został stworzony jako
zamiennik dla formatu GIF, z wieloma rozszerzeniami i nowościami.

%description -l pt_BR.UTF-8
Esta biblioteca é uma coleção de rotinas para criar e manipular
arquivos gráficos no formato PNG. Este formato foi projetado para
substituir o formato GIF, com extensões e melhorias.

%description -l tr.UTF-8
PNG kitaplığı, PNG formatındaki resim dosyalarını işlemeye yönelik
yordamları içerir. PNG, GIF formatının yerini almak üzere tasarlanmış
bir resim formatıdır.

%package devel
Summary:	Header files for libpng
Summary(de.UTF-8):	libpng Headers
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas estáticas
Summary(fr.UTF-8):	en-têtes et bibliothèques statiques
Summary(pl.UTF-8):	Pliki nagłówkowe libpng
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas estáticas
Summary(tr.UTF-8):	başlık dosyaları ve statik kitaplıklar
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	zlib-devel
Provides:	libpng(APNG)-devel = 0.10
Conflicts:	libpng < 1.0.15

%description devel
The header files are only needed for development of programs using the
PNG library.

%description devel -l de.UTF-8
Die Header-Dateien werden nur zur Entwicklung von Programmen mit der
PNG-Library benötigt.

%description devel -l es.UTF-8
Archivos de inclusión y bibliotecas estáticas que son necesarios
solamente para el desarrollo de programas que usan la biblioteca PNG.

%description devel -l fr.UTF-8
Fichiers d'en-tete et les librairies qui sont requis seulement pour le
développement avec la librairie PNG.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających bibliotek PNG.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão e bibliotecas estáticas que são necessários
somente para o desenvolvimento de programas que usam a biblioteca PNG.

%description devel -l tr.UTF-8
PNG kitaplığını kullanan programlar geliştirmek için gereken
kitaplıklar ve başlık dosyaları.

%package static
Summary:	Static PNG libraries
Summary(de.UTF-8):	Statischen PNG Libraries
Summary(pl.UTF-8):	Biblioteki statyczne PNG
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libpng
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	libpng(APNG)-static = 0.10

%description static
Static PNG libraries.

%description static -l de.UTF-8
Statischen PNG Libraries.

%description static -l pl.UTF-8
Biblioteki statyczne PNG.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libpng.

%package progs
Summary:	libpng utility programs
Summary(pl.UTF-8):	Narzędzia do plików PNG
Group:		Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description progs
This package contains utility programs to convert PNG files to and
from PNM files.

%description progs -l pl.UTF-8
Narzędzia do konwersji plików PNG z lub do plików PNM.

%prep
%setup -q -c -T
xzcat -dc %{SOURCE0} | tar xf - -C ..
%patch0 -p1
%patch1 -p0

%build
%configure
%{__make}

%{__make} -C contrib/pngminus -f makefile.std \
	LIBPATH=%{_libdir} \
	CC="%{__cc}" \
	OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install contrib/pngminus/{png2pnm,pnm2png} $RPM_BUILD_ROOT%{_bindir}
install example.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES LICENSE README TODO
%attr(755,root,root) %{_libdir}/libpng14.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpng14.so.14

%files devel
%defattr(644,root,root,755)
%doc libpng-%{version}.txt
%attr(755,root,root) %{_bindir}/libpng14-config
%attr(755,root,root) %{_bindir}/libpng-config
%attr(755,root,root) %{_libdir}/libpng14.so
%attr(755,root,root) %{_libdir}/libpng.so
%{_libdir}/libpng14.la
%{_libdir}/libpng.la
%{_pkgconfigdir}/libpng14.pc
%{_pkgconfigdir}/libpng.pc
%{_includedir}/libpng14
%{_includedir}/png*.h
%{_mandir}/man3/libpng.3*
%{_mandir}/man3/libpngpf.3*
%{_mandir}/man5/png.5*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libpng14.a
%{_libdir}/libpng.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/png2pnm
%attr(755,root,root) %{_bindir}/pnm2png
