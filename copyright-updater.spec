Name:		copyright-updater
Version:	1.2.2
Release:	1%{?dist}
Summary:	Updates copyright messages in text files

License:	GPL
Url:            http://martin-ueding.de/en/projects/%{name}
Source0:        http://bulk.martin-ueding.de/source/%{name}/%{name}_%{version}.tar.gz

BuildArch:      noarch
BuildRequires:	python-devel
Requires:	python

%description


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} setupoptions="--root %{buildroot}"


%files
%doc
%{python2_sitelib}/*
/usr/bin/*
/usr/share/vim/vimfiles/plugin/*


%changelog

