#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	XML::SAXDriver::Sablotron perl module
Summary(pl):	Modu³ perla XML::SAXDriver::Sablotron
Name:		perl-XML-SAXDriver-Sablotron
Version:	0.30
Release:	2
License:	GPL v2+ or MPL v1.1
Group:		Development/Languages/Perl
Source0:	http://download-2.gingerall.cz/download/sablot/XML-SAXDriver-Sablotron-%{version}.tar.gz
# Source0-md5:	785db592e5ca705b3732816cbbd1d1f3
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-Sablotron
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SAXDriver::Sablotron is a SAX2 driver based on Sablotron XSLT
processor. An XSLT transformation result is outputted as a stream of
SAX2 events. The result tree is not build at all - SAX2 events are
emitted directly instead.

%description -l pl
XML::SAXDriver::Sablotron to sterownik SAX2 bazuj±cy na procesorze
XSLT Sablotron. Wyj¶ciem transformacji XSLT jest strumien zdarzeñ
SAX2. Wynikowe drzewo nie jest budowane - zdarzenia SAX2 s± wywo³ywane
bezpo¶rednio.

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
