%global pypi_name packaging
%global python3_wheelname %python2_wheelname

Name:		python-%{pypi_name}
Version:	21.3
Release:	2
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
%{?python_provide:%python_provide python3-%{pypi_name}}
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
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
cp -a . %{py3dir}

%build
%py3_build

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# Do not bundle fonts
rm -rf html/_static/fonts/

%install
%py3_install

%files
%dir %{py3_puresitedir}/%{pypi_name}
%{py3_puresitedir}/%{pypi_name}/*
%{py3_puresitedir}/%{pypi_name}-*.egg-info/

%files doc
%doc LICENSE LICENSE.APACHE LICENSE.BSD
