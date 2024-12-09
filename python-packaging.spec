%global pypi_name packaging

Name:		python-%{pypi_name}
Version:	24.2
Release:	1
Summary:	Core utilities for Python packages
License:	BSD or ASL 2.0
Group:		Development/Python
URL:		https://github.com/pypa/packaging
Source0:	https://files.pythonhosted.org/packages/source/p/packaging/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-parsing
BuildRequires:	python-six
Requires:	python-six
Requires:	python-parsing

%description
python-packaging provides core utilities for Python
packages like utilities for dealing with versions,
specifiers, markers etc.

%package doc
Summary:	python-packaging documentation
Recommends:	%{name} = %{EVRD}
Group:		Development/Python

%description doc
Documentation for python-packaging.

%prep
%autosetup -p1 -n packaging-%{version}

%build
%py_build

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# Do not bundle fonts
rm -rf html/_static/fonts/

%install
%py_install

%files
%dir %{py3_puresitedir}/%{pypi_name}
%{py3_puresitedir}/%{pypi_name}/*
%{py3_puresitedir}/%{pypi_name}-*-info/

%files doc
%doc LICENSE LICENSE.APACHE LICENSE.BSD
