%include	/usr/lib/rpm/macros.perl
Summary:	XML::SAXDriver::Sablotron perl module
Summary(pl):	Modu³ perla XML::SAXDriver::Sablotron
Name:		perl-XML-Sablotron
Version:	0.20
Release:	1
License:	GPL or MPLv1.1
Group:		Development/Languages/Perl
Source0:	http://download-2.gingerall.cz/download/sablot/XML-SAXDriver-Sablotron-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-Sablotron
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{perl_sitelib}/XML/SAXDriver
%{perl_sitelib}/XML/SAXDriver/Sablotron.pm
%{_mandir}/man3/*
