%include	/usr/lib/rpm/macros.perl
%define		pdir	Image
%define		pnam	Size
Summary:	Image::Size - read the dimensions of an image in several popular formats
Summary(pl):	Image::Size - odczyt rozmiar�w obrazk�w w kilku popularnych formatach
Name:		perl-Image-Size
Version:	2.992
Release:	1
Epoch:		1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2e278c39a9379f5fefaf6eb288208bd8
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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
Image::Size to biblioteka oparta na kodzie sprawdzaj�cym rozmiar
obrazk�w w skrypcie wwwimagesize - narz�dziu analizuj�cym pliki HTML i
dodaj�cym atrybuty HEIGHT i WIDTH do znacznik�w IMG. Image::Size ma
uog�lniony kod tak, �eby zwraca� par� (X,Y) oraz do��czone wrappery
preformatuj�ce to wyj�cie do HTML-a lub zbioru par atrybut�w dla
biblioteki CGI.pm Lincolna Steina.

Aktualnie Image::Size mo�e odczyta� rozmiar obrazk�w w formatach XPM,
XBM, GIF, JPEG, PNG, MNG, TIFF i rodzinie PPM (PPM/PGM/PBM) oraz,
je�li zainstalowano Image::Magick, w formatach obs�ugiwanych przez t�
bibliotek�.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/imgsize
%{perl_vendorlib}/Image/Size.pm
%dir %{perl_vendorlib}/auto/Image
%dir %{perl_vendorlib}/auto/Image/Size
%{perl_vendorlib}/auto/Image/Size/autosplit.ix
%{perl_vendorlib}/auto/Image/Size/*.al
%{_mandir}/man[13]/*
