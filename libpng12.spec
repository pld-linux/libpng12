Summary:	PNG library
Summary(de):	PNG-Library
Summary(fr):	Librarie PNG.
Summary(pl):	Biblioteki PNG 
Summary(tr):	PNG kitaplýðý
Name:		libpng
Version:	1.0.3
Release:	4
Copyright:	distributable
Group:		Libraries
Group(pl):	Biblioteki
Serial:		1
Source:		ftp://ftp.uu.net/graphics/png/src/%{name}-%{version}.tar.gz
Patch:          libpng-opt.patch
Buildroot:	/tmp/%{name}-%{version}-root
Conflicts:	glibc <= 2.0.7

%description
The PNG library is a collection of routines used to crate and manipulate
PNG format graphics files.  The PNG format was designed as a replacement
for GIF, with many improvements and extensions.

%description -l pl
Biblioteki PNG s± kolekcj± form u¿ywanych do tworzenia i manipulowania
plikami w formatacie graficznym PNG. format ten zosta³ stworzony jako
zamiennik dla formatu GIF, z wieloma rozszerzeniami i nowo¶ciami.

%package devel
Summary:	headers 
Summary(de):	Headers und statische Libraries 
Summary(fr):	en-têtes et bibliothèques statiques
Summary(pl):	Pliki nag³ówkowe
Summary(tr):	baþlýk dosyalarý ve statik kitaplýklar
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The header files and static libraries are only needed for development
of programs using the PNG library.

%description -l pl devel
W pakiecie tym znajduj± siê pliki nag³ówkowe, przeznaczone dla programistów 
u¿ywaj±cych bibliotek PNG.

%description -l de devel
Die Header-Dateien und statischen Libraries werden nur zur Entwicklung
von Programmen mit der PNG-Library benötigt.

%description -l de
Die PNG-Library ist eine Sammlung von Routinen zum Erstellen und Bearbeiten
von Grafiken im PNG-Format. Das PNG-Format wurde als Ersatz für GIF
entwickelt und enthält viele Verbesserungen und Erweiterungen.

%description -l fr devel
Fichiers d'en-tete et les librairies qui sont requis seulement pour
le développement avec la librairie PNG.

%description -l fr
La librairie PNG est un ensemble de routines utilisées pour créer et 
manipuler des fichiers graphiques au format PNG. Le format PNG a été
élaboré pour remplacer le GIF, avec de nombreuses améliorations et
extensions.

%description -l tr devel
PNG kitaplýðýný kullanan programlar geliþtirmek için gereken kitaplýklar ve
baþlýk dosyalarý.

%description -l tr
PNG kitaplýðý, PNG formatýndaki resim dosyalarýný iþlemeye yönelik yordamlarý
içerir. PNG, GIF formatýnýn yerini almak üzere tasarlanmýþ bir resim formatýdýr.

%package	static
Summary:	static libraries
Summary(pl):	Biblioteki statyczne
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
static libraries

%description -l pl static
Biblioteki statyczne

%prep
%setup -q
%patch -p1
ln -s scripts/makefile.lnx ./Makefile

%build
make  

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{lib,man/man{3,5}}

make prefix=$RPM_BUILD_ROOT/usr install

bzip2 -9 *.txt ANNOUNCE CHANGES KNOWNBUG README

install png.5 $RPM_BUILD_ROOT/usr/man/man5/
install {libpngpf,libpng}.3 $RPM_BUILD_ROOT/usr/man/man3/

strip $RPM_BUILD_ROOT/usr/lib/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755,root,root) /usr/lib/*.so.*.*
%attr(644,root,root) /usr/man/man5/*

%files devel
%defattr(644,root,root,755)
%doc {*.txt,ANNOUNCE,CHANGES,KNOWNBUG,README}.bz2
%attr(755,root,root) /usr/lib/lib*.so
/usr/include/*
/usr/man/man3/*

%files static
%attr(644,root,root) /usr/lib/lib*.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Mar  5 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.3-4]
- added striping shared libraries,
- added "Conflicts: glibc <= 2.0.7" fr prevent installing package
  in proper enviroment,
- added installing man pages.

* Fri Jan 22 1999 Pawe³ Gajda <pagaj@shadow.eu.org>
  [1.0.3-1d]
- all files install now into /usr

* Sun Nov 15 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [1.0.2-1d]
- added some docs files,
- added %%lang macros.

* Thu Jul 16 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.0.1-5d]
- build against glibc-2.1,
- added pl translation,
- moved %changelog at the end of spec,
- changed permisions of *.so libs to 755,
- addes static subpackage.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- devel subpackage moved to Development/Libraries

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.0.1
- added buildroot

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- updated to new version
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
