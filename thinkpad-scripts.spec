# Copyright © 2015 Martin Ueding <dev@martin-ueding.de>

# spec file for package thinkpad-scripts
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
Version:        4.7.1
Release:        1
License:        GPL-2.0+
Summary:        Rotate scripts for Lenovo ThinkPad
Url:            http://martin-ueding.de/en/projects/%{name}
Source0:        http://bulk.martin-ueding.de/source/%{name}/%{name}_%{version}.tar.gz
#Group:
#Patch:
BuildRequires:  gettext python3-setuptools python3-devel

%if 0%{?suse_version}
BuildRequires:  oxygen-icon-theme
BuildRequires:  python3-Sphinx
BuildRequires:  systemd
BuildRequires:  udev
BuildRequires:  update-desktop-files
%else
BuildRequires:  python3-sphinx
%endif

BuildArch:      noarch
Requires:       acpid alsa-utils python3-setuptools udev xinput 

%if 0%{?suse_version}
Requires:       systemd
Requires:       xrandr
%else
Requires:       xorg-x11-server-utils
%endif

#PreReq:
#Provides:       think-rotate think-dock
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

This collection of scripts is intended for the Lenovo ThinkPad X220 Tablet. You
can still use them with the regular X220 machine, but only ``thinkpad-rotate``
will probably be useless for you then. I think that most scripts will also be
handy for other ThinkPad models, I have not tested them though.

In short, this script fixes or improves the following:

1. Rotation of the internal screen and any Wacom touch and pen input devices
   using the bezel buttons or physical screen rotation

2. Get the microphone mute button to work.

3. Automatically use any external monitor, speakers and LAN connection when
   docking onto an UltraBase or similar.

4. Ability to disable touch pad or touch screen

%prep
%setup -q

%if 0%{?suse_version}
%define sphinx_build sphinx-build
%else
%define sphinx_build sphinx-build-3
%endif

%build
make %{?_smp_mflags} SPHINXBUILD=%{sphinx_build}

%install
%make_install
/usr/bin/python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
#%py3_install

%if 0%{?suse_version}
%suse_update_desktop_file -r thinkpad-dock-off System HardwareSettings
%suse_update_desktop_file -r thinkpad-dock-on System HardwareSettings
%suse_update_desktop_file -r thinkpad-rotate System Monitor
%suse_update_desktop_file -r thinkpad-rotate-flip System Monitor
%suse_update_desktop_file -r thinkpad-rotate-left System Monitor
%suse_update_desktop_file -r thinkpad-touch System HardwareSettings
%suse_update_desktop_file -r thinkpad-touchpad System HardwareSettings
%suse_update_desktop_file -r thinkpad-touchpad System HardwareSettings
%endif

%post
systemctl restart acpid.service || true
udevadm hwdb --update

%postun
systemctl restart acpid.service || true
udevadm hwdb --update

%files
%defattr(-,root,root)

%doc CHANGELOG.rst README.rst COPYING.rst
%{python3_sitelib}/*
/etc/acpi
/etc/acpi/events
/etc/acpi/events/*
/lib/udev/hwdb.d/*
/lib/udev/rules.d/*
/usr/bin/*
/usr/share/applications/*
/usr/share/man/man1/*

%changelog
* Sat Jan 24 2015 Martin Ueding <dev@martin-ueding.de> 4.2.2-1
- New upstream version that does not depend on termcolor any more.

* Sat Jan 24 2015 Martin Ueding <dev@martin-ueding.de> 4.2.1-2
- Fix %%files section where I previously attemted to own `/`.

* Sat Jan 24 2015 Martin Ueding <dev@martin-ueding.de> 4.2.1-1
- Initial packaging
