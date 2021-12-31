#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fontquiver
Version  : 0.2.1
Release  : 20
URL      : https://cran.r-project.org/src/contrib/fontquiver_0.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fontquiver_0.2.1.tar.gz
Summary  : Set of Installed Fonts
Group    : Development/Tools
License  : GPL-3.0
Requires: R-fontBitstreamVera
Requires: R-fontLiberation
BuildRequires : R-fontBitstreamVera
BuildRequires : R-fontLiberation
BuildRequires : buildreq-R

%description
useful when you want to avoid system fonts to make sure your
    outputs are reproducible.

%prep
%setup -q -c -n fontquiver
cd %{_builddir}/fontquiver

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589577725

%install
export SOURCE_DATE_EPOCH=1589577725
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fontquiver
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fontquiver
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fontquiver
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fontquiver || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fontquiver/DESCRIPTION
/usr/lib64/R/library/fontquiver/INDEX
/usr/lib64/R/library/fontquiver/LICENSE
/usr/lib64/R/library/fontquiver/Meta/Rd.rds
/usr/lib64/R/library/fontquiver/Meta/features.rds
/usr/lib64/R/library/fontquiver/Meta/hsearch.rds
/usr/lib64/R/library/fontquiver/Meta/links.rds
/usr/lib64/R/library/fontquiver/Meta/nsInfo.rds
/usr/lib64/R/library/fontquiver/Meta/package.rds
/usr/lib64/R/library/fontquiver/NAMESPACE
/usr/lib64/R/library/fontquiver/NEWS.md
/usr/lib64/R/library/fontquiver/R/fontquiver
/usr/lib64/R/library/fontquiver/R/fontquiver.rdb
/usr/lib64/R/library/fontquiver/R/fontquiver.rdx
/usr/lib64/R/library/fontquiver/fonts/symbola-VERSION
/usr/lib64/R/library/fontquiver/fonts/symbola-fonts/Symbola.ttf
/usr/lib64/R/library/fontquiver/fonts/symbola-fonts/Symbola.woff
/usr/lib64/R/library/fontquiver/help/AnIndex
/usr/lib64/R/library/fontquiver/help/aliases.rds
/usr/lib64/R/library/fontquiver/help/fontquiver.rdb
/usr/lib64/R/library/fontquiver/help/fontquiver.rdx
/usr/lib64/R/library/fontquiver/help/paths.rds
/usr/lib64/R/library/fontquiver/html/00Index.html
/usr/lib64/R/library/fontquiver/html/R.css
/usr/lib64/R/library/fontquiver/tests/testthat.R
/usr/lib64/R/library/fontquiver/tests/testthat/test-fonts.R
/usr/lib64/R/library/fontquiver/tests/testthat/test-html-dependency.R
