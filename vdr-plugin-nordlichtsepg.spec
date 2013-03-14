
%define plugin	nordlichtsepg
%define name	vdr-plugin-%plugin
%define version	0.8a
%define rel	18

Summary:	VDR plugin: Extended EPG
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://martins-kabuff.de/nordlichtsepg.html
Source:		http://martins-kabuff.de/download/vdr-%plugin-%version.tar.bz2
Patch0:		91_nordlichtsepg-0.8a_vdr153.dpatch
Patch1:		nordlichtsepg-0.8a-i18n-1.6.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin provides an EPG (Electronic Program Guide) similar to VDR's
"What's on now?"-menu. Unlike this it also shows channels without epg-infos.
You can browse the epg with an adjustable step width. It is also possible to
set a time at the setup which you can jump to by keypress, with the keys 1-7
you can jumpo 1-7 days forward. You can enter a time to jump to instantly.
A bargraph at the "What's on now?"-view shows the progress of the running
program. Timers are marked with a clock-icon, recording timers with a
'REC'-icon. It is possible, also for channels without epg-infos, to set and
delete timers.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.8a-17mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.8a-16mdv2009.1
+ Revision: 359343
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.8a-15mdv2009.0
+ Revision: 197955
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.8a-14mdv2009.0
+ Revision: 197697
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of VDR 1.5.3 (P0 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.8a-13mdv2008.1
+ Revision: 145154
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.8a-12mdv2008.1
+ Revision: 103173
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.8a-11mdv2008.0
+ Revision: 50023
- rebuild for new vdr

* Fri Jun 22 2007 Anssi Hannula <anssi@mandriva.org> 0.8a-10mdv2008.0
+ Revision: 42638
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.8a-8mdv2008.0
+ Revision: 22761
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.8a-7mdv2007.0
+ Revision: 90948
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.8a-6mdv2007.1
+ Revision: 74061
- rebuild for new vdr
- Import vdr-plugin-nordlichtsepg

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.8a-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.8a-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.8a-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.8a-2mdv2007.0
- rebuild for new vdr

* Sun Jul 16 2006 Anssi Hannula <anssi@mandriva.org> 0.8a-1mdv2007.0
- initial Mandriva release

