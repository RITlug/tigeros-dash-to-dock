Name:           tigeros-dash-to-dock
Version:        1
Release:        1%{?dist}
Summary:        dash-to-dock tweaks for TigerOS

License:        GPLv3+
URL:            https://github.com/RITlug/tigeros-dash-to-dock
Source0:        https://builder.ritlug.com/packages/x86_64/%{name}-%{version}-%{release}.tar.gz

BuildArch:      noarch
Requires:       gnome-shell-extension-dash-to-dock
Requires:       glib2
Requires:       dconf

%description
This package tweaks the default installation
settings given from gnome-shell-extensions-dash-to-dock.

%prep
%setup -q

%install
%{__mkdir_p} %{buildroot}%{_datadir}/share/glib-2.0/schemas
install -p -m 644 %{buildroot}%{_datadir}/glib-2.0/schemas/10_tigeros.dash-to-dock.gschema.override

%post
glib-compile-schemas /usr/share/glib-2.0/schemas/ 2>/dev/null
dconf update

%postun
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null
dconf update

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_datadir}/glib-2.0/schemas/10_tigeros.dash-to-dock.gschema.override

%changelog
* Sun Apr 01 2018 Tim Zabel <tjz8659@rit.edu>
- Created initial spec file
- Added gschema override
