Summary: A real-time data compression library
Name: minilzo
Version: 2.03
Release: 6%{?dist}
Group: System Environment/Libraries
License: GPLv2+
Source0: http://www.oberhumer.com/opensource/lzo/download/lzo-%{version}.tar.gz
URL: http://www.oberhumer.com/opensource/lzo/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
#BuildRequires: automake19
BuildRequires: gcc-c++

%description
LZO is a portable lossless data compression library written in ANSI C.
It implements a number of algorithms with the following features:
- Decompression is simple and *very* fast.
- Requires no memory for decompression.
- Compression is pretty fast.
- Requires 64 kB of memory for compression.
- Allows you to dial up extra compression at a speed cost in the
  compressor. The speed of the decompressor is not reduced.
- Includes compression levels for generating pre-compressed data which
  achieve a quite competitive compression ratio.
- There is also a compression level which needs only 8 kB for
  compression.
- Supports overlapping compression and in-place decompression.
- Algorithm is thread safe.
- Algorithm is lossless.

%install
pwd
gcc -fPIC -g -c -Wall *.c
gcc -shared -Wl,-soname,libminilzo.so *.o -o libminilzo.so
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/lib64
mkdir -p %{buildroot}/usr/local/include/minilzo
cp libminilzo.so %{buildroot}/usr/local/lib64
cp *.h %{buildroot}/usr/local/include/minilzo

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/local/lib64/libminilzo.so
/usr/local/include/minilzo/*.h

%changelog
* Thu Aug 28 2008 root <root@junior.atrpms.net> - 2.03-5
- Update to 2.03.

* Sat Jun 14 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.02-4.0.1
- Fix not utf-8	specfile entries.

* Wed Jun  6 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.02-4
- Updgrade to 2.02.

* Mon Oct 30 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.08-3
- Use %%lib methods to create proper compat subpackage.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.
- Now exclude .la file.

* Tue Feb 18 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Spec file cleanup for Red Hat Linux 8.0.

* Sat Feb 15 2003 José Romildo Malaquias <malaquias@iceb.ufop.br> 1.08-1
- First spec file

