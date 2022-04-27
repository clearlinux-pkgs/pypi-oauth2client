#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-oauth2client
Version  : 4.1.3
Release  : 60
URL      : https://files.pythonhosted.org/packages/a6/7b/17244b1083e8e604bf154cf9b716aecd6388acd656dd01893d0d244c94d9/oauth2client-4.1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/a6/7b/17244b1083e8e604bf154cf9b716aecd6388acd656dd01893d0d244c94d9/oauth2client-4.1.3.tar.gz
Summary  : OAuth 2.0 client library
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-oauth2client-license = %{version}-%{release}
Requires: pypi-oauth2client-python = %{version}-%{release}
Requires: pypi-oauth2client-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(httplib2)
BuildRequires : pypi(pyasn1)
BuildRequires : pypi(pyasn1_modules)
BuildRequires : pypi(rsa)
BuildRequires : pypi(six)

%description
oauth2client is a client library for OAuth 2.0.

%package license
Summary: license components for the pypi-oauth2client package.
Group: Default

%description license
license components for the pypi-oauth2client package.


%package python
Summary: python components for the pypi-oauth2client package.
Group: Default
Requires: pypi-oauth2client-python3 = %{version}-%{release}

%description python
python components for the pypi-oauth2client package.


%package python3
Summary: python3 components for the pypi-oauth2client package.
Group: Default
Requires: python3-core
Provides: pypi(oauth2client)
Requires: pypi(httplib2)
Requires: pypi(pyasn1)
Requires: pypi(pyasn1_modules)
Requires: pypi(rsa)
Requires: pypi(six)

%description python3
python3 components for the pypi-oauth2client package.


%prep
%setup -q -n oauth2client-4.1.3
cd %{_builddir}/oauth2client-4.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651102850
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-oauth2client
cp %{_builddir}/oauth2client-4.1.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-oauth2client/a7b6feb97b476557d3d699fa1f20090fb956d662
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-oauth2client/a7b6feb97b476557d3d699fa1f20090fb956d662

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*