%define ff_epoch 0
%define ff_ver 3.0.10
%define realname downthemall

%define _mozillapath %{_libdir}/firefox-%{ff_ver}
%define _mozillaextpath %{_mozillapath}/extensions

%define rel 1

Summary: DownThemAll! extension for firefox
Name: firefox-ext-%{realname}
Version: 1.1.2
Release: %mkrel %rel
License: MPL1.1 or GPLv2+ or LGPLv2+
Group: Networking/WWW
URL: http://www.downthemall.net
Source: http://code.downthemall.net/releases/%{realname}-%{version}.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: mozilla-firefox = %{ff_epoch}:%{ff_ver}
Obsoletes: mozilla-firefox-ext-%{realname} < %{version}-%{release}
Provides: mozilla-firefox-ext-%{realname} = %{version}-%{release}

%description
DownThemAll (or just dTa) is a powerful yet easy-to-use Mozilla Firefox
extension that adds new advanced download capabilities to your browser.

DownThemAll lets you download all the links or images contained in a
webpage and much more: you can refine your downloads by fully
customizable criteria to get only what you really want.

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %_mozillapath
%{_mozillaextpath}
