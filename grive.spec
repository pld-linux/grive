Summary:	An open source Linux client for Google Drive
Name:		grive
Version:	0.2.0
Release:	3
License:	GPL v2
Group:		Applications/Networking
URL:		http://www.lbreda.com/grive/
Source0:	http://www.lbreda.com/grive/_media/packages/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8260b1e6c0369da35ebcfe8c8f840f2b
BuildRequires:	binutils-devel
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	json-c-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of this project is to provide an independent
implementation of Google Drive client. It uses the Google Document
List API to talk to the servers in Google. The code is written in
standard C++.

%prep
%setup -q

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
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/grive.1*
