# Created by pyp2rpm-3.3.3
%global pypi_name lz4

%bcond_without docs
%bcond_with tests

Name:           python-%{pypi_name}
Version:        3.0.2
Release:        1
Summary:        LZ4 Bindings for Python
Group:          Development/Python
License:        None
URL:            https://github.com/python-lz4/python-lz4
Source0:        https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python-devel
#BuildRequires:  python3dist(flake8)
BuildRequires:  python-pkgconfig
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
# for docs
%if %{with docs}
BuildRequires:  python3dist(sphinx) >= 1.6.0
#BuildRequires:  python3dist(sphinx-bootstrap-theme)
BuildRequires:  python3dist(sphinx)
%endif
# for tests
%if %{with tests}
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pytest)
#BuildRequires:  python3dist(pytest-cov)
#BuildRequires:  python3dist(pytest-runner)
%endif

%description
This package provides python bindings for the LZ4 compression library.

The bindings provided in this package cover the frame format, the block format, and the
streaming format specifications. The frame format bindings are the recommended ones to use,
as this guarantees interoperability with other implementations and language bindings.

The API provided by the frame format bindings follows that of the LZMA, zlib, gzip and bzip2
compression libraries which are provided with the Python standard library. As such, these
LZ4 bindings should provide a drop-in alternative to the compression libraries shipped with
Python. The package provides context managers and file handler support.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%if %{with docs}
# build egg-info
%py_build_egg
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py_install

%if %{with tests}
%check
%{__python} setup.py test
%endif

%files 
%license docs/license.rst LICENSE
%doc README.rst
%if %{with docs}
%doc html
%endif
%{python_sitearch}/%{pypi_name}
%{python_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
