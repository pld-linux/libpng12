Summary:	PNG library
Summary(de):	PNG-Library
Summary(fr):	Librarie PNG
Summary(pl):	Biblioteka PNG 
Summary(tr):	PNG kitaplýðý
Name:		libpng
Version:	1.0.7
Release:	1
Copyright:	distributable
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Serial:		1
Source0:	ftp://ftp.uu.net/graphics/png/src/%{name}-%{version}.tar.gz
Patch0:		libpng-opt.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PNG library is a collection of routines used to create and
manipulate PNG format graphics files. The PNG format was designed as a
replacement for GIF, with many improvements and extensions.

%description -l pl
Biblioteki PNG s± kolekcj± form u¿ywanych do tworzenia i manipulowania
plikami w formatacie graficznym PNG. Format ten zosta³ stworzony jako
zamiennik dla formatu GIF, z wieloma rozszerzeniami i nowo¶ciami.

%description -l de
Die PNG-Library ist eine Sammlung von Routinen zum Erstellen und
Bearbeiten von Grafiken im PNG-Format. Das PNG-Format wurde als Ersatz
für GIF entwickelt und enthält viele Verbesserungen und Erweiterungen.

%description -l fr
La librairie PNG est un ensemble de routines utilisées pour créer et
manipuler des fichiers graphiques au format PNG. Le format PNG a été
élaboré pour remplacer le GIF, avec de nombreuses améliorations et
extensions.

%description -l tr
PNG kitaplýðý, PNG formatýndaki resim dosyalarýný iþlemeye yönelik
yordamlarý içerir. PNG, GIF formatýnýn yerini almak üzere tasarlanmýþ
bir resim formatýdýr.

%package devel
Summary:	headers 
Summary(de):	Headers und statische Libraries 
Summary(fr):	en-têtes et bibliothèques statiques
Summary(pl):	Pliki nag³ówkowe
Summary(tr):	baþlýk dosyalarý ve statik kitaplýklar
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The header files and static libraries are only needed for development
of programs using the PNG library.

%description -l pl devel
W pakiecie tym znajduj± siê pliki nag³ówkowe, przeznaczone dla
programistów u¿ywaj±cych bibliotek PNG.

%description -l de devel
Die Header-Dateien und statischen Libraries werden nur zur Entwicklung
von Programmen mit der PNG-Library benötigt.

%description -l fr devel
Fichiers d'en-tete et les librairies qui sont requis seulement pour le
développement avec la librairie PNG.

%description -l tr devel
PNG kitaplýðýný kullanan programlar geliþtirmek için gereken
kitaplýklar ve baþlýk dosyalarý.

%package	static
Summary:	static libraries
Summary(pl):	Biblioteki statyczne
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries.

%description -l pl static
Biblioteki statyczne.

%prep
%setup -q
%patch -p1
ln -s scripts/makefile.linux ./Makefile

%build
%{__make}  

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man{3,5}}

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

install png.5 $RPM_BUILD_ROOT%{_mandir}/man5/
install {libpngpf,libpng}.3 $RPM_BUILD_ROOT%{_mandir}/man3/

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	*.txt ANNOUNCE CHANGES KNOWNBUG README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%doc {*.txt,ANNOUNCE,CHANGES,KNOWNBUG,README}.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
