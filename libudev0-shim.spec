Name     : libudev0-shim
Version  : 1
Release  : 6
URL      : https://github.com/archlinux/libudev0-shim/archive/v1.tar.gz
Source0  : https://github.com/archlinux/libudev0-shim/archive/v1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : systemd-dev32
BuildRequires : systemd-lib32
BuildRequires : systemd-dev

Requires: libudev0-shim-lib
Patch1: build.patch

%description
No detailed description available

%package lib
Summary: lib components for the libudev0-shim package.
Group: Libraries

%description lib
lib components for the libudev0-shim package.


%package lib32
Summary: lib32 components for the libudev0-shim package.
Group: Default

%description lib32
lib32 components for the libudev0-shim package.


%prep
%setup -q -n libudev0-shim-1
%patch1 -p1

%build
export LANG=C
unset LD_AS_NEEDED
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libudev.so.0.0.9999

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libudev.so.0.0.9999
