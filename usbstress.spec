%define name    usbstress
%define version 0.3
%define release %mkrel 7

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:	USB test Load
URL:		http://www.lrr.in.tum.de/Par/arch/usb/download/usbstress/
License:	GPL
Group:		System/Kernel and hardware
Source0:	%{name}-%{version}.tar.bz2
Patch0:		uhcidump.c.patch.bz2
Patch1:		ihex2hdr.c.patch.bz2
Buildroot:	 %{_tmppath}/%{name}-%{version}-root

%description
This is a USB stress test suite.  It requires an AnchorChips AN2131
based device, which is loaded with a special test firmware.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0
sed -i s/-march=i686// Makefile.*

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%files
%attr(755,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%_bindir/usbstress
%_sbindir/uhcidump

%clean
rm -rf $RPM_BUILD_ROOT
