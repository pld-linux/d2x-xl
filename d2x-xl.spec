Summary:	D2X-XL - port of Descent 2 to OpenGL
Summary(pl.UTF-8):	D2X-XL - port Descenta 2 do OpenGL-a
Name:		d2x-xl
Version:	1.13.81
Release:	0.1
License:	GPLv2
Group:		X11/Applications/Games
Source0:	http://www.descent2.de/downloads/%{name}-src-%{version}.rar
# Source0-md5:	de886c4abf7af7260ad949e0fd924ee5
URL:		http://www.descent2.de/
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	unrar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D2X-XL - port of Descent 2 to OpenGL.

%description -l pl.UTF-8
D2X-XL - port Descenta 2 do OpenGL-a.

%prep
%setup -q -c -T
unrar x -idq %{SOURCE0}
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
