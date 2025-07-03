#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Experimental type system extensions for programs checked with the mypy typechecker
Summary(pl.UTF-8):	Eksperymentalne rozszerzenia systemu typowania dla programów sprawdzanych narzędziem mypy
Name:		python3-mypy_extensions
Version:	1.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mypy-extensions/
Source0:	https://files.pythonhosted.org/packages/source/m/mypy-extensions/mypy_extensions-%{version}.tar.gz
# Source0-md5:	f59bfd7f9dca73f36c8feed12f9e8eba
URL:		https://pypi.org/project/mypy-extensions/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.11
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "mypy_extensions" module defines experimental extensions to the
standard "typing" module that are supported by the mypy typechecker.

%description -l pl.UTF-8
Moduł "mypy_extensions" definiuje eksperymentalne rozszerzenia
standardowego modułu "typing", obsługiwane przez narzędzie do
kontroli typów mypy.

%prep
%setup -q -n mypy_extensions-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m unittest discover tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/mypy_extensions.py
%{py3_sitescriptdir}/__pycache__/mypy_extensions.cpython-*.py[co]
%{py3_sitescriptdir}/mypy_extensions-%{version}.dist-info
