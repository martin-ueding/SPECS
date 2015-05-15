Name:		legacy-file-formats
Version:	1.6.9
Release:	1%{?dist}
Summary:	Exports files

License:	GPL
Url:            http://martin-ueding.de/en/projects/%{name}
Source0:        http://bulk.martin-ueding.de/source/%{name}/%{name}_%{version}.tar.gz

BuildArch:      noarch
BuildRequires:	python-docutils java-1.8.0-openjdk-devel python-setuptools
Requires:	java-1.8.0-openjdk python python-prettytable xorg-x11-server-Xvfb python-setuptools

%description


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} SETUPOPTIONS="--prefix=%{_prefix} --root=%{buildroot}"


%files
%doc CHANGELOG.rst
%{python_sitelib}/*
/etc/legacy
/usr/bin/*
/usr/share/legacy
/usr/share/man/man1/*


%changelog

