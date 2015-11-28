%define 	module	googlemaps
Summary:	Python wrapper for the Google Maps and Local Search APIs
Name:		python-%{module}
Version:	1.0.2
Release:	3
License:	AGPL v3
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/project/py-googlemaps/googlemaps-%{version}.tar.gz
# Source0-md5:	314b5c32f083a2070efcec7f3942f6c8
URL:		http://sourceforge.net/projects/py-googlemaps/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy-to-use Python wrapper for the Google Maps and Local Search APIs.
Provides geocoding, reverse geocoding, directions, and local search.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/html/*
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/googlemaps-*.egg-info
%endif
