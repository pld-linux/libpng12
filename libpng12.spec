Summary:     PNG library
Summary(de): PNG-Library
Summary(fr): Librarie PNG.
Summary(pl): Biblioteka PNG
Summary(tr): PNG kitaplýðý
Name:        libpng
Version:     1.0.2
Release:     1
Copyright:   distributable
Group:       Libraries
Source:      ftp://ftp.uu.net/graphics/png/src/%{name}-%{version}.tar.gz
Patch0:      libpng-1.0.2.patch
Icon:        png-tiny.gif
URL:         http://www.cdrom.com/pub/png/
Buildroot:   /tmp/%{name}-%{version}-root

%description
The PNG library is a collection of routines used to crate and manipulate
PNG format graphics files.  The PNG format was designed as a replacement
for GIF, with many improvements and extensions.

%description -l de
Die PNG-Library ist eine Sammlung von Routinen zum Erstellen und Bearbeiten
von Grafiken im PNG-Format. Das PNG-Format wurde als Ersatz für GIF
entwickelt und enthält viele Verbesserungen und Erweiterungen.

%description -l fr
La librairie PNG est un ensemble de routines utilisées pour créer et 
manipuler des fichiers graphiques au format PNG. Le format PNG a été
élaboré pour remplacer le GIF, avec de nombreuses améliorations et
extensions.

%description -l tr
PNG kitaplýðý, PNG formatýndaki resim dosyalarýný iþlemeye yönelik yordamlarý
içerir. PNG, GIF formatýnýn yerini almak üzere tasarlanmýþ bir resim formatýdýr.

%package devel
Summary:     header files an documentation for PNG library
Summary(pl): Pliki nag³owkowe i dokumentacja do biblioteki PNG
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
The header files and static libraries are only needed for development
of programs using the PNG library.

%description -l de devel
Die Header-Dateien und statischen Libraries werden nur zur Entwicklung
von Programmen mit der PNG-Library benötigt.

%description -l fr devel
Fichiers d'en-tete et les librairies qui sont requis seulement pour
le développement avec la librairie PNG.

%description -l tr devel
PNG kitaplýðýný kullanan programlar geliþtirmek için gereken kitaplýklar ve
baþlýk dosyalarý.

%package static
Summary:     PNG static library
Summary(pl): Biblioteka PNG - wersja statyczna
Group:       Development/Libraries
Requires:    %{name}-devel = %{version}

%description static
The static PNG library.

%description -l pl static
Bibliotek PNG - wersja statyczna

%prep
%setup -q
%patch0 -p1

%ifos Linux
ln -sf scripts/makefile.lnx Makefile
%endif

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/man/man3

make install prefix=$RPM_BUILD_ROOT/usr
install {libpng,libpngpf}.3 $RPM_BUILD_ROOT/usr/man/man3

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755, root, root) /usr/lib/lib*.so.*.*

%files devel
%defattr(644, root, root, 755)
%doc *.txt example.c
/usr/include/*
/usr/lib/lib*.so
%attr(644, root,  man) /usr/man/man3/*

%files static
%attr(644, root, root) /usr/lib/lib*.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Aug  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.2-1]
- added pl translation,
- added -q %setup parameter,
- added using %%{name} and %%{version} macros in Buildroot,
- added %clean section,
- added package icon,
- added URL,
- added stripping sharebd lib,
- added "%ifos Linux .. %endif" around making sym link to proper Makefile,
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- added man pages to devel,
- added static subpackage,
- Rquires in devel changed to "%%{name} %%{version}"
- changed permission on shared libs to 755 (now ldd output on this files is
  correct),
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

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
