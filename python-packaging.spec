%global pypi_name packaging

%global python2_wheelname %{pypi_name}-%{version}-py2.py3-none-any.whl
%global python3_wheelname %python2_wheelname

Name:		python-%{pypi_name}
Version:	20.8
Release:	1
Summary:	Core utilities for Python packages
License:	BSD or ASL 2.0
Group:		Development/Python
URL:		https://github.com/pypa/packaging
Source0:	https://files.pythonhosted.org/packages/d7/c5/e81b9fb8033fe78a2355ea7b1774338e1dca2c9cbd2ee140211a9e6291ab/packaging-20.8.tar.gz
BuildArch:	noarch
BuildRequires:	python2-setuptools
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-parsing
BuildRequires:	python2-six
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

%package -n python2-%{pypi_name}
Summary:	%{summary}
Group:		Development/Python
%{?python_provide:%python_provide python2-%{pypi_name}}
Requires:	python2-six

%description -n python2-%{pypi_name}
python2-packaging provides core utilities for Python
packages like utilities for dealing with versions,
specifiers, markers etc.


%package doc
Summary:	python-packaging documentation
Recommends:	%{name} = %{version}-%{release}
Group:		Development/Python

%description doc
Documentation for python-packaging.

%prep
%setup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
cp -a . %{py3dir}

%build
%{__python2} setup.py build
cd %{py3dir}
%{__python3} setup.py build
cd -

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# Do not bundle fonts
rm -rf html/_static/fonts/

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
cd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
cd -

%files -n python2-%{pypi_name}
%{python2_sitelib}/%{pypi_name}/
%{python2_sitelib}/%{pypi_name}-*egg-info

%files
%{py3_puresitedir}/%{pypi_name}/
%{py3_puresitedir}/%{pypi_name}-*.egg-info/

%files doc
%doc LICENSE LICENSE.APACHE LICENSE.BSD
