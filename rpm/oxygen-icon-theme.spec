# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       oxygen-icon-theme

# >> macros
# << macros

Summary:    Oxygen icon theme
Version:    4.13.2
Release:    1
Group:      System/GUI/Other
License:    LGPLv2.1+
BuildArch:  noarch
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  oxygen-icon-theme.yaml
Source101:  oxygen-icon-theme-rpmlintrc
Requires:   kf5-filesystem
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes

%description
Oxygen icon theme.


%package large
Summary:    Oxygen icon theme, large and non-scalable version
Group:      System/GUI/Other
Requires:   %{name} = %{version}-%{release}

%description large
This package contains the large (128x128 and larger) non-scalable icons
of the Oxygen icon theme.


%package scalable
Summary:    Oxygen icon theme, scalable version
Group:      System/GUI/Other
Requires:   %{name} = %{version}-%{release}

%description scalable
This package contains the scalable icons of the Oxygen icon theme.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# hardlink reports
##/usr/sbin/hardlink -c -v %{buildroot}%{_datadir}/icons/oxygen

# create/own all potential dirs
mkdir -p %{buildroot}%{_datadir}/icons/oxygen/{16x16,22x22,24x24,32x32,36x36,48x48,64x64,96x96,128x128,512x512,scalable}/{actions,apps,devices,mimetypes,places}

# %%ghost icon.cache
touch  %{buildroot}%{_datadir}/icons/oxygen/icon-theme.cache

# fix duplicates
%fdupes %{buildroot}%{_datadir}/icons/oxygen
# << install post

%files
%defattr(-,root,root,-)
%doc AUTHORS CONTRIBUTING COPYING
%dir %{_datadir}/icons/oxygen/
%ghost %{_datadir}/icons/oxygen/icon-theme.cache
%exclude %{_datadir}/icons/oxygen/scalable/
%exclude %{_datadir}/icons/oxygen/128x128/
%exclude %{_datadir}/icons/oxygen/256x256/
%exclude %{_datadir}/icons/oxygen/512x512/
%{_datadir}/icons/oxygen/
# >> files
# << files

%files large
%defattr(-,root,root,-)
%{_datadir}/icons/oxygen/128x128/
%{_datadir}/icons/oxygen/256x256/
%{_datadir}/icons/oxygen/512x512/
# >> files large
# << files large

%files scalable
%defattr(-,root,root,-)
%{_datadir}/icons/oxygen/scalable/
# >> files scalable
# << files scalable
