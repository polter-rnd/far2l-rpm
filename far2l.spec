%global commit 920f22abae00f9f7d0592d3d21f78dc82a0c2f3a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global build_time %(date +"%Y%m%d")

%bcond_without gui
%if %{with gui}
Name: far2l
Conflicts: far2l-tty
%else
Name: far2l-tty
Conflicts: far2l
%endif
Version: 2.4
Release: git%{build_time}%{?dist}

Summary: Linux port of FAR v2

Group: File tools
License: GPLv2
Url: https://github.com/elfmz/far2l

Source0: https://github.com/elfmz/far2l/archive/%{commit}/far2l-%{shortcommit}.tar.gz

# Changes from VPROFi <v.l.snake.2000@gmail.com>
# https://github.com/VPROFi/far2l
Patch0: VPROFi-initial-changes.patch

BuildRequires: gawk m4
BuildRequires: cmake gcc-c++
%if %{with gui}
BuildRequires: (wxGTK-devel >= 3.0 or wxGTK3-devel)
%endif
BuildRequires: xerces-c-devel
BuildRequires: spdlog-devel
BuildRequires: uchardet-devel
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
%autosetup -n far2l-%{commit} -p1

%build
%set_build_flags
%if %{with gui}
cmake -DUSEWX=yes \
    -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} .
%else
cmake -DUSEWX=no \
    -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} .
%endif
%make_build

%install
%make_install

%files
%_bindir/far2l
%_prefix/lib/far2l/
%_datadir/far2l/
%_datadir/icons/far2l.svg
%_datadir/icons/hicolor/1024x1024/apps/far2l.svg
%_datadir/icons/hicolor/128x128/apps/far2l.svg
%_datadir/icons/hicolor/16x16/apps/far2l.svg
%_datadir/icons/hicolor/192x192/apps/far2l.svg
%_datadir/icons/hicolor/24x24/apps/far2l.svg
%_datadir/icons/hicolor/256x256/apps/far2l.svg
%_datadir/icons/hicolor/32x32/apps/far2l.svg
%_datadir/icons/hicolor/48x48/apps/far2l.svg
%_datadir/icons/hicolor/512x512/apps/far2l.svg
%_datadir/icons/hicolor/64x64/apps/far2l.svg
%_datadir/icons/hicolor/72x72/apps/far2l.svg
%_datadir/icons/hicolor/96x96/apps/far2l.svg
%_datadir/applications/far2l.desktop

%changelog
* Thu Jul 28 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.4-beta
- bump upstream commit (920f22a)
- add changes from VPROFi <v.l.snake.2000@gmail.com>

* Tue Jul 5 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.4-beta
- bump upstream commit (78c2802)
- require wxGTK3 or wxGTK (which is 3.1 on Fedora)

* Mon Apr 11 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.4-beta
- bump upstream commit (bcac692)

* Mon Apr 11 2022 Pavel Artsishevsky <polter.rnd@gmail.com> 2.3
- add pure console version (far2l-tty)

* Thu Sep 2 2021 Pavel Artsishevsky <polter.rnd@gmail.com> 2.3
- updated build requirements
- bump upstream commit

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
