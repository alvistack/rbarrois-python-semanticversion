%global debug_package %{nil}

Name: python-semantic-version
Epoch: 100
Version: 2.8.5
Release: 1%{?dist}
BuildArch: noarch
Summary: Library implementing the 'SemVer' scheme
License: BSD-2-Clause
URL: https://github.com/rbarrois/python-semanticversion/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This small python library provides a few tools to handle semantic
versioning in Python.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-semantic_version
Summary: Library implementing the 'SemVer' scheme
Requires: python3
Requires: python3-setuptools >= 0.8
Provides: python3-semantic_version = %{epoch}:%{version}-%{release}
Provides: python3dist(semantic-version) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-semantic_version = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(semantic-version) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-semantic_version = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(semantic-version) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-semantic_version
This small python library provides a few tools to handle semantic
versioning in Python.

%files -n python%{python3_version_nodots}-semantic_version
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-semantic_version
Summary: Library implementing the 'SemVer' scheme
Requires: python3
Requires: python3-setuptools >= 0.8
Provides: python3-semantic_version = %{epoch}:%{version}-%{release}
Provides: python3dist(semantic-version) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-semantic_version = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(semantic-version) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-semantic_version = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(semantic-version) = %{epoch}:%{version}-%{release}

%description -n python3-semantic_version
This small python library provides a few tools to handle semantic
versioning in Python.

%files -n python3-semantic_version
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
