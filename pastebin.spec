%define name pastebin
%define version 1.0
%define release %mkrel 4

Summary: A tool to send data to pastebin 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}
License: GPL
Group: Text tools
Url: http://raphael.slinckx.net/files/%{name}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: python

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

