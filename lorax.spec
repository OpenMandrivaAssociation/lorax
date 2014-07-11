%define debug_package %{nil}

Summary:	Tool for creating the anaconda install images
Name:		lorax
Version:	18.12
Release:	14
Group:		System/Base
License:	GPLv2+
Url:		http://git.fedorahosted.org/git/?p=lorax.git
Source0:	https://fedorahosted.org/releases/l/o/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
Requires:	cdrkit-genisoimage
Requires:	cpio
Requires:	device-mapper
Requires:	dosfstools
Requires:	e2fsprogs
Requires:	findutils
Requires:	gawk
Requires:	GConf2
Requires:	gzip
Requires:	isomd5sum
Requires:	python-selinux
Requires:	module-init-tools
Requires:	parted
Requires:	python-mako
Requires:	squashfs-tools >= 4.2
Requires:	util-linux
Requires:	xz
Requires:	pykickstart
%ifarch %{ix86} x86_64
Requires:	syslinux >= 4.02-5
%endif
Suggests:	yum

%description
Lorax is a tool for creating the anaconda install images.

It also includes livemedia-creator which is used to create bootable livemedia,
including live isos and disk images. It can use libvirtd for the install, or
Anaconda's image install feature.

%prep
%setup -q

%build

%install
%makeinstall_std

%files
%doc COPYING AUTHORS README.livemedia-creator
%{python_sitelib}/pylorax
%{python_sitelib}/*.egg-info
%{_sbindir}/lorax
%{_sbindir}/mkefiboot
%{_sbindir}/livemedia-creator
%dir %{_sysconfdir}/lorax
%config(noreplace) %{_sysconfdir}/lorax/lorax.conf
%dir %{_datadir}/lorax
%{_datadir}/lorax/*

