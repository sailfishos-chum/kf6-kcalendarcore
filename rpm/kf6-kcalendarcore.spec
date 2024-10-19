%global  kf_version 6.6.0

Name: kf6-kcalendarcore
Version: 6.6.0
Release: 0%{?dist}
Summary: Library for Interfacing with Calendars
License: LGPLv2+
URL:     https://invent.kde.org/frameworks/kcalendarcore
Source0: %{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  kf6-extra-cmake-modules >= %{majmin_ver_kf6}
BuildRequires:  kf6-rpm-macros
BuildRequires:  make

BuildRequires: kf6-kconfig-devel >= %{majmin_ver_kf6}

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-qtdeclarative-devel

BuildRequires: pkgconfig(libical)

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6CalendarCore.so.*

%files devel
%{_kf6_includedir}/KCalendarCore/
%{_kf6_libdir}/cmake/KF6CalendarCore/
%{_kf6_libdir}/libKF6CalendarCore.so
%{_qt6_docdir}/*.tags
%{_libdir}/pkgconfig/KF6CalendarCore.pc

%files doc
%{_qt6_docdir}/*.qch
