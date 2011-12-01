Name:           pbm2l2030
Version:        1.4
Release:        5.1%{?dist}
Summary:        Converts PBM stream to Lexmark 2030 printer language

Group:          System Environment/Libraries
License:        GPLv2+
# This is the original one, but has gone away...
#URL:            http://home.t-online.de/home/paetzold-net/page_004.html
# ...and as the original upstream author did not respond to e-mails,
# here is at least some reference:
URL:            http://www.linuxprinting.org/show_driver.cgi?driver=%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This is a filter to convert pbmraw data such as produced by ghostscript to
the printer language of Lexmark 2030 printers.  It is meant to be used
by the PostScript Description files of the drivers from the foomatic package.

%prep
%setup -q

%build
# The included Makefile is badly written
%{__cc} %{optflags} -o pbm2l2030 pbm2l2030.c pbm.c

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/%{_bindir}
%{__install} pbm2l2030 $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/pbm2l2030
%doc LICENSE README.TXT

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.4-5.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4-3
- Autorebuild for GCC 4.3

* Fri Aug 3 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.4-2
- Modify the License tag in accordance with the new guidelines

* Fri Jun 8 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.4-1
- Initial package
