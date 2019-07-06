Name:		om-control-center
Version:	0.1.16
Release:	1
Summary:	OpenMandriva Lx Control Center
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/OpenMandrivaAssociation/om-control-center
Source0:	https://github.com/OpenMandrivaSoftware/om-control-center/archive/%{version}/%{name}-%{version}.tar.gz
Requires:	kdialog
Requires:	dnf-plugins-core
Requires:	htmlscript >= 1.0.1
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
%make_install

%find_lang om-control-center

mkdir -p %{buildroot}%{_datadir}/icons/
cp om-cc.svg %{buildroot}%{_datadir}/icons/

%files -f om-control-center.lang
%{_bindir}/om-control-center
%{_datadir}/%{name}/*
%{_datadir}/applications/om-control-center.desktop
%{_datadir}/icons/om-cc.svg
