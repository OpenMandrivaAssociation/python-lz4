# Created by pyp2rpm-3.3.3
%global pypi_name lz4

Name:           python-%{pypi_name}
Version:        4.4.5
Release:        1
Summary:        LZ4 Bindings for Python
Group:          Development/Python
License:        None
URL:            https://github.com/python-lz4/python-lz4
Source0:        https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python-devel
#BuildRequires:  python3dist(flake8)
#BuildRequires:  python-pkgconfig
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(setuptools-scm)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(pkgconfig)
BuildRequires:  python%{pyver}dist(future)


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

%install
%py_install

%files 
%license docs/license.rst LICENSE
%doc README.rst

%{python_sitearch}/%{pypi_name}
%{python_sitearch}/%{pypi_name}-%{version}-py%{python_version}.egg-info
