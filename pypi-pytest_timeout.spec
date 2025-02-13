#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v4
# autospec commit: 1ab68ca
#
Name     : pypi-pytest_timeout
Version  : 2.3.1
Release  : 82
URL      : https://files.pythonhosted.org/packages/93/0d/04719abc7a4bdb3a7a1f968f24b0f5253d698c9cc94975330e9d3145befb/pytest-timeout-2.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/93/0d/04719abc7a4bdb3a7a1f968f24b0f5253d698c9cc94975330e9d3145befb/pytest-timeout-2.3.1.tar.gz
Summary  : pytest plugin to abort hanging tests
Group    : Development/Tools
License  : MIT
Requires: pypi-pytest_timeout-license = %{version}-%{release}
Requires: pypi-pytest_timeout-python = %{version}-%{release}
Requires: pypi-pytest_timeout-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pexpect
BuildRequires : pypi-pytest
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
==============
pytest-timeout
==============
|python| |version| |anaconda| |ci| |pre-commit|

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
%setup -q -n pytest-timeout-2.3.1
cd %{_builddir}/pytest-timeout-2.3.1
pushd ..
cp -a pytest-timeout-2.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709914164
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytest_timeout
cp %{_builddir}/pytest-timeout-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytest_timeout/8216f3d66db8d3c8edf0e6c29f7db60c021f3490 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
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
