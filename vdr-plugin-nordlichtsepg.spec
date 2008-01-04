
%define plugin	nordlichtsepg
%define name	vdr-plugin-%plugin
%define version	0.8a
%define rel	13

Summary:	VDR plugin: Extended EPG
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://martins-kabuff.de/nordlichtsepg.html
Source:		http://martins-kabuff.de/download/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
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

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY


