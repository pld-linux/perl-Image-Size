%include	/usr/lib/rpm/macros.perl
%define		pdir	Image
%define		pnam	Size
Summary:	Image::Size - read the dimensions of an image in several popular formats
Summary(pl.UTF-8):   Image::Size - odczyt rozmiarów obrazków w kilku popularnych formatach
Name:		perl-Image-Size
Version:	3.0
Release:	1
Epoch:		1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f77eba3d3e5ac6efcc6058f527bb180f
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Image::Size to biblioteka oparta na kodzie sprawdzającym rozmiar
obrazków w skrypcie wwwimagesize - narzędziu analizującym pliki HTML i
dodającym atrybuty HEIGHT i WIDTH do znaczników IMG. Image::Size ma
uogólniony kod tak, żeby zwracał parę (X,Y) oraz dołączone wrappery
preformatujące to wyjście do HTML-a lub zbioru par atrybutów dla
biblioteki CGI.pm Lincolna Steina.

Aktualnie Image::Size może odczytać rozmiar obrazków w formatach XPM,
XBM, GIF, JPEG, PNG, MNG, TIFF i rodzinie PPM (PPM/PGM/PBM) oraz,
jeśli zainstalowano Image::Magick, w formatach obsługiwanych przez tę
bibliotekę.

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
