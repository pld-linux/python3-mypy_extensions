#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Experimental type system extensions for programs checked with the mypy typechecker
Summary(pl.UTF-8):	Eksperymentalne rozszerzenia systemu typowania dla programów sprawdzanych narzędziem mypy
Name:		python-mypy_extensions
Version:	0.4.3
Release:	5
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mypy-extensions/
Source0:	https://files.pythonhosted.org/packages/source/m/mypy-extensions/mypy_extensions-%{version}.tar.gz
# Source0-md5:	4163ff73d0db8631c0a78bb55b551c84
URL:		https://pypi.org/project/mypy-extensions/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "mypy_extensions" module defines experimental extensions to the
standard "typing" module that are supported by the mypy typechecker.

%description -l pl.UTF-8
Moduł "mypy_extensions" definiuje eksperymentalne rozszerzenia
standardowego modułu "typing", obsługiwane przez narzędzie do
kontroli typów mypy.

%package -n python3-mypy_extensions
Summary:	Experimental type system extensions for programs checked with the mypy typechecker
Summary(pl.UTF-8):	Eksperymentalne rozszerzenia systemu typowania dla programów sprawdzanych narzędziem mypy
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-mypy_extensions
The "mypy_extensions" module defines experimental extensions to the
standard "typing" module that are supported by the mypy typechecker.

%description -n python3-mypy_extensions -l pl.UTF-8
Moduł "mypy_extensions" definiuje eksperymentalne rozszerzenia
standardowego modułu "typing", obsługiwane przez narzędzie do
kontroli typów mypy.

%prep
%setup -q -n mypy_extensions-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/mypy_extensions.py[co]
%{py_sitescriptdir}/mypy_extensions-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-mypy_extensions
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/mypy_extensions.py
%{py3_sitescriptdir}/__pycache__/mypy_extensions.cpython-*.py[co]
%{py3_sitescriptdir}/mypy_extensions-%{version}-py*.egg-info
%endif
