#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	RaveMP
Summary:	Audio::RaveMP Perl module - interface to Sensory Science RaveMP player
Summary(pl):	Modu³ Perla Audio::RaveMP - interfejs do odtwarzacza Sensory Science RaveMP
Name:		perl-Audio-RaveMP
Version:	0.04
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Audio::RaveMP module provides a Perl interface to the Sensory
Science RaveMP player.

%description -l pl
Modu³ Audio::RaveMP udostêpnia perlowy interfejs do odtwarzacza
Sensory Science RaveMP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitearch}/Audio/RaveMP*.pm
%dir %{perl_sitearch}/auto/Audio/RaveMP
%{perl_sitearch}/auto/Audio/RaveMP/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Audio/RaveMP/*.so
%{_mandir}/man3/*
