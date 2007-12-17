%define pkgname Gazpacho
Summary: Gazpacho is a clone of the glade designer written in python and gtk
Name: gazpacho
Version: 0.7.2
Release: %mkrel 1
Source: http://ftp.gnome.org/pub/GNOME/sources/gazpacho/%{name}-%{version}.tar.bz2
License: LGPL
Group: Development/Python
BuildRequires: pygtk2.0-devel
BuildRequires: python-kiwi
BuildRequires: desktop-file-utils
Requires: python
Requires: python-kiwi
Url: http://gazpacho.sicem.biz/
Buildarch: noarch

%description
This program allows you to create the Graphical User Interface (GUI) of your
GTK+ program in a visual way. Yes, it is a Glade-3 clone. It is compatible with
libglade and it's on its early stages of development.
 
Gazpacho is part of the Gruppy framework but is not dependent of any part of
it so you can use it by its own.

%prep
%setup -q

%build
export LC_ALL=C
python%{pyver} setup.py build

%install
rm -rf $RPM_BUILD_ROOT %name.lang
export LC_ALL=C
python%{pyver} setup.py install --root=%{buildroot}
%find_lang %name
# menu
mkdir -p %{buildroot}/%{_menudir}
cat > %{buildroot}/%{_menudir}/%{name} <<EOF
?package(%{name}): \
command="%{_bindir}/%{name}" \
title="Gazpacho" \
longtitle="Clone of the glade designer written in python and gtk" \
needs="x11" \
icon="%{_datadir}/gazpacho/pixmaps/gazpacho-icon.png" \
section="More Applications/Development/Development Environments" \
startup_notify="yes" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Development-DevelopmentEnviroments" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc %_datadir/doc/%name/
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%_datadir/applications/%name.desktop
%{py_puresitedir}/*
%{_menudir}/%{name}


