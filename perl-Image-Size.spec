%include	/usr/lib/rpm/macros.perl
Summary:	Image-Size perl module
Summary(pl):	Modu³ perla Image-Size
Name:		perl-Image-Size
Version:	2.904
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Image/Image-Size-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image-Size reads the dimensions of an image in several popular
formats.

%description -l pl
Image-Size odczytuje rozmiary obrazków w kilku popularnych formatach.

%prep
%setup -q -n Image-Size-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/imgsize
%{perl_sitelib}/Image/Size.pm
%{perl_sitelib}/auto/Image/Size
%{_mandir}/man[13]/*
