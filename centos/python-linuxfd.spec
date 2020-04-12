%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

# This is the name of this python module on the pip repository.
%define pipname linuxfd


Name:      python-%{pipname}
Version:   1.5
Release:   1%{?dist}
Summary:   Python bindings for the Linux eventfd/signalfd/timerfd/inotify syscalls.
License:   LGPL

Source0:   %{name}.tar.xz

%description
linuxfd provides a Python interface for the Linux system calls 'eventfd',
'signalfd', 'timerfd' and 'inotify'.

%package -n python2-%{pipname}
Summary:       Python2 bindings for the Linux eventfd/signalfd/timerfd/inotify syscalls.
BuildRequires: python2-devel
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires: python-setuptools
%else
BuildRequires: python2-setuptools
%endif
%{?python_provide:%python_provide python2-%{pipname}}

%description -n python2-%{pipname}
linuxfd provides a Python interface for the Linux system calls 'eventfd',
'signalfd', 'timerfd' and 'inotify'.

This is the Python2 version.


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pipname}
Summary:       Python3 bindings for the Linux eventfd/signalfd/timerfd/inotify syscalls.
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pipname}}

%description -n python%{python3_pkgversion}-%{pipname}
linuxfd provides a Python interface for the Linux system calls 'eventfd',
'signalfd', 'timerfd' and 'inotify'.

This is the Python3 version.
%endif


%prep
%setup -n python-%{pipname}


%build
%py2_build
%if %{with python3}
%py3_build
%endif


%install
%py2_install
%if %{with python3}
%py3_install
%endif


%files -n python2-%{pipname}
%doc README.md COPYING
%{python2_sitearch}/%{pipname}/
%{python2_sitearch}/%{pipname}-%{version}-py?.?.egg-info


%if %{with python3}
%files -n python%{python3_pkgversion}-%{pipname}
%doc README.md COPYING
%{python3_sitearch}/%{pipname}/
%{python3_sitearch}/%{pipname}-%{version}-py?.?.egg-info
%endif
