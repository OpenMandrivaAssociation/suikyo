%define version 2.1.0
%define release	%mkrel 7

%define libname_orig %mklibname %{name}
%define libname %{libname_orig}0

Name:        suikyo
Summary:     Suikyo is Romaji-Kana conversion Library
Version:     %{version}
Release:     %{release}
Group:       System/Internationalization
License:     GPL
URL:         http://taiyaki.org/suikyo/
Source0:     %{name}-%{version}.tar.bz2
BuildRoot:   %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:       ruby
BuildRequires:  ruby-devel

%description
Suikyo is Romaji-Kana conversion Library.

%prep
%setup -q

%build
[[ ! -x configure ]] && ./autogen.sh

%configure2_5x --with-rubydir=%{ruby_sitelibdir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -fr $RPM_BUILD_ROOT%_datadir/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{ruby_sitelibdir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/emacs/site-lisp/*
%{_datadir}/%name

