%global commit 43057bdfe76532b2532c94149685df62e9d25205
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global build_time %(date +"%Y%m%d")

Name: far2l
Version: 2.0alpha
Release: git%{build_time}%{?dist}

Summary: Linux port of FAR v2

Group: File tools
License: GPLv2
Url: https://github.com/elfmz/far2l

Source0: https://github.com/elfmz/far2l/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: gawk m4
BuildRequires: cmake gcc-c++
BuildRequires: wxGTK3-devel
BuildRequires: libssh-devel
BuildRequires: openssl-devel
BuildRequires: libsmbclient-devel
BuildRequires: libnfs-devel
BuildRequires: neon-devel
BuildRequires: libarchive-devel
BuildRequires: pcre2-devel

%description
Linux port of FAR v2
ALPHA VERSION.
Currently interesting only for enthusiasts!!!

License: GNU/GPLv2

Used code from projects:
 - FAR for Windows
 - WINE
 - ANSICON
 - Portable UnRAR
 - 7z ANSI-C Decoder


%prep
%autosetup -n %{name}-%{commit}

%build
%set_build_flags
cmake -DUSEWX=yes \
    -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} .
%make_build

%install
%make_install

%files
%_bindir/%name
%_prefix/lib/%name/
%_datadir/%name/
%_datadir/icons/%name.svg
%_datadir/icons/hicolor/1024x1024/apps/%name.svg
%_datadir/icons/hicolor/128x128/apps/%name.svg
%_datadir/icons/hicolor/16x16/apps/%name.svg
%_datadir/icons/hicolor/192x192/apps/%name.svg
%_datadir/icons/hicolor/24x24/apps/%name.svg
%_datadir/icons/hicolor/256x256/apps/%name.svg
%_datadir/icons/hicolor/32x32/apps/%name.svg
%_datadir/icons/hicolor/48x48/apps/%name.svg
%_datadir/icons/hicolor/512x512/apps/%name.svg
%_datadir/icons/hicolor/64x64/apps/%name.svg
%_datadir/icons/hicolor/72x72/apps/%name.svg
%_datadir/icons/hicolor/96x96/apps/%name.svg
%_datadir/applications/%name.desktop

%changelog
* Wed Jul 1 2020 Pavel Artsishevsky <polter.rnd@gmail.com> 2.0-alpha
- removed glib2
- added with plugin dependencies

* Sat Sep 15 2018 Anton Midyukov <antohami@altlinux.org> 2.0-alt3.89d986a
- rebuilt with libwxGTK3.0

* Sat Jul 07 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt2.89d986a
- new git build 89d986a

* Wed Jan 04 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt2.4d33a48
- new git build 4d33a48

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1.4198cd5
- new git build 4198cd5

* Sat Aug 20 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- initial build for ALT Linux Sisyphus
