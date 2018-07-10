# Disable debug because it should be empty but rpmlint rejects build
%define debug_package %{nil}

%define libname_orig %mklibname %{name}
%define libname %{libname_orig}0

%define devname suikyo-devel

Name:		suikyo
Summary:	Romaji-Kana conversion Library
Version:	2.1.0
Release:	20
Group:		System/Internationalization
License:	GPL
URL:		http://taiyaki.org/suikyo/
Source0:	%{name}-%{version}.tar.bz2
Requires:	ruby
BuildRequires:	ruby-devel

%package -n %{devname}
Summary:	Development files for %{name}
Requires:	%{name} = %{EVRD}

%description
Suikyo is Romaji-Kana conversion Library.

%description -n %{devname}
Development files for %{name}.

%prep
%setup -q

%build
[[ ! -x configure ]] && ./autogen.sh

%configure2_5x --with-rubydir=%{ruby_sitelibdir}
%make

%install
%makeinstall_std
rm -fr %{buildroot}%{_datadir}/doc

%files
%doc AUTHORS COPYING ChangeLog README
%{ruby_sitelibdir}/*
%{_datadir}/emacs/site-lisp/*
%{_datadir}/%{name}

%files -n %{devname}
%{_libdir}/pkgconfig/*
