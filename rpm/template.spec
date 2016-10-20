Name:           ros-indigo-aruco
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS aruco package

Group:          Development/Libraries
License:        BSD
URL:            http://www.uco.es/investiga/grupos/ava/node/26
Source0:        %{name}-%{version}.tar.gz

Requires:       opencv-devel
BuildRequires:  opencv-devel
BuildRequires:  ros-indigo-catkin

%description
The ARUCO Library has been developed by the Ava group of the Univeristy of
Cordoba(Spain). It provides real-time marker based 3D pose estimation using AR
markers.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Oct 20 2016 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

