%include	/usr/lib/rpm/macros.perl
%define		pdir	Image
%define		pnam	Size
Summary:	Image::Size reads the dimensions of an image in several popular formats
Summary(pl):	Image::Size odczytuje rozmiary obrazków w kilku popularnych formatach
Name:		perl-Image-Size
Version:	2.991
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Image::Magick)'

%description
Image::Size is a library based on the image-sizing code in the
wwwimagesize script, a tool that analyzes HTML files and adds HEIGHT
and WIDTH tags to IMG directives.  Image::Size has generalized that
code to return a raw (X, Y) pair, and included wrappers to pre-format
that output into either HTML or a set of attribute pairs suitable for
the CGI.pm library by Lincoln Stein.

Currently, Image::Size can size images in XPM, XBM, GIF, JPEG, PNG,
MNG, TIFF, the PPM family of formats (PPM/PGM/PBM) and if
Image::Magick is installed, the formats supported by it.

%description -l pl
Image::Size to biblioteka oparta na kodzie sprawdzaj±cym rozmiar
obrazków w skrypcie wwwimagesize - narzêdziu analizuj±cym pliki HTML i
dodaj±cym atrybuty HEIGHT i WIDTH do znaczników IMG. Image::Size ma
uogólniony kod tak, ¿eby zwraca³ parê (X,Y) oraz do³±czone wrappery
preformatuj±ce to wyj¶cie do HTML-a lub zbioru par atrybutów dla
biblioteki CGI.pm Lincolna Steina.

Aktualnie Image::Size mo¿e odczytaæ rozmiar obrazków w formatach XPM,
XBM, GIF, JPEG, PNG, MNG, TIFF i rodzinie PPM (PPM/PGM/PBM) oraz,
je¶li zainstalowano Image::Magick, w formatach obs³ugiwanych przez tê
bibliotekê.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
