Summary:	D2X-XL - port of Descent 2 to OpenGL
Summary(pl.UTF-8):	D2X-XL - port Descenta 2 do OpenGL-a
Name:		d2x-xl
Version:	1.14.158
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.descent2.de/downloads/%{name}-src-%{version}.rar
# Source0-md5:	84b4b5f5d9d8d9e2fce28df3154fc781
URL:		http://www.descent2.de/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.8
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	openmotif-devel
BuildRequires:	unrar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D2X-XL - port of Descent 2 to OpenGL.

%description -l pl.UTF-8
D2X-XL - port Descenta 2 do OpenGL-a.

%prep
%setup -q -c -T
unrar x -idq -o- %{SOURCE0}
# INSTALL file will be overwrited
rm INSTALL
unrar x -idq d2x-xl-makefiles.rar

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
chmod u+x configure
%configure
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
