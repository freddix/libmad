Summary:	MPEG audio decoder library
Name:		libmad
Version:	0.15.1b
Release:	13
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
# Source0-md5:	1be543bc30c56fb6bea1d7bf6a64e66c
Patch0:		%{name}-amd64-64bit.patch
Patch1:		%{name}-pkgconfig.patch
Patch2:		%{name}-frame-length.patch
Patch3:		%{name}-optimize.patch
URL:		http://www.underbit.com/products/mad/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Provides:	mad-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags   -ftree-vectorize -ftree-vectorizer-verbose=1

%description
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2 extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II
and Layer III a.k.a. MP3) are fully implemented.

%package devel
Summary:	Header files for libmad library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	mad-devel = %{version}

%description devel
Header files for libmad library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-debugging	\
	--disable-static	\
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYRIGHT CREDITS README TODO
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

