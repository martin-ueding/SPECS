Name:		backup-scripts
Version:	3.1.0
Release:	1%{?dist}
Summary:	Backup scripts

License:	GPL
Url:            http://martin-ueding.de/en/projects/%{name}
Source0:        http://bulk.martin-ueding.de/source/%{name}/%{name}_%{version}.tar.gz

BuildRequires:	python3-setuptools python3-devel
Requires:	python3-setuptools
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description


%prep
%setup -q


%build


%install
python3 setup.py install --skip-build --root $RPM_BUILD_ROOT


%files
%doc CHANGELOG.rst
%{python3_sitelib}/*

%changelog

