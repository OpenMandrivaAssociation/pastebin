%define name pastebin
%define version 1.0
%define release 8

Summary:	A tool to send data to pastebin 
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}
License:	GPLv2+
Group:		Text tools
Url:		https://raphael.slinckx.net/files/%{name}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python

%description
A simple tool to send data to pastebin.
Usage could be "echo toto | pastebin"

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 %SOURCE0 %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%name



%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 1.0-7mdv2011.0
+ Revision: 664797
- rebuild old package

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

  + Sandro Cazzaniga <kharec@mandriva.org>
    - Just fix mix of space and tabs in spec, not bump release.
    - fix licence

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2010.0
+ Revision: 430241
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 255045
- rebuild

* Tue Mar 11 2008 Erwan Velu <erwan@mandriva.org> 1.0-1mdv2008.1
+ Revision: 186977
- import pastebin


