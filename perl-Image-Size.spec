%include	/usr/lib/rpm/macros.perl
Summary:	Image-Size perl module
Summary(pl):	Modu³ perla Image-Size
Name:		perl-Image-Size
Version:	2.901
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Image/Image-Size-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Image-Size reads the dimensions of an image in several popular formats.

%description -l pl
Image-Size odczytuje rozmiary obrazków w kilku popularnych formatach.

%prep
%setup -q -n Image-Size-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Image/Size
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/imgsize

%{perl_sitelib}/Image/Size.pm
%{perl_sitelib}/auto/Image/Size

%{perl_sitearch}/auto/Image/Size

%{_mandir}/man[13]/*
