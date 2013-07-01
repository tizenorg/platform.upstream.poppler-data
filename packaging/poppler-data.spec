Name:           poppler-data
Version:        0.4.6
Release:        0
License:        BSD-3-Clause ; GPL-2.0
Summary:        Encoding Files for use with libpoppler
Url:            http://poppler.freedesktop.org/
Group:          System/Libraries
Source:         http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
Source1001: 	poppler-data.manifest
BuildArch:      noarch

%description
This package consists of encoding files for use with poppler.  The
encoding files are optional and poppler will automatically read them if
they are present. When installed, the encoding files enables poppler
to correctly render CJK and Cyrrilic properly.

%prep
%setup -q
cp %{SOURCE1001} .

%build
make %{?_smp_mflags} prefix=%{_prefix}

%install
%makeinstall prefix=%{_prefix}

%files
%manifest %{name}.manifest
%defattr (-, root, root)
%license COPYING COPYING.adobe COPYING.gpl2
%{_datadir}/poppler

%changelog
