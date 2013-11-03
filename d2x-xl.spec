Summary:	D2X-XL - port of Descent 2 to OpenGL
Summary(pl.UTF-8):	D2X-XL - port Descenta 2 do OpenGL-a
Name:		d2x-xl
Version:	1.15.89
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.descent2.de/downloads/%{name}-src-%{version}.7z
# Source0-md5:	41355662b87111a228a34a1620d7b229
Patch0:		%{name}-byte.patch
URL:		http://www.descent2.de/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.8
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
#BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	glew-devel
BuildRequires:	motif-devel
BuildRequires:	p7zip
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D2X-XL - port of Descent 2 to OpenGL.

%description -l pl.UTF-8
D2X-XL - port Descenta 2 do OpenGL-a.

%prep
%setup -q -c -T -n %{name}
7z x %{SOURCE0}
7z x -y d2x-xl-makefiles.7z

%patch0 -p1
%{__sed} -i 's/-O3//' configure
%{__sed} -i '/dialheap.h/d' main/gamedata.cpp

%build
%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
%{__automake}
chmod u+x configure
%configure \
	LIBS="-lstdc++" \
	--enable-release=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
