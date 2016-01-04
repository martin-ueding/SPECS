# Copyright © 2015 Martin Ueding <dev@martin-ueding.de>

# spec file for package backup-scripts
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           backup-scripts
Version:        3.1.0
Release:        1
License:        GPL-2.0+
Summary:        My personal backup scripts
Url:            http://martin-ueding.de/en/projects/%{name}
Source0:        http://bulk.martin-ueding.de/source/%{name}/%{name}_%{version}.tar.gz
BuildRequires:  python3-setuptools
Requires:       python3-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description

Backup home folder, webservers and Android devices

%prep
%setup -q

%build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root)
%{python3_sitelib}/*
/usr/bin/*
