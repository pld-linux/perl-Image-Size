%include	/usr/lib/rpm/macros.perl
%define		pdir	Image
%define		pnam	Size
Summary:	Image::Size Perl module
Summary(cs):	Modul Image::Size pro Perl
Summary(da):	Perlmodul Image::Size
Summary(de):	Image::Size Perl Modul
Summary(es):	Módulo de Perl Image::Size
Summary(fr):	Module Perl Image::Size
Summary(it):	Modulo di Perl Image::Size
Summary(ja):	Image::Size Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Image::Size ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Image::Size
Summary(pl):	Modu³ Perla Image::Size
Summary(pt):	Módulo de Perl Image::Size
Summary(pt_BR):	Módulo Perl Image::Size
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Image::Size
Summary(sv):	Image::Size Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Image::Size
Summary(zh_CN):	Image::Size Perl Ä£¿é
Name:		perl-Image-Size
Version:	2.904
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image::Size reads the dimensions of an image in several popular
formats.

%description -l pl
Image::Size odczytuje rozmiary obrazków w kilku popularnych formatach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/imgsize
%{perl_sitelib}/Image/Size.pm
%dir %{perl_sitelib}/auto/Image
%dir %{perl_sitelib}/auto/Image/Size
%{perl_sitelib}/auto/Image/Size/autosplit.ix
%{perl_sitelib}/auto/Image/Size/*.al
%{_mandir}/man[13]/*
