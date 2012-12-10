%define realname downthemall

%define rel 2

Summary: DownThemAll! extension for firefox
Name: firefox-ext-%{realname}
Version: 2.0.3
Release: %rel
License: MPL1.1 or GPLv2+ or LGPLv2+
Group: Networking/WWW
URL: http://www.downthemall.net
Source: http://code.downthemall.net/releases/%{realname}-%{version}.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Buildarch: noarch
Requires: firefox >= %{firefox_version}
Obsoletes: mozilla-firefox-ext-%{realname} < %{version}-%{release}
Provides: mozilla-firefox-ext-%{realname} = %{version}-%{release}
BuildRequires: firefox-devel
Obsoletes: %{name} < %{version}-%{release}

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
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}


%changelog
* Wed May 11 2011 Funda Wang <fwang@mandriva.org> 2.0.3-1mdv2011.0
+ Revision: 673415
- update to new version 2.0.3

* Sat Mar 19 2011 Funda Wang <fwang@mandriva.org> 2.0.2-1
+ Revision: 646531
- update to new version 2.0.2

* Tue Jan 18 2011 Funda Wang <fwang@mandriva.org> 2.0-1
+ Revision: 631462
- New version 2.0

* Wed Jan 05 2011 Thierry Vignaud <tv@mandriva.org> 2.0-0.b5.3mdv2011.0
+ Revision: 628871
- rebuild for new firefox

* Sun Nov 14 2010 Thierry Vignaud <tv@mandriva.org> 2.0-0.b5.2mdv2011.0
+ Revision: 597399
- rebuild for new firefox

* Fri Nov 12 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 2.0-0.b5.1mdv2011.0
+ Revision: 596987
- new beta

* Sun Nov 07 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 2.0-0.b4.1mdv2011.0
+ Revision: 594456
- update to 2.0b4 for firefox4 support

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - rebuild for firefox-3.6.8

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 1.1.10-3mdv2011.0
+ Revision: 561154
- rebuild for ff 3.6.8

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 1.1.10-2mdv2010.1
+ Revision: 549363
- rebuild with FF 3.6.6

  + Funda Wang <fwang@mandriva.org>
    - New version 1.1.10

* Sun Apr 04 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.1.9-2mdv2010.1
+ Revision: 531266
- Rebuild

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 1.1.9-1mdv2010.1
+ Revision: 531237
- update to new version 1.1.9

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 1.1.8-3mdv2010.1
+ Revision: 531091
- rebuild

* Wed Mar 24 2010 Funda Wang <fwang@mandriva.org> 1.1.8-2mdv2010.1
+ Revision: 527007
- rebuild

* Fri Jan 22 2010 Funda Wang <fwang@mandriva.org> 1.1.8-1mdv2010.1
+ Revision: 494854
- update to new version 1.1.8

* Fri Jan 22 2010 Funda Wang <fwang@mandriva.org> 1.1.7-3mdv2010.1
+ Revision: 494797
- rebuild

* Sun Dec 20 2009 Funda Wang <fwang@mandriva.org> 1.1.7-2mdv2010.1
+ Revision: 480366
- rebuild for ff 3.6b5

* Tue Nov 10 2009 Funda Wang <fwang@mandriva.org> 1.1.7-1mdv2010.1
+ Revision: 463977
- new version 1.1.7

* Wed Sep 16 2009 Funda Wang <fwang@mandriva.org> 1.1.4-3mdv2010.0
+ Revision: 443381
- rebuild for new ff

* Tue Aug 18 2009 Gustavo De Nardin <gustavodn@mandriva.com> 1.1.4-2mdv2010.0
+ Revision: 417669
- buildrequire firefox-devel, which provides the new macros for building extensions
- make use of the firefox package macros
- rebuild for firefox 3.5.2

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 1.1.4-1mdv2010.0
+ Revision: 410559
- new version 1.1.4

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 1.1.3-4mdv2010.0
+ Revision: 410505
- rebuild for new ff

* Fri Jul 31 2009 Funda Wang <fwang@mandriva.org> 1.1.3-3mdv2010.0
+ Revision: 405029
- rebuild for new ff

* Sun Jun 14 2009 Funda Wang <fwang@mandriva.org> 1.1.3-2mdv2010.0
+ Revision: 385773
- rebuild for new ff

* Sat May 30 2009 Funda Wang <fwang@mandriva.org> 1.1.3-1mdv2010.0
+ Revision: 381245
- New version 1.1.3

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 1.1.2-1mdv2010.0
+ Revision: 369813
- New version 1.1.2

* Sat Mar 28 2009 Gustavo De Nardin <gustavodn@mandriva.com> 1.1.0-3mdv2009.1
+ Revision: 361849
- rebuild for firefox 3.0.8

* Thu Mar 12 2009 Funda Wang <fwang@mandriva.org> 1.1.0-2mdv2009.1
+ Revision: 354097
- rebuild for new ff

* Wed Feb 04 2009 Funda Wang <fwang@mandriva.org> 1.1.0-1mdv2009.1
+ Revision: 337312
- rename to firefox
- New version 1.1.0
- New version 1.0.4
- rename to firefox

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 1.0.3-7mdv2009.1
+ Revision: 318919
- rebuild for new ff

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 1.0.3-6mdv2009.1
+ Revision: 303694
- rebuild for new FF

* Mon Sep 29 2008 Funda Wang <fwang@mandriva.org> 1.0.3-5mdv2009.0
+ Revision: 289174
- rebuild for new FF

* Wed Jul 30 2008 Tiago Salem <salem@mandriva.com.br> 1.0.3-4mdv2009.0
+ Revision: 256465
- add conditional to ff3

* Wed Jul 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-3mdv2009.0
+ Revision: 236361
- rebuilt for mozilla-firefox-2.0.0.16

* Thu Jul 03 2008 Tiago Salem <salem@mandriva.com.br> 1.0.3-2mdv2009.0
+ Revision: 231257
- Rebuild for firefox 2.0.0.15

* Sat Jun 07 2008 Funda Wang <fwang@mandriva.org> 1.0.3-1mdv2009.0
+ Revision: 216650
- New version 1.0.3

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 1.0.1-1mdv2009.0
+ Revision: 201020
- New version 1.0.1

* Sat Apr 19 2008 Funda Wang <fwang@mandriva.org> 1.0-3mdv2009.0
+ Revision: 195740
- rebuild with FF 2.0.0.14

* Wed Mar 26 2008 Tiago Salem <salem@mandriva.com.br> 1.0-2mdv2008.1
+ Revision: 190328
- bump ff_ver and release

* Sat Mar 01 2008 Funda Wang <fwang@mandriva.org> 1.0-1mdv2008.1
+ Revision: 177075
- New version 1.0

* Sat Feb 09 2008 Funda Wang <fwang@mandriva.org> 1.0-0.b2.4mdv2008.1
+ Revision: 164603
- Clearify the license
- rebuild for new FF

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Thierry Vignaud <tv@mandriva.org> 1.0-0.b2.3mdv2008.1
+ Revision: 117791
- own firefox directories so that they're not left behind on uninstall

* Wed Dec 12 2007 Funda Wang <fwang@mandriva.org> 1.0-0.b2.2mdv2008.1
+ Revision: 117621
- Rebuild for new ff

* Sun Nov 18 2007 Funda Wang <fwang@mandriva.org> 1.0-0.b2.1mdv2008.1
+ Revision: 109789
- import SOURCE and SPEC
- Created package structure for mozilla-firefox-ext-downloadthemall.

