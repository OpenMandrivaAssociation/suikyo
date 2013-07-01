# Disable debug because it should be empty but rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define libname_orig %mklibname %{name}
%define libname %{libname_orig}0

Name:		suikyo
Summary:	Is Romaji-Kana conversion Library
Version:	2.1.0
Release:	10
Group:		System/Internationalization
License:	GPL
URL:		http://taiyaki.org/suikyo/
Source0:	%{name}-%{version}.tar.bz2
Requires:	ruby
BuildRequires:	ruby-devel

%description
Suikyo is Romaji-Kana conversion Library.

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
%{_libdir}/pkgconfig/*
%{_datadir}/emacs/site-lisp/*
%{_datadir}/%{name}



%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-9mdv2011.0
+ Revision: 670236
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-8mdv2011.0
+ Revision: 607756
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-7mdv2010.1
+ Revision: 524137
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.1.0-6mdv2010.0
+ Revision: 427218
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.1.0-5mdv2009.0
+ Revision: 225511
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.1.0-4mdv2008.1
+ Revision: 171133
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue May 02 2006 Pascal Terjan <pterjan@mandriva.org> 2.1.0-3mdk
- ruby_libdir is already defined in ruby package
- use the macro in %%files to make the package build on x86_64

* Sat Apr 01 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 2.1.0-2mdk
- add "define ruby_libdir" to install suikyo properly

* Tue Mar 29 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 2.1.0-1mdk
- new release

* Fri Feb 18 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 2.0.1.2-1mdk
- new release

* Mon Jan 03 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0.1-0.1mdk
- do not package empty doc 
- do not own system directories
- initial spec for mdk (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)

