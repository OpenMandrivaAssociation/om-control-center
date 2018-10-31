Name:		om-control-center
Version:	0.0.3
Release:	2
Summary:	OpenMandriva Lx Control Center
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/OpenMandrivaAssociation/om-control-center
Source0:	https://github.com/OpenMandrivaSoftware/om-control-center/archive/%{name}-%{version}.tar.gz
Requires:	kdialog
Requires:	htmlscript
BuildRequires:	make
BuildArch:	noarch

%description
OpenMandriva Lx Control Center.

%prep
%setup -q
%apply_patches

%build
# Nothing to do here...

%install
%makeinstall_std

%find_lang om-control-center

%files -f om-control-center.lang
%{_bindir}/om-cc-launcher
%{_bindir}/om-control-center
%{_datadir}/%{name}/*
%{_datadir}/applications/om-control-center.desktop
