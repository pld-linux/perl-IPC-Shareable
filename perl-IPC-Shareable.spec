#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IPC
%define	pnam	Shareable
Summary:	IPC::Shareable - share Perl variables between processes
Summary(pl):	IPC::Shareable - wspó³dzielenie zmiennych Perla miêdzy procesami
Name:		perl-IPC-Shareable
Version:	0.60
Release:	3
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	51462dabfb4eec81e0b3417a9f9add4e
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-Storable >= 0.607}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::Shareable allows you to tie a variable to shared memory making it
easy to share the contents of that variable with other Perl processes.
Scalars, arrays, and hashes can be tied.  The variable being tied may
contain arbitrarily complex data structures - including references to
arrays, hashes of hashes, etc.

%description -l pl
Modu³ IPC::Shareable pozwala zwi±zaæ zmienn± z pamiêci± dzielon±, co
u³atwia wspó³dzielenie zawarto¶ci tej zmiennej z innymi procesami
Perla. Wi±zane mog± byæ skalary, tablice i hasze. Powi±zana zmienna
mo¿e zawieraæ dowolnie skomplikowane struktury danych - w³±czenie z
referencjami do tablic, haszy haszy itd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__perl} -pi -e 's/^(require 5.005)(03;)$/$1_$2/' ./lib/IPC/Shareable.pm

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS DISCLAIMER README TO_DO
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
