%define	pdir	Image
%define	pnam	Size
%include	/usr/lib/rpm/macros.perl
Summary:	Image-Size perl module
Summary(pl):	Modu� perla Image-Size
Name:		perl-Image-Size
Version:	2.904
Release:	4

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image-Size reads the dimensions of an image in several popular
formats.

%description -l pl
Image-Size odczytuje rozmiary obrazk�w w kilku popularnych formatach.

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
