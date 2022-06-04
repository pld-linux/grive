%define		commit		27817e835fe115ebbda5410ec904aa49a2ad01f1
# bash: %%(c=%{commit}; echo ${c:0:7})
%define		shortcommit	27817e8
%define		cdate		20130702
%define		rel		41
Summary:	An open source Linux client for Google Drive
Summary(pl.UTF-8):	Linuksowy, mające otwarte źródła klient Google Drive
Name:		grive
Version:	0.3.0
Release:	0.%{cdate}git%{shortcommit}.%{rel}
License:	GPL v2
Group:		Applications/Networking
Source0:	https://github.com/Grive/grive/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# Source0-md5:	4f3c3411588f889801bd5b9297e6e2c9
# https://github.com/Grive/grive/issues/187
Patch0:		json-c.patch
Patch1:		%{name}-bgrive_cmake_fix.patch
Patch2:		build.patch
Patch3:		binutils-2.34.patch
Patch4:		%{name}-json-c-0.14.patch
URL:		https://github.com/Grive/grive
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	binutils-devel
BuildRequires:	boost-devel >= 1.40.0
BuildRequires:	cmake >= 2.8
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	json-c-devel >= 0.11
BuildRequires:	libgcrypt-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	yajl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of this project is to provide an independent
implementation of Google Drive client. It uses the Google Document
List API to talk to the servers in Google.

%description -l pl.UTF-8
Celem tego projektu jest zapewnienie niezależnej implementacji klienta
Google Drive. Do komunikacji z serwerami Google'a wykorzystuje API
Google Document List.

%package -n bgrive
Summary:	Qt frontend for Grive
Summary(pl.UTF-8):	Interfejs Qt do Grive
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description -n bgrive
GUI frontend for Grive.

%description -n bgrive -l pl.UTF-8
Graficzny interfejs użytkownika do Grive.

%prep
%setup -q -n %{name}-%{commit}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/grive
%{_mandir}/man1/grive.1*

%files -n bgrive
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bgrive
