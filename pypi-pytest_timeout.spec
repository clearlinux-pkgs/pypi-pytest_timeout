#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pytest_timeout
Version  : 2.1.0
Release  : 75
URL      : https://files.pythonhosted.org/packages/ef/30/37abbd50f86cb802cbcea50d68688438de1a7446d73c8ed8d048173b4b13/pytest-timeout-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ef/30/37abbd50f86cb802cbcea50d68688438de1a7446d73c8ed8d048173b4b13/pytest-timeout-2.1.0.tar.gz
Summary  : pytest plugin to abort hanging tests
Group    : Development/Tools
License  : MIT
Requires: pypi-pytest_timeout-license = %{version}-%{release}
Requires: pypi-pytest_timeout-python = %{version}-%{release}
Requires: pypi-pytest_timeout-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pytest)
BuildRequires : pypi-pexpect
BuildRequires : pypi-pytest

%description
pytest-timeout
        ==============
        
        |python| |version| |anaconda| |ci|

%package license
Summary: license components for the pypi-pytest_timeout package.
Group: Default

%description license
license components for the pypi-pytest_timeout package.


%package python
Summary: python components for the pypi-pytest_timeout package.
Group: Default
Requires: pypi-pytest_timeout-python3 = %{version}-%{release}

%description python
python components for the pypi-pytest_timeout package.


%package python3
Summary: python3 components for the pypi-pytest_timeout package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_timeout)
Requires: pypi(pytest)

%description python3
python3 components for the pypi-pytest_timeout package.


%prep
%setup -q -n pytest-timeout-2.1.0
cd %{_builddir}/pytest-timeout-2.1.0
pushd ..
cp -a pytest-timeout-2.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656401415
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytest_timeout
cp %{_builddir}/pytest-timeout-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytest_timeout/8216f3d66db8d3c8edf0e6c29f7db60c021f3490
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pytest_timeout/8216f3d66db8d3c8edf0e6c29f7db60c021f3490

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
