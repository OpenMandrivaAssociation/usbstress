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


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.3-7mdv2010.0
+ Revision: 434589
- rebuild
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-5mdv2009.0
+ Revision: 255261
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.3-3mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Anne Nicolas <anne.nicolas@mandriva.com> 0.3-3mdv2008.0
+ Revision: 63536
- rebuild for 2008.0
- Import usbstress



* Fri May 26 2006 Pascal Terjan <pterjan@mandriva.org> 0.3-2mdv2007.0
- fix build for non i686
- mkrel
- use standard way for installing doc
- tell in the description that it won't work for me

* Tue May 9 2006 Anne Nicolas <anne.nicolas@mandriva.com> 0.3-1mdk
- initial release
