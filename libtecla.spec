Summary:	Command-line editing library
Summary(pl.UTF-8):	Biblioteka do edycji linii poleceń
Name:		libtecla
Version:	1.6.3
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	https://sites.astro.caltech.edu/~mcs/tecla/%{name}-%{version}.tar.gz
# Source0-md5:	90105ca19e405fb92825a90978e4ab18
URL:		https://sites.astro.caltech.edu/~mcs/tecla/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tecla library provides UNIX and LINUX programs with interactive
command line editing facilities, similar to those of the UNIX tcsh
shell. In addition to simple command-line editing, it supports recall
of previously entered command lines, TAB completion of file names, and
in-line wild-card expansion of filenames. The internal functions which
perform file-name completion and wild-card expansion are also
available externally for optional use by programs, along with a module
for tab-completion and lookup of filenames in a list of directories.

%description -l pl.UTF-8
Biblioteka tecla udostępnia programom uniksowym/linuksowym możliwość
interaktywnej edycji wiersza poleceń, podobną do powłoki uniksowej
tcsh. Oprócz prostej edycji wiersza poleceń obsługuje przywoływanie
poprzednio wprowadzanych linii, dopełnianie Tabem nazw plików czy
rozwijanie masek nazw plików. Funkcje wewnętrzne wykonujące
dopełnianie nazw plików i rozwijanie masek są dostępne także z
zewnątrz, do wykorzystania przez programy, podobnie jak moduł
dopełniania Tabem i wyszukiwania nazw plików w liście katalogów.

%package devel
Summary:	Header files for tecla library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki tecla
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tecla library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tecla.

%package static
Summary:	Static tecla library
Summary(pl.UTF-8):	Statyczna biblioteka tecla
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tecla library.

%description static -l pl.UTF-8
Statyczna biblioteka tecla.

%prep
%setup -q -n %{name}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	INCDIR=$RPM_BUILD_ROOT%{_includedir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE.TERMS README RELEASE.NOTES
%attr(755,root,root) %{_bindir}/enhance
%attr(755,root,root) %{_libdir}/libtecla.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtecla.so.1
%attr(755,root,root) %{_libdir}/libtecla_r.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtecla_r.so.1
%{_mandir}/man1/enhance.1*
%{_mandir}/man5/teclarc.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtecla.so
%attr(755,root,root) %{_libdir}/libtecla_r.so
%{_includedir}/libtecla.h
%{_mandir}/man3/cfc_*.3*
%{_mandir}/man3/cpl_*.3*
%{_mandir}/man3/del_*.3*
%{_mandir}/man3/ef_*.3*
%{_mandir}/man3/gl_*.3*
%{_mandir}/man3/libtecla*.3*
%{_mandir}/man3/new_*.3*
%{_mandir}/man3/pca_*.3*
%{_mandir}/man3/ppc_*.3*
%{_mandir}/man7/tecla.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libtecla.a
%{_libdir}/libtecla_r.a
