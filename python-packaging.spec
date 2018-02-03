%global pypi_name packaging

%global python2_wheelname %{pypi_name}-%{version}-py2.py3-none-any.whl
%global python3_wheelname %python2_wheelname

Name:           python-%{pypi_name}
Version:        16.8
Release:        6
Summary:        Core utilities for Python packages

License:        BSD or ASL 2.0
URL:            https://github.com/pypa/packaging
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-setuptools
BuildRequires:  python2-devel
BuildRequires:  python2-six

BuildRequires:  python-setuptools
BuildRequires:  python3-devel

%description
python-packaging provides core utilities for Python
packages like utilities for dealing with versions,
specifiers, markers etc.

%package -n python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-six
%description -n python2-%{pypi_name}
python2-packaging provides core utilities for Python
packages like utilities for dealing with versions,
specifiers, markers etc.


%package -n python-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python-six

%description -n python-%{pypi_name}
python3-packaging provides core utilities for Python
packages like utilities for dealing with versions,
specifiers, markers etc.

%package -n python-%{pypi_name}-doc
Summary:        python-packaging documentation
Suggests:       python-%{pypi_name} = %{version}-%{release}

%description -n python-%{pypi_name}-doc
Documentation for python-packaging

%prep
%setup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
cp -a . %{py3dir}

%build
%{__python2} setup.py build
pushd %{py3dir}
%{__python3} setup.py build
popd

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# Do not bundle fonts
rm -rf html/_static/fonts/

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd

%files -n python2-%{pypi_name}
%{python2_sitelib}/%{pypi_name}/
%{python2_sitelib}/%{pypi_name}-*.egg-info/

%files -n python-%{pypi_name}
%{py3_puresitedir}/%{pypi_name}/
%{py3_puresitedir}/%{pypi_name}-*.egg-info/

%files -n python-%{pypi_name}-doc
%doc LICENSE LICENSE.APACHE LICENSE.BSD
