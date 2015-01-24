#
# spec file for package 
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           thinkpad-scripts
Version:        4.2.1
Release:        1
License:        GPL
Summary:        Rotate scripts for Lenovo ThinkPad
Url:            http://martin-ueding.de/en/projects/%{name}
Source0:        http://bulk.martin-ueding.de/source/%{name}/%{name}_%{version}.tar.gz
#Group:
#Source:         %{name}_%{version}.tar.gz
#Patch:
BuildRequires:  gettext python3-setuptools python3-sphinx python-termcolor
BuildArch:      noarch
#PreReq:
#Provides:       think-rotate think-dock
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
%setup -q

%build
make %{?_smp_mflags} SPHINXBUILD=sphinx-build-3

%install
%make_install

%post

%postun

%files
%defattr(-,root,root)
/
%doc CHANGELOG.rst README.rst COPYING.rst

%changelog

