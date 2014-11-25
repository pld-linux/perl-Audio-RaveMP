#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Audio
%define		pnam	RaveMP
%include	/usr/lib/rpm/macros.perl
Summary:	Audio::RaveMP Perl module - interface to Sensory Science RaveMP player
Summary(pl.UTF-8):	Moduł Perla Audio::RaveMP - interfejs do odtwarzacza Sensory Science RaveMP
Name:		perl-Audio-RaveMP
Version:	0.04
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9635c52c73fe4344919da0d0a5fca41
Patch0:		%{name}-build.patch
URL:		http://search.cpan.org/dist/Audio-RaveMP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# uses direct iob()/outb() on 0x378 port
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Audio::RaveMP module provides a Perl interface to the Sensory
Science RaveMP player.

%description -l pl.UTF-8
Moduł Audio::RaveMP udostępnia perlowy interfejs do odtwarzacza
Sensory Science RaveMP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Audio/RaveMP*.pm
%dir %{perl_vendorarch}/auto/Audio/RaveMP
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/RaveMP/*.so
%{_mandir}/man3/*
