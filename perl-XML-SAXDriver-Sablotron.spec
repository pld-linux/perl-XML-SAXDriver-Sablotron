#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	XML
%define		pnam	SAXDriver-Sablotron
%include	/usr/lib/rpm/macros.perl
Summary:	XML::SAXDriver::Sablotron perl module
Summary(pl.UTF-8):	Moduł perla XML::SAXDriver::Sablotron
Name:		perl-XML-SAXDriver-Sablotron
Version:	0.30
Release:	2
License:	GPL v2+ or MPL v1.1
Group:		Development/Languages/Perl
#Source0Download:	http://www.gingerall.com/charlie/ga/xml/d_sab.xml
Source0:	http://download-1.gingerall.cz/download/sablot/XML-SAXDriver-Sablotron-%{version}.tar.gz
# Source0-md5:	785db592e5ca705b3732816cbbd1d1f3
URL:		http://search.cpan.org/dist/XML-SAXDriver-Sablotron/
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-Sablotron
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SAXDriver::Sablotron is a SAX2 driver based on Sablotron XSLT
processor. An XSLT transformation result is outputted as a stream of
SAX2 events. The result tree is not build at all - SAX2 events are
emitted directly instead.

%description -l pl.UTF-8
XML::SAXDriver::Sablotron to sterownik SAX2 bazujący na procesorze
XSLT Sablotron. Wyjściem transformacji XSLT jest strumień zdarzeń
SAX2. Wynikowe drzewo nie jest budowane - zdarzenia SAX2 są wywoływane
bezpośrednio.

%prep
%setup -q -n XML-SAXDriver-Sablotron-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%dir %{perl_vendorlib}/XML/SAXDriver
%{perl_vendorlib}/XML/SAXDriver/Sablotron.pm
%{_mandir}/man3/*
