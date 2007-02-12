Summary:	D2X-XL - port of Descent 2 to OpenGL
Summary(pl.UTF-8):   D2X-XL - port Descenta 2 do OpenGL-a
Name:		d2x-xl
Version:	1.5.112
Release:	0.1
License:	GPLv2
Group:		X11/Applications/Games
Source0:	http://www.descent2.de/resources/%{name}-src-%{version}.tgz
# Source0-md5:	8eefcfc57bcf27ff5fb91a3da750a87a
URL:		http://www.descent2.de/
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D2X-XL - port of Descent 2 to OpenGL.

%description -l pl.UTF-8
D2X-XL - port Descenta 2 do OpenGL-a.

%prep
%setup -q -n src

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
