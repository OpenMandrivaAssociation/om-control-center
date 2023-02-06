Name:		om-control-center
Version:	0.2.15
Release:	2
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
%autopatch -p1

%build
# Nothing to do here...

%install
%make_install

%find_lang om-control-center

mkdir -p %{buildroot}%{_datadir}/icons/
cp om-cc.svg %{buildroot}%{_datadir}/icons/

# Adding update script
install -d %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/om-update.desktop
[Desktop Entry]
Name=System Update
GenericName=System Update
Comment=Check for available system update and then install them
Exec=/usr/share/om-control-center/apps/updatesys.run
Icon=/usr/share/om-control-center/images/system-update.svg
Terminal=false
Type=Application
Categories=System
EOF

%files -f om-control-center.lang
%{_bindir}/om-control-center
%{_datadir}/%{name}/*
%{_datadir}/applications/om-control-center.desktop
%{_datadir}/applications/om-update.desktop
%{_datadir}/icons/om-cc.svg
