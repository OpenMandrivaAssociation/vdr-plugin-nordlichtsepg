%define plugin	nordlichtsepg

Summary:	VDR plugin: Extended EPG
Name:		vdr-plugin-%plugin
Version:	0.8a
Release:	20
Group:		Video
License:	GPL
URL:		https://martins-kabuff.de/nordlichtsepg.html
Source:		http://martins-kabuff.de/download/vdr-%plugin-%{version}.tar.bz2
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
%setup -q -n %plugin-%{version}
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README* HISTORY




